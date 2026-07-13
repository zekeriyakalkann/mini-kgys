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
		print(f"Isim: {camera['name']}")
		print(f"IP: {camera['ip']}")
		print(f"Durum: {camera['status']}")
