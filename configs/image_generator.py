import uuid
import requests
from .settings import API_URL, REQUEST_HEADERS, MEDIA_DIR, BASE_DIR


def generate_image(prompt):
    response = requests.post(API_URL, headers=REQUEST_HEADERS, json={"inputs": prompt + " " + "4k"})
    if response.status_code == 200:
        image_path = f"{BASE_DIR}/media/{uuid.uuid4()}.png"
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Image to {image_path}")
        return image_path
    else:
        print("Error:", response.json())
