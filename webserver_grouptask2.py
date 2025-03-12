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

# HTML page with Wi-Fi connect form
html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESP32-S3 Control Panel</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Poppins', sans-serif;
            background: #0f172a;
            color: #f8fafc;
            text-align: center;
            padding: 30px;
        }
        h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 2rem;
            font-weight: 500;
            margin: 30px 0 15px;
        }
        button {
            padding: 12px 25px;
            font-size: 1.2rem;
            font-weight: 500;
            background: linear-gradient(135deg, #00d4ff, #0072ff);
            color: #fff;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        button:hover {
            transform: scale(1.05);
            background: linear-gradient(135deg, #0072ff, #00d4ff);
        }
        form {
            background: #1e293b;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            max-width: 500px;
            margin: 0 auto;
        }
        label {
            display: block;
            font-size: 1.2rem;
            margin-bottom: 8px;
        }
        input, select {
            width: 100%;
            padding: 12px;
            font-size: 1.1rem;
            margin-bottom: 15px;
            border: none;
            border-radius: 8px;
            background: #334155;
            color: #f8fafc;
        }
        table {
            width: 100%;
            margin: 20px 0;
            border-collapse: collapse;
            background: #1e293b;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        }
        th, td {
            padding: 15px;
            text-align: left;
            font-size: 1.1rem;
        }
        th {
            background: #00d4ff;
            color: #0f172a;
        }
        tr:nth-child(even) {
            background: #334155;
        }
        #status {
            font-size: 1.4rem;
            margin-top: 20px;
            font-weight: 500;
            color: #00d4ff;
        }
    </style>
</head>