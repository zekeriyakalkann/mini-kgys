#include <WiFi.h>
#include <WebServer.h>
#include "esp_camera.h"
#include "wifi_manager.h"
#include "config.h"
#include "board_config.h"
#include "api_server.h"
#include "camera_manager.h"

void setup()
{
    Serial.begin(115200);
    delay(1000);

    connectWiFi();

    initCamera();

    startServer();

    startEspHttpServer();

    testCapture();
}



void loop()
{
    handleServer();
}