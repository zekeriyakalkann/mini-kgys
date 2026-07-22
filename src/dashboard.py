from datetime import datetime
from pathlib import Path

from database import get_all_cameras
from monitoring import check_cameras
from events import get_last_events


def print_header():

    print()

    print("=" * 60)
    print("                 MINI-KGYS DASHBOARD")
    print("=" * 60)

    print(
        f"System Time    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print("Database       : CONNECTED")

    print()


def get_dashboard_summary(cameras):

    total = len(cameras)

    online = sum(
        1
        for camera in cameras
        if camera["status"] == "ONLINE"
    )

    offline = total - online

    return total, online, offline


def print_system_summary(total, online, offline):

    print(f"Total Cameras  : {total}")
    print(f"Online Cameras : {online}")
    print(f"Offline Cameras: {offline}")

    print("=" * 60)


def print_camera(camera):

    print("-" * 60)

    print(f"ID             : {camera['id']}")
    print(f"Name           : {camera['name']}")
    print(f"IP Address     : {camera['ip']}")
    print(f"Status         : {camera['status']}")

    if camera.get("last_ping") is not None:
        print(f"Last Ping      : {camera['last_ping']} ms")
    else:
        print("Last Ping      : N/A")

    if camera.get("last_http") is not None:
        print(f"Last HTTP      : {camera['last_http']} ms")
    else:
        print("Last HTTP      : N/A")

    if camera.get("last_check"):
        print(f"Last Check     : {camera['last_check']}")
    else:
        print("Last Check     : N/A")

    if camera.get("last_image"):

        image_name = Path(camera["last_image"]).name

        print(f"Last Image     : {image_name}")

    else:

        print("Last Image     : N/A")

    print("-" * 60)


def print_camera_list(cameras):

    if not cameras:

        print("\nNo camera found.\n")

        return

    print("\nCAMERA STATUS\n")

    for camera in cameras:

        print_camera(camera)


def print_event_history():

    events = get_last_events(limit=5)

    print()
    print("=" * 60)
    print("LAST EVENTS")
    print("=" * 60)

    if not events:

        print("No events found.")
        print()

        return

    for event in events:

        print("-" * 60)

        print(f"Time        : {event['event_time']}")
        print(f"Type        : {event['event_type']}")
        print(f"Description : {event['description']}")

    print("-" * 60)
    print()


def print_footer():

    print()


def refresh_dashboard():

    print()

    print("=" * 60)
    print("Updating camera status...")
    print("=" * 60)

    check_cameras()

    print()
    print("Loading dashboard...")
    print()


def show_dashboard():

    refresh_dashboard()

    cameras = get_all_cameras()

    total, online, offline = get_dashboard_summary(cameras)

    print_header()

    print_system_summary(
        total,
        online,
        offline
    )

    print_camera_list(cameras)

    print_event_history()

    print_footer()