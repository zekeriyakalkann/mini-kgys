#ifndef API_SERVER_H
#define API_SERVER_H

#include "esp_http_server.h"
#include <WebServer.h>

extern WebServer server;

void startServer();
void handleServer();

void startEspHttpServer();

#endif