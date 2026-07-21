#include "api_server.h"
#include <WiFi.h>
#include "config.h"
#include "camera_manager.h"

httpd_handle_t espServer = NULL;

WebServer server(80);

static esp_err_t healthHandler(httpd_req_t *req)
{
    const char *response = "OK";

    httpd_resp_set_type(req, "text/plain");

    httpd_resp_send(
        req,
        response,
        HTTPD_RESP_USE_STRLEN
    );

    return ESP_OK;
}

static esp_err_t captureHandler(httpd_req_t *req)
{
    if (!isCameraReady())
    {
        httpd_resp_send_err(
            req,
            HTTPD_500_INTERNAL_SERVER_ERROR,
            "Camera Not Ready"
        );

        return ESP_FAIL;
    }

    camera_fb_t *fb = captureFrame();

    if (fb == nullptr)
    {
        httpd_resp_send_err(
            req,
            HTTPD_500_INTERNAL_SERVER_ERROR,
            "Capture Failed"
        );

        return ESP_FAIL;
    }

    Serial.println();
    Serial.println("========== CAPTURE ==========");

    Serial.print("Width  : ");
    Serial.println(fb->width);

    Serial.print("Height : ");
    Serial.println(fb->height);

    Serial.print("Length : ");
    Serial.print(fb->len);

    Serial.println(" bytes");

    Serial.println("=============================");

    httpd_resp_set_type(req, "image/jpeg");

    esp_err_t result = httpd_resp_send(
        req,
        (const char *)fb->buf, 
        fb->len
    );

    releaseFrame(fb);

    return result;
}

httpd_uri_t healthUri =
{
    .uri = "/health",

    .method = HTTP_GET,

    .handler = healthHandler,

    .user_ctx = NULL
};

httpd_uri_t captureUri =
{
    .uri = "/capture",

    .method = HTTP_GET,

    .handler = captureHandler,

    .user_ctx = NULL
};

void handleHealth()
{
    server.send(200, "text/plain", "OK");
}

void handleInfo()
{
    String json = "{";

    json += "\"device\":\"";
    json += DEVICE_NAME;
    json += "\",";

    json += "\"firmware\":\"";
    json += FIRMWARE_VERSION;
    json += "\",";

    json += "\"ip\":\"";
    json += WiFi.localIP().toString();
    json += "\",";

    json += "\"status\":\"ONLINE\"";

    json += "}";

    server.send(200, "application/json", json);
}

void startServer()
{
    server.on("/health", handleHealth);

    server.on("/info", handleInfo);

    server.begin();

    Serial.println("HTTP Server Started");
}

void handleServer()
{
    server.handleClient();
}

void startEspHttpServer()
{
    httpd_config_t config = HTTPD_DEFAULT_CONFIG();

    config.server_port = 8080;

    esp_err_t result = httpd_start(&espServer, &config);

    if(result == ESP_OK)
    {
        httpd_register_uri_handler(
            espServer,
            &healthUri
        );

        httpd_register_uri_handler(
            espServer,
            &captureUri
        );

        Serial.println("ESP HTTP Server Started");
    }

    else
    {
        Serial.println("ESP HTTP Server Failed");
    }
}