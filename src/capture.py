import requests

from pathlib import Path

from datetime import datetime


IMAGE_FOLDER = Path(__file__).resolve().parent.parent / "images"


def capture_image(camera_name, ip):

    IMAGE_FOLDER.mkdir(exist_ok=True)

    camera_folder = IMAGE_FOLDER / camera_name

    camera_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    url = f"http://{ip}:8080/capture"

    response = requests.get(
        url,
        timeout=5
    )

    if response.status_code != 200:
        return False

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = camera_folder / f"{timestamp}.jpg"

    with open(file_path, "wb") as file:
        file.write(response.content)

    return str(file_path)