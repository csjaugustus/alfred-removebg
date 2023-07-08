import os
from PIL import Image
import requests
import sys
import json

api_key = os.environ['api_key']

def convert_to_png(image_path):
    img = Image.open(image_path)
    new_image_path = os.path.splitext(image_path)[0] + ".png"
    img.save(new_image_path, "png")
    os.remove(image_path)
    return new_image_path

def remove_background(image_path):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(image_path, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': api_key},
    )
    if response.status_code == requests.codes.ok:
        new_image_path = os.path.splitext(image_path)[0] + ".png"
        with open(new_image_path, 'wb') as out:
            out.write(response.content)
    else:
        errors.append("Error:", response.status_code, response.text)

errors = []
file_paths = sys.argv[1].split()
for fp in file_paths:
    if fp.endswith((".webp", ".jpeg", ".jpg")):
        n = convert_to_png(fp)
        remove_background(n)
    if fp.endswith(".png"):
        remove_background(fp)

if errors:
    print("\n".join(errors))
else:
    if len(file_paths) == 1:
        print(f"Successfully removed background for {os.path.basename(file_paths[0])}.")
    else:
        print(f"Successfully removed backgrounds for {len(file_paths)} images.")
