import wifi
import socketpool
import adafruit_requests
import ssl
import os

print("Connect Wifi")
# setup wifi credentials in .env file
wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))
print("Connected!")

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
url = "https://www.adafruit.com/api/quotes.php"

response = requests.get(url)
print(response.text)
response.close()