#include <string.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/event_groups.h"
#include "esp_system.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "esp_log.h"
#include <arpa/inet.h>
#include <string.h>

#include "lwip/err.h"
#include "lwip/sockets.h"
#include "lwip/sys.h"
#include "lwip/netdb.h"
#include "lwip/dns.h"

#define WIFI_TAG "WIFI"

/** SERVER UDP **/
#define UDP_HOST 0x0104A8C0
#define UDP_PORT 5001

/** SERVER TCP **/
#define TCP_HOST 0x0104A8C0
#define TCP_PORT 5001

/** DEFINES **/
#define WIFI_SUCCESS 1 << 0
#define WIFI_FAILURE 1 << 1
#define UDP_SUCCESS 1 << 0
#define UDP_FAILURE 1 << 1
#define TCP_SUCCESS 1 << 0
#define TCP_FAILURE 1 << 1
#define MAX_FAILURES 10

void wifi_event_handler(void *arg, esp_event_base_t event_base, int32_t event_id, void *event_data);
void ip_event_handler(void *arg, esp_event_base_t event_base, int32_t event_id, void *event_data);

esp_err_t connect_wifi();
esp_err_t connect_UDP_server();
esp_err_t connect_TCP_server();