import subprocess
import requests
import time

from events import add_event
from database import (
    get_all_cameras,
    get_camera_status,
    update_camera_monitoring
)
from logger import info, warning
from capture import capture_image


# -------------------------------------------------
# Ping Test
# -------------------------------------------------

def ping_camera(ip):

    start = time.perf_counter()

    result = subprocess.run(
        ["ping", "-c", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    end = time.perf_counter()

    response_time = round((end - start) * 1000, 2)

    if result.returncode == 0:
        return True, response_time

    return False, None


# -------------------------------------------------
# HTTP Health Check
# -------------------------------------------------

def http_check(ip):

    try:

        start = time.perf_counter()

        response = requests.get(
            f"http://{ip}:8080/health",
            timeout=2
        )

        end = time.perf_counter()

        response_time = round((end - start) * 1000, 2)

        if response.status_code == 200:
            return True, response_time

        return False, None

    except Exception:

        return False, None


# -------------------------------------------------
# Monitor Single Camera
# -------------------------------------------------

def monitor_camera(camera):

    result = {
        "id": camera["id"],
        "name": camera["name"],
        "ip": camera["ip"],
        "status": "OFFLINE",
        "ping": None,
        "http": None,
        "image": None
    }

    ping_ok, ping_time = ping_camera(camera["ip"])
    result["ping"] = ping_time

    if not ping_ok:
        return result

    http_ok, http_time = http_check(camera["ip"])
    result["http"] = http_time

    if not http_ok:
        return result

    image_path = capture_image(
        camera["name"],
        camera["ip"]
    )

    result["image"] = image_path
    result["status"] = "ONLINE"

    return result


# -------------------------------------------------
# Monitoring
# -------------------------------------------------

def check_cameras():

    print("\n========================================")
    print("         MONITORING BASLADI")
    print("========================================")

    cameras = get_all_cameras()

    online_count = 0
    offline_count = 0

    for camera in cameras:

        result = monitor_camera(camera)

        print(f"\nKamera : {result['name']}")
        print(f"IP     : {result['ip']}")
        print("----------------------------------------")

        if result["ping"] is not None:
            print(f"Ping   : OK ({result['ping']} ms)")
        else:
            print("Ping   : FAILED")

        if result["http"] is not None:
            print(f"HTTP   : OK ({result['http']} ms)")
        else:
            print("HTTP   : FAILED")

        print(f"Status : {result['status']}")

        if result["image"] is not None:
            print(f"Image  : {result['image']}")

        # ----------------------------------------
        # State Change Detection
        # ----------------------------------------

        old_status = get_camera_status(result["id"])

        # ----------------------------------------
        # Database Update
        # ----------------------------------------

        update_camera_monitoring(
            result["id"],
            result["status"],
            result["ping"],
            result["http"],
            result["image"]
        )

        # ----------------------------------------
        # ONLINE / OFFLINE Events
        # ----------------------------------------

        if old_status != result["status"]:

            if result["status"] == "ONLINE":

                add_event(
                    result["id"],
                    "ONLINE",
                    f"{result['name']} is online."
                )

            else:

                add_event(
                    result["id"],
                    "OFFLINE",
                    f"{result['name']} is offline."
                )

        # ----------------------------------------
        # Capture Event
        # ----------------------------------------

        if result["image"] is not None:

            add_event(
                result["id"],
                "CAPTURE",
                "Image captured successfully."
            )

        # ----------------------------------------
        # Log & Statistics
        # ----------------------------------------

        if result["status"] == "ONLINE":

            online_count += 1

            info(
                f"{result['name']} ONLINE"
            )

        else:

            offline_count += 1

            warning(
                f"{result['name']} OFFLINE"
            )

    print("\n========================================")
    print("Monitoring Tamamlandi")
    print("----------------------------------------")
    print(f"Online  : {online_count}")
    print(f"Offline : {offline_count}")
    print("========================================")