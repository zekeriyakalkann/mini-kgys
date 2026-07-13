# Sistemde kayıtlı kameralar

cameras = [
    {
        "id": 1,
        "name": "ESP32-CAM-01",
        "ip": "192.168.1.101",
        "status": "UNKNOWN"
    }
]


def list_cameras():
    for camera in cameras:
        print(f"\nID: {camera['id']}")
        print(f"İsim: {camera['name']}")
        print(f"IP: {camera['ip']}")
        print(f"Durum: {camera['status']}")


def get_camera_count():
    return len(cameras)