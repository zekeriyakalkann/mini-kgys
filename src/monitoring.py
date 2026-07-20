import subprocess
import requests
import time

from datetime import datetime

from database import get_all_cameras, update_camera_status
from logger import info, warning

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

def http_check(ip):

    try:

        start = time.perf_counter()

        response = requests.get(
            f"http://{ip}",
            timeout=2
        )

        end = time.perf_counter()

        response_time = round((end - start) * 1000, 2)

        if response.status_code == 200:
            return True, response_time

        return False, None

    except:

        return False, None

def check_cameras():

    print("\n========================================")
    print("         MONITORING BASLADI")
    print("========================================")

    cameras = get_all_cameras()

    online_count = 0
    offline_count = 0

    for camera in cameras:

        print(f"\nKamera : {camera['name']}")
        print(f"IP     : {camera['ip']}")

        ping_ok, ping_time = ping_camera(camera["ip"])
        http_ok, http_time = http_check(camera["ip"])

        print("----------------------------------------")

        if ping_ok:
            print(f"Ping   : OK ({ping_time} ms)")
        else:
            print("Ping   : FAILED")

        if http_ok:
            print(f"HTTP   : OK ({http_time} ms)")
        else:
            print("HTTP   : FAILED")

        if ping_ok and http_ok:

            status = "ONLINE"

            online_count += 1

            update_camera_status(
                camera["id"],
                status
            )

            info(f"{camera['name']} ONLINE")

        else:

            status = "OFFLINE"

            offline_count += 1

            update_camera_status(
                camera["id"],
                status
            )

            warning(f"{camera['name']} OFFLINE")

        print(f"Status : {status}")

    print("\n========================================")
    print("Monitoring Tamamlandi")
    print("----------------------------------------")
    print(f"Online  : {online_count}")
    print(f"Offline : {offline_count}")
    print("========================================")