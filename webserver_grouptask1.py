from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import network
import socket
import dht
import neopixel

# Wi-Fi configuration (Access Point mode)
AP_SSID = "ESP32-S3_AP"
AP_PASSWORD = "12345678"

# OLED size
WIDTH = 128
HEIGHT = 64

# I2C setup (using GPIO 9 for SDA and 8 for SCL)
i2c = I2C(0, scl=Pin(9), sda=Pin(8))

# Initialize OLED
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.text('Starting AP...', 0, 0)
oled.show()

# Set up ESP32 in AP mode
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=AP_SSID, password=AP_PASSWORD)

print('Starting Access Point...')
while not ap.active():
    pass

print('AP Started. IP:', ap.ifconfig()[0])
oled.fill(0)
oled.text('AP Mode Active', 0, 0)
oled.text(f'IP: {ap.ifconfig()[0]}', 0, 10)
oled.show()

# DHT11 sensor setup (GPIO 4)
dht_sensor = dht.DHT11(Pin(4))

# Neopixel setup for RGB LED (GPIO 48)
np = neopixel.NeoPixel(Pin(48), 1)
