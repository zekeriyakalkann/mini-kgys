#include <WiFi.h>

#include "config.h"
#include "wifi_manager.h"

void connectWiFi()
{
    Serial.println();
    Serial.println("==============================");
    Serial.println("Mini-KGYS Camera Boot");
    Serial.println("==============================");

    Serial.print("SSID     : ");
    Serial.println(WIFI_SSID);

    Serial.print("PASSWORD : ");
    Serial.println(WIFI_PASSWORD);

    WiFi.mode(WIFI_STA);
    WiFi.disconnect(true, true);
    delay(1000);

    WiFi.begin(
        WIFI_SSID,
        WIFI_PASSWORD
    );

    Serial.print("WiFi Connecting");

    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");

        Serial.print(" Status = ");
        Serial.println(WiFi.status());

        delay(1000);
    }

    Serial.println();
    Serial.println("Connected");

    Serial.print("IP Address : ");

    Serial.println(WiFi.localIP());
}