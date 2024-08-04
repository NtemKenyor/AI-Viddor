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

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)

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

def create_video(images, audio_clips, output_file="output_video.mp4"):
    video_clips = []
    for image_url, audio_file in zip(images, audio_clips):
        image_clip = ImageClip(image_url).set_duration(AudioFileClip(audio_file).duration)
        audio_clip = AudioFileClip(audio_file)
        image_clip = image_clip.set_audio(audio_clip)
        video_clips.append(image_clip)

    final_video = concatenate_videoclips(video_clips, method="compose")
    final_audio = concatenate_audioclips([AudioFileClip(audio) for audio in audio_clips])
    final_video = final_video.set_audio(final_audio)
    final_video.write_videofile(output_file, fps=24)

def clean_output_directory(directory="."):
    for file in os.listdir(directory):
        if file.startswith("output") and (file.endswith(".mp3") or file.endswith(".mp4")):
            os.remove(os.path.join(directory, file))

@app.route('/generate-prompt', methods=['GET'])
def api_generate_prompt():
    prompt = generate_random_prompt()
    return jsonify({"prompt": prompt})

@app.route('/generate-text', methods=['POST'])
def api_generate_text():
    data = request.json
    message = data.get('message')
    text = generate_text(message)
    return jsonify({"text": text})

@app.route('/generate-images', methods=['POST'])
def api_generate_images():
    data = request.json
    prompts = data.get('prompts')
    images = generate_images(prompts)
    return jsonify({"images": images})

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
    create_video(images, audio_clips, output_file)
    return send_file(output_file, as_attachment=True)

@app.route('/clean-output-directory', methods=['POST'])
def api_clean_output_directory():
    clean_output_directory()
    return jsonify({"message": "Output directory cleaned"})

if __name__ == '__main__':
    app.run(debug=True)
