from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import network
import socket
import json

# OLED setup
WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.text('Starting AP...', 0, 0)
oled.show()

# AP mode setup
AP_SSID = "ESP32-S3_AP"
AP_PASSWORD = "12345678"
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=AP_SSID, password=AP_PASSWORD)

while not ap.active():
    pass

ip = ap.ifconfig()[0]
print('AP Started. IP:', ip)
oled.fill(0)
oled.text('AP Mode Active', 0, 0)
oled.text(f'IP: {ip}', 0, 10)
oled.show()