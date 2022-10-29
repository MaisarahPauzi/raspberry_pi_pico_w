import wifi
import socketpool
import adafruit_requests
import ssl
import os
from adafruit_httpserver import HTTPServer, HTTPResponse
import digitalio
import board

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("Connect Wifi")
wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))
print("Connected!")

print("IP ADDR:", str(wifi.radio.ipv4_address))

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)

@server.route("/")
def base(request):  
    """Default reponse is /index.html"""
    return HTTPResponse(filename="/index.html")

@server.route("/on")
def on(request):  
    led.value = True
    return HTTPResponse(body=f"on")

@server.route("/off")
def off(request):  
    led.value = False
    return HTTPResponse(body=f"off")

# Never returns
server.serve_forever(str(wifi.radio.ipv4_address))