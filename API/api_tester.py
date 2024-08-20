import requests

url = "http://127.0.0.1:5000/create-video"

data = {
    "images": [
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-8ZoXJveZuiladdCUztd7LdRg.png?st=2024-08-20T06%3A18%3A12Z&se=2024-08-20T08%3A18%3A12Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A12%3A35Z&ske=2024-08-20T23%3A12%3A35Z&sks=b&skv=2024-08-04&sig=jq65Z%2BW577nu%2BZBYkQmCsJ1dsOf%2BjJKmuf6rxBQbTYo%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-0Zy1ZrvfSGnbou7OivbmO1xB.png?st=2024-08-20T06%3A18%3A20Z&se=2024-08-20T08%3A18%3A20Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A16%3A59Z&ske=2024-08-20T23%3A16%3A59Z&sks=b&skv=2024-08-04&sig=MwSYQ5UnyuXnJsYxXu8V4JFog%2BqWfSI/b4dOAQk48cg%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-2TbcATsM6Hp5FCpSBVXC3YOF.png?st=2024-08-20T06%3A18%3A30Z&se=2024-08-20T08%3A18%3A30Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A13%3A31Z&ske=2024-08-20T23%3A13%3A31Z&sks=b&skv=2024-08-04&sig=yLWkcuFFL8jNXndjivO2fZ4aSc76ol%2BUV63kgEBMiZ4%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-2G4a3trngRNLZA7XTDeHAxiC.png?st=2024-08-20T06%3A18%3A38Z&se=2024-08-20T08%3A18%3A38Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A16%3A52Z&ske=2024-08-20T23%3A16%3A52Z&sks=b&skv=2024-08-04&sig=TYqYWFbOIhl0dZvZ1H2TpaSjPcfiGC3Gi3bEokoZPSg%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-Uwk4hqJMGojnUvRKB2FA76Th.png?st=2024-08-20T06%3A18%3A49Z&se=2024-08-20T08%3A18%3A49Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A07%3A09Z&ske=2024-08-20T23%3A07%3A09Z&sks=b&skv=2024-08-04&sig=rUyAglK3pseIdhSTTrOESsHJFZvJ8unYl7%2BpDhQ7qA8%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-BM0i0QfiILwBNcitmNtDe6Vr.png?st=2024-08-20T06%3A18%3A57Z&se=2024-08-20T08%3A18%3A57Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-20T05%3A39%3A44Z&ske=2024-08-21T05%3A39%3A44Z&sks=b&skv=2024-08-04&sig=hpeTgFQyqgRAlOu6XCKlvDz4SDP/mU030Tc9mfE4ysI%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-oLVpmhdYJMhy1DcNI0G4bAPD.png?st=2024-08-20T06%3A19%3A06Z&se=2024-08-20T08%3A19%3A06Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A19%3A40Z&ske=2024-08-20T23%3A19%3A40Z&sks=b&skv=2024-08-04&sig=PSVga56jIGFZsoBkpa8Mlu9RrM8yDQrjCxro0d%2BEawU%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-P7CawF1LK3VtI9ifFqqbmfpP.png?st=2024-08-20T06%3A19%3A14Z&se=2024-08-20T08%3A19%3A14Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A09%3A46Z&ske=2024-08-20T23%3A09%3A46Z&sks=b&skv=2024-08-04&sig=V2sM7fLHGW6pp3/2uA5dEphVEijBvvePMicYvCgA0bE%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-kuBwZu9EI2AXixnUnqltyfJI.png?st=2024-08-20T06%3A19%3A22Z&se=2024-08-20T08%3A19%3A22Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A19%3A30Z&ske=2024-08-20T23%3A19%3A30Z&sks=b&skv=2024-08-04&sig=rKZaJ1u2T5mtwUG5r4bz4mrpLPnxX2JJFuk5cf%2Bcy6E%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-1ODK8wLInmzHh2xeYDD56IfL.png?st=2024-08-20T06%3A19%3A31Z&se=2024-08-20T08%3A19%3A31Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A14%3A53Z&ske=2024-08-20T23%3A14%3A53Z&sks=b&skv=2024-08-04&sig=YMm%2Bu7kFPl4EkfjHGIlwpWEHeLx0upKdJdfcROmGHy4%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-rRT7iWjvlhxXVGUNLc3ZUBrr.png?st=2024-08-20T06%3A19%3A39Z&se=2024-08-20T08%3A19%3A39Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A16%3A05Z&ske=2024-08-20T23%3A16%3A05Z&sks=b&skv=2024-08-04&sig=fpE5BkG2Og3Yvr3oFSdYClvLMK7Dw3nIO%2BVJugDZOtA%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-PFVfme08hrol561dkGIcy3uY.png?st=2024-08-20T06%3A19%3A47Z&se=2024-08-20T08%3A19%3A47Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A23%3A32Z&ske=2024-08-20T23%3A23%3A32Z&sks=b&skv=2024-08-04&sig=ODchTuJK7R4HepXp/BzHHVAZhK/I468lMai/oAnnPis%3D",
        "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-WtmBLF9T51HGSykzqFEDf2NM.png?st=2024-08-20T06%3A19%3A56Z&se=2024-08-20T08%3A19%3A56Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A43%3A27Z&ske=2024-08-20T23%3A43%3A27Z&sks=b&skv=2024-08-04&sig=BFJAlxtsJaRajOTmMfO2Kp/IdbmaX%2BEEU//eCJG4xuQ%3D"
    ],
    "audio_clips": ["output_0.mp3","output_1.mp3","output_2.mp3","output_3.mp3","output_4.mp3","output_5.mp3","output_6.mp3","output_7.mp3","output_8.mp3","output_9.mp3","output_10.mp3","output_11.mp3","output_12.mp3"]
}

response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Request was successful.")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)

# data = {
#     "images": [
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-8ZoXJveZuiladdCUztd7LdRg.png?st=2024-08-20T06%3A18%3A12Z&se=2024-08-20T08%3A18%3A12Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A12%3A35Z&ske=2024-08-20T23%3A12%3A35Z&sks=b&skv=2024-08-04&sig=jq65Z%2BW577nu%2BZBYkQmCsJ1dsOf%2BjJKmuf6rxBQbTYo%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-0Zy1ZrvfSGnbou7OivbmO1xB.png?st=2024-08-20T06%3A18%3A20Z&se=2024-08-20T08%3A18%3A20Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A16%3A59Z&ske=2024-08-20T23%3A16%3A59Z&sks=b&skv=2024-08-04&sig=MwSYQ5UnyuXnJsYxXu8V4JFog%2BqWfSI/b4dOAQk48cg%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-2TbcATsM6Hp5FCpSBVXC3YOF.png?st=2024-08-20T06%3A18%3A30Z&se=2024-08-20T08%3A18%3A30Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A13%3A31Z&ske=2024-08-20T23%3A13%3A31Z&sks=b&skv=2024-08-04&sig=yLWkcuFFL8jNXndjivO2fZ4aSc76ol%2BUV63kgEBMiZ4%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-2G4a3trngRNLZA7XTDeHAxiC.png?st=2024-08-20T06%3A18%3A38Z&se=2024-08-20T08%3A18%3A38Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A16%3A52Z&ske=2024-08-20T23%3A16%3A52Z&sks=b&skv=2024-08-04&sig=TYqYWFbOIhl0dZvZ1H2TpaSjPcfiGC3Gi3bEokoZPSg%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-Uwk4hqJMGojnUvRKB2FA76Th.png?st=2024-08-20T06%3A18%3A49Z&se=2024-08-20T08%3A18%3A49Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A07%3A09Z&ske=2024-08-20T23%3A07%3A09Z&sks=b&skv=2024-08-04&sig=rUyAglK3pseIdhSTTrOESsHJFZvJ8unYl7%2BpDhQ7qA8%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-BM0i0QfiILwBNcitmNtDe6Vr.png?st=2024-08-20T06%3A18%3A57Z&se=2024-08-20T08%3A18%3A57Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-20T05%3A39%3A44Z&ske=2024-08-21T05%3A39%3A44Z&sks=b&skv=2024-08-04&sig=hpeTgFQyqgRAlOu6XCKlvDz4SDP/mU030Tc9mfE4ysI%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-oLVpmhdYJMhy1DcNI0G4bAPD.png?st=2024-08-20T06%3A19%3A06Z&se=2024-08-20T08%3A19%3A06Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A19%3A40Z&ske=2024-08-20T23%3A19%3A40Z&sks=b&skv=2024-08-04&sig=PSVga56jIGFZsoBkpa8Mlu9RrM8yDQrjCxro0d%2BEawU%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-P7CawF1LK3VtI9ifFqqbmfpP.png?st=2024-08-20T06%3A19%3A14Z&se=2024-08-20T08%3A19%3A14Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A09%3A46Z&ske=2024-08-20T23%3A09%3A46Z&sks=b&skv=2024-08-04&sig=V2sM7fLHGW6pp3/2uA5dEphVEijBvvePMicYvCgA0bE%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-kuBwZu9EI2AXixnUnqltyfJI.png?st=2024-08-20T06%3A19%3A22Z&se=2024-08-20T08%3A19%3A22Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A19%3A30Z&ske=2024-08-20T23%3A19%3A30Z&sks=b&skv=2024-08-04&sig=rKZaJ1u2T5mtwUG5r4bz4mrpLPnxX2JJFuk5cf%2Bcy6E%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-1ODK8wLInmzHh2xeYDD56IfL.png?st=2024-08-20T06%3A19%3A31Z&se=2024-08-20T08%3A19%3A31Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A14%3A53Z&ske=2024-08-20T23%3A14%3A53Z&sks=b&skv=2024-08-04&sig=YMm%2Bu7kFPl4EkfjHGIlwpWEHeLx0upKdJdfcROmGHy4%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-rRT7iWjvlhxXVGUNLc3ZUBrr.png?st=2024-08-20T06%3A19%3A39Z&se=2024-08-20T08%3A19%3A39Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A16%3A05Z&ske=2024-08-20T23%3A16%3A05Z&sks=b&skv=2024-08-04&sig=fpE5BkG2Og3Yvr3oFSdYClvLMK7Dw3nIO%2BVJugDZOtA%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-PFVfme08hrol561dkGIcy3uY.png?st=2024-08-20T06%3A19%3A47Z&se=2024-08-20T08%3A19%3A47Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A23%3A32Z&ske=2024-08-20T23%3A23%3A32Z&sks=b&skv=2024-08-04&sig=ODchTuJK7R4HepXp/BzHHVAZhK/I468lMai/oAnnPis%3D",
#         "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oyvjf4q86YNb2QYzhnaoUAUP/user-dNkEchEx3A08nAECjlJKblCC/img-WtmBLF9T51HGSykzqFEDf2NM.png?st=2024-08-20T06%3A19%3A56Z&se=2024-08-20T08%3A19%3A56Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-08-19T23%3A43%3A27Z&ske=2024-08-20T23%3A43%3A27Z&sks=b&skv=2024-08-04&sig=BFJAlxtsJaRajOTmMfO2Kp/IdbmaX%2BEEU//eCJG4xuQ%3D"
#     ]
# }

# images = data["images"]
# audio_clips = ["output_0.mp3","output_1.mp3","output_2.mp3","output_3.mp3","output_4.mp3","output_5.mp3","output_6.mp3","output_7.mp3","output_8.mp3","output_9.mp3","output_10.mp3","output_11.mp3","output_12.mp3"]
# create_video(images, audio_clips)
