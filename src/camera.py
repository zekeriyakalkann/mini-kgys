from database import get_all_cameras


def list_cameras():

    cameras = get_all_cameras()

    for camera in cameras:

        print(f"\nID: {camera['id']}")
        print(f"İsim: {camera['name']}")
        print(f"IP: {camera['ip']}")
        print(f"Durum: {camera['status']}")


def get_camera_count():

    cameras = get_all_cameras()

    return len(cameras)