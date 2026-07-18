import subprocess

from database import get_all_cameras, update_camera_status
from logger import info, warning


def check_cameras():

    print("\nMonitoring basladi")

    cameras = get_all_cameras()

    for camera in cameras:

        print(f"Kontrol ediliyor: {camera['name']}")

        result = subprocess.run(
            ["ping", "-c", "1", camera["ip"]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:

            update_camera_status(camera["id"], "ONLINE")

            info(f"{camera['name']} ONLINE")

            print(f"DEBUG: {camera['name']} -> ONLINE")

        else:

            update_camera_status(camera["id"], "OFFLINE")

            warning(f"{camera['name']} OFFLINE")

            print(f"DEBUG: {camera['name']} -> OFFLINE")

    print("\nMonitoring bitti")