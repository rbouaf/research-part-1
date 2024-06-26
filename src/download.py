import requests
import os

def download_image(url, folder_path, file_name):
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Full path for saving the image
    file_path = os.path.join(folder_path, file_name)

    # Download the image
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download {url}")

