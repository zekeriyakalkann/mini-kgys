# ESP32-CAM Firmware

This firmware is developed for the Mini-KGYS project.

## Hardware

- AI Thinker ESP32-CAM
- OV2640 Camera Module

## Features

- Wi-Fi Connection
- REST API
- Camera Initialization
- Health Check Endpoint
- Camera Information Endpoint
- Image Capture Endpoint

## REST API

### Health Check

GET

```
/health
```

Response

```
OK
```

---

### Camera Information

GET

```
/info
```

Returns camera information.

---

### Capture Image

GET

```
/capture
```

Returns a JPEG image.

---

## Project Files

```
mini_kgys_camera.ino
api_server.cpp
camera_manager.cpp
wifi_manager.cpp
config.cpp
```

## Status

Current Version: v0.3.0

Firmware Status

- WiFi ✔
- REST API ✔
- Image Capture ✔
- HTTP Server ✔
