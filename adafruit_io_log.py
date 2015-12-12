#!/usr/bin/python
from Adafruit_IO import Client
from sense_hat import SenseHat
import time
from time import sleep

ADAFRUIT_IO_KEY = ‘Insert you secret key’
aio = Client(ADAFRUIT_IO_KEY)

sense = SenseHat()
sense.low_light = True

response = 1 # Variable to check for connection status

# Warning display on LED Matrix
x = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

temp_warn = [
O, x, x, x, x, x, x, O,
O, x, x, x, x, x, x, O,
O, O, O, x, x, O, O, O,
O, O, O, x, x, O, O, O,
O, O, O, x, x, O, O, O,
O, O, O, x, x, O, O, O,
O, O, O, x, x, O, O, O,
O, O, O, x, x, O, O, O
]

hum_warn = [
O, x, x, O, O, x, x, O,
O, x, x, O, O, x, x, O,
O, x, x, O, O, x, x, O,
O, x, x, x, x, x, x, O,
O, x, x, x, x, x, x, O,
O, x, x, O, O, x, x, O,
O, x, x, O, O, x, x, O,
O, x, x, O, O, x, x, O
]

pres_warn = [
O, x, x, x, x, x, x, O,
O, x, x, O, O, x, x, O,
O, x, x, O, O, x, x, O,
O, x, x, O, O, x, x, O,
O, x, x, x, x, x, x, O,
O, x, x, O, O, O, O, O,
O, x, x, O, O, O, O, O,
O, x, x, O, O, O, O, O
]

# Adafruit IO: Temperature feed is 'temperature'
# Adafruit IO: Pressure feed is 'pressure'
# Adafruit IO: Humidity feed is 'humidity'
# Adafruit IO: Notification text box is 'notification'

while True:

# Get data from environmental sensors. Sensor data is of type float.
   temperature = sense.get_temperature()
   humidity = sense.get_humidity()
   pressure = sense.get_pressure()
   temperature = round(temperature, 1)
   humidity = round(humidity, 1)
   pressure = round(pressure, 1)
   
# Send sensor data to Adafruit IO.
   aio.send('temperature', temperature) # in deg C
   aio.send('humidity', humidity) # in %rH
   aio.send('pressure', pressure) # in millibar

# Conditions for warnings
   if temperature > 30: #30 deg C
      aio.send('notification', 'Temperature alert')
      sense.set_pixels(temp_warn)

   if humidity > 80: #80% rH
      aio.send('notification', 'Humidity alert')
      sense.set_pixels(hum_warn)

   if pressure < 900: #900 millibar
      aio.send('notification', 'Pressure alert')
      sense.set_pixels(pres_warn)

# Condition for no warning
   if (temperature <= 30 and humidity <= 80 and pressure >= 900):
      aio.send('notification', 'All ok!')
      sense.clear()
