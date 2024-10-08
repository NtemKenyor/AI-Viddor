from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import random
import json
import openai
from gtts import gTTS
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips
from dotenv import load_dotenv
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)


# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_random_prompt():
    prompts = [
        "List key tactics used by Roman legions in the Battle of Cannae.",
        # Add more prompts...
    ]
    return random.choice(prompts)

def generate_text(message, max_tokens=300):
    messages = [{"role": "system", "content": "You are a great presenter. Capture the audience with your first sentence. Try to end every story/topic you start with some simple lesson, moral or facts"}]
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.7,
        )
    reply = chat.choices[0].message.content
    return reply

def generate_painter(message, max_tokens=3000, canvas_structure=None):
    # Example: structure for canvas elements (adjust according to your needs)
    canvas_elements_ = f'''canvas_elements = {canvas_structure}'''
    messages = [{f"role": "system", "content": f"You are a skilled canvas painter and creative. Make sure you fill up over 70% of the entire canvas. you are very good in drawing. Only return a 'canvas_elements' json structure like this: {canvas_elements_} . I repeat, only return a json structure. do not add any other sentence only rturn a json struture."}]
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.7,
        )
    reply = chat.choices[0].message.content
    return reply

def text_to_image_prompts(text):
    sentences = text.split('.')
    prompts = [sentence.strip() for sentence in sentences if sentence]
    ai_prompt = [generate_text(f" Given this sentence: {prompt} , Generate a detailed descriptive and yet safe prompt for the OPENAI image generator. Avoid adding text that would be detected by the safety system", max_tokens=70) for prompt in prompts if prompts]
    return ai_prompt

def generate_images(prompts):
    images = []
    for prompt in prompts:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"  # Adjust the size as needed
        )
        image_url = response['data'][0]['url']
        images.append(image_url)
    return images

def generate_audio(text, filename="output.mp3", speed=1.5):
    tts = gTTS(text)
    tts.save(filename)
    return filename

# def create_video(images, audio_clips, output_file="output_video.mp4"):
#     video_clips = []
#     for image_url, audio_file in zip(images, audio_clips):
#         image_clip = ImageClip(image_url).set_duration(AudioFileClip(audio_file).duration)
#         audio_clip = AudioFileClip(audio_file)
#         image_clip = image_clip.set_audio(audio_clip)
#         video_clips.append(image_clip)

#     final_video = concatenate_videoclips(video_clips, method="compose")
#     final_audio = concatenate_audioclips([AudioFileClip(audio) for audio in audio_clips])
#     final_video = final_video.set_audio(final_audio)
#     final_video.write_videofile(output_file, fps=24)

def create_video(images, audio_clips, output_file="output_video.mp4"):
    video_clips = []
    
    try:
        # Process each image and audio pair
        for image_url, audio_file in zip(images, audio_clips):
            # Load and process the image
            image_clip = ImageClip(image_url)
            audio_clip = AudioFileClip(audio_file)
            
            # Set duration and audio
            image_clip = image_clip.set_duration(audio_clip.duration).set_audio(audio_clip)
            video_clips.append(image_clip)

            # Close the audio and image clips to free up resources
            audio_clip.close()
            image_clip.close()
        
        # Concatenate video and audio clips
        final_video = concatenate_videoclips(video_clips, method="compose")
        final_audio = concatenate_audioclips([AudioFileClip(audio) for audio in audio_clips])
        
        # Set the final audio to the final video
        final_video = final_video.set_audio(final_audio)
        
        # Write the video file
        final_video.write_videofile(output_file, fps=24)
    
    except Exception as e:
        print(f"An error occurred during video creation: {e}")
    
    finally:
        # Clean up resources
        for clip in video_clips:
            clip.close()
        for audio in audio_clips:
            # audio.close()
            pass

def clean_output_directory(directory="."):
    for file in os.listdir(directory):
        if file.startswith("output") and (file.endswith(".mp3") or file.endswith(".mp4")):
            os.remove(os.path.join(directory, file))


import json

def get_canvas_standard():
    canvas_standard = {
        "shapes": [
            {
                "type": "ellipse",
                "cx": 150,
                "cy": 100,
                "rx": 80,
                "ry": 50,
                "color": "rgba(255, 0, 0, 0.5)"
            },
            {
                "type": "rectangle",
                "x": 50,
                "y": 50,
                "width": 200,
                "height": 100,
                "color": "rgba(0, 255, 0, 0.5)",
                "borderColor": "black",
                "borderWidth": 2
            },
            {
                "type": "line",
                "x1": 300,
                "y1": 50,
                "x2": 500,
                "y2": 150,
                "color": "blue",
                "lineWidth": 5
            },
            {
                "type": "text",
                "x": 200,
                "y": 300,
                "text": "Hello, Canvas!",
                "font": "20px Arial",
                "color": "black"
            },
            {
                "type": "multi-dot",
                "positions": [
                    {"x": 100, "y": 100},
                    {"x": 150, "y": 150},
                    {"x": 200, "y": 200},
                    {"x": 250, "y": 250}
                ],
                "radius": 5,
                "color": "purple"
            },
            {
                "type": "arc",
                "cx": 600,
                "cy": 200,
                "radius": 50,
                "startAngle": 0,
                "endAngle": 3.14,
                "color": "orange",
                "lineWidth": 4
            },
            {
                "type": "circle",
                "cx": 700,
                "cy": 300,
                "radius": 40,
                "color": "rgba(0, 0, 255, 0.5)",
                "borderColor": "black",
                "borderWidth": 2
            }
        ]
    }
    
    return canvas_standard

# Example usage
# canvas_standard = get_canvas_standard()
# print(json.dumps(canvas_standard, indent=4))

def extract_json_from_text(text):
    """
    Function to extract and clean JSON structure from the AI-generated text.
    Assumes that the JSON structure is embedded within the text output.
    """

    # Import necessary modules
    import json
    import re

    # Use a regular expression to find JSON-like structures in the text
    json_like_structures = re.findall(r'\{.*?\}', text, re.DOTALL)

    # If a structure is found, try to parse it as JSON
    if json_like_structures:
        for json_str in json_like_structures:
            try:
                # Attempt to parse the JSON string
                parsed_json = json.loads(json_str)
                return parsed_json
            except json.JSONDecodeError:
                continue

    # If no JSON structure is found or parsed, return an empty list
    return []  # or an appropriate fallback structure




app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def welcome():
    # prompt = generate_random_prompt()
    print("still on test...")
    return jsonify({"prompt": "WELCOME TO AI VIDDOR API"})


@app.route('/generate-prompt', methods=['GET'])
def api_generate_prompt():
    prompt = generate_random_prompt()
    return jsonify({"prompt": prompt})


@app.route('/generate-paint', methods=['POST'])
def api_generate_paint():
    # Initialize the canvas structure or call a function to define it
    THE_CANVAS_STRUCTURE = get_canvas_standard() 

    # Receive and process the incoming JSON data
    data = request.json
    message = data.get('prompt')
    canvas_height = data.get('height')
    canvas_width = data.get('width')

    # Create the final prompt including canvas dimensions
    final_prompt = f"{message} - Put into consideration that the canvas has height: {canvas_height} and width: {canvas_width} so do not exceed it"

    # Call the AI model to generate the painter data
    generated_data = generate_painter(message=final_prompt, canvas_structure=THE_CANVAS_STRUCTURE)

    # Print statements for debugging (optional)
    print("Original Prompt:", message)
    print("Generated Data:", generated_data)

    # Extract JSON structure from the AI's output (assume the output is a mix of text and JSON)
    # This function would clean and extract the JSON data
    canvas_elements = extract_json_from_text(generated_data)

    # Return the entire text and the cleaned JSON structure
    return jsonify({"text": generated_data, "canvasElements": canvas_elements})


@app.route('/generate-text', methods=['POST'])
def api_generate_text():
    data = request.json
    message = data.get('message')
    text = generate_text(message)
    print(message)
    print(text)
    return jsonify({"text": text})


@app.route('/generate-images', methods=['POST'])
def api_generate_images():
    try:
        logging.info("Received request to generate images")
        data = request.json
        logging.debug(f"Request JSON data: {data}")
        
        if not data or 'prompts' not in data:
            logging.error("No prompts found in the request")
            return jsonify({"error": "No prompts provided"}), 400

        prompts = data.get('prompts')
        logging.debug(f"Prompts: {prompts}")

        images = generate_images(prompts)
        logging.info(f"Generated images: {images}")

        return jsonify({"images": images})

    except Exception as e:
        logging.exception("An error occurred while generating images")
        return jsonify({"error": str(e)}), 500


@app.route('/generate-audio', methods=['POST'])
def api_generate_audio():
    data = request.json
    text = data.get('text')
    filename = data.get('filename', 'output.mp3')
    audio_file = generate_audio(text, filename)
    return send_file(audio_file, as_attachment=True)

@app.route('/create-video', methods=['POST'])
def api_create_video():
    data = request.json
    images = data.get('images')
    audio_clips = data.get('audio_clips')
    output_file = data.get('output_file', 'output_video.mp4')
    # return data
    create_video(images, audio_clips, output_file)
    return send_file(output_file, as_attachment=True)

@app.route('/clean-output-directory', methods=['POST'])
def api_clean_output_directory():
    clean_output_directory()
    return jsonify({"message": "Output directory cleaned"})

# if __name__ == '__main__':
    # app.run(debug=True)
