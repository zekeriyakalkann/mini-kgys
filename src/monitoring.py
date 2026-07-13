import subprocess

from camera import cameras
from logger import info, warning


def check_cameras():

    for camera in cameras:

        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", camera["ip"]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:

            camera["status"] = "ONLINE"

            info(f"{camera['name']} ONLINE")

        else:

            camera["status"] = "OFFLINE"

            warning(f"{camera['name']} OFFLINE")