#ifndef CAMERA_MANAGER_H
#define CAMERA_MANAGER_H

#include "esp_camera.h"

void initCamera();

camera_fb_t* captureFrame();

void releaseFrame(camera_fb_t *fb);

bool isCameraReady();

void testCapture();

#endif