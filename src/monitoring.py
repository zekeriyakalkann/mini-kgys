import subprocess

from datetime import datetime

from database import get_all_cameras, update_camera_status
from logger import info, warning


def check_cameras():

    online_count = 0
    offline_count = 0

    print("\n========== Monitoring Basladi ==========\n")

    cameras = get_all_cameras()

    for camera in cameras:

        old_status = camera["status"]

        print(f"Kontrol Ediliyor : {camera['name']} ({camera['ip']})")

        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", camera["ip"]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:

            new_status = "ONLINE"
            online_count += 1

        else:

            new_status = "OFFLINE"
            offline_count += 1

        if old_status != new_status:

            update_camera_status(camera["id"], new_status)

            if new_status == "ONLINE":

                info(f"{camera['name']} ONLINE")

            else:

                warning(f"{camera['name']} OFFLINE")

        print(f"Durum : {new_status}\n")

    print("========== Monitoring Ozeti ==========")
    print(f"Kontrol Zamani : {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"Toplam Kamera  : {len(cameras)}")
    print(f"Online         : {online_count}")
    print(f"Offline        : {offline_count}")
    print("======================================")