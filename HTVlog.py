# Log humidity, temperature, and pressure values in a .csv file
# Change path for the file as required in line 9 and line 11
# Place HTVlog.sh in crontab to run at startup. Change path to HTVlog.py file as required.

import os
import time
from time import sleep
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

file = open("/home/pi/Programs/log/HTVlog.csv", "a")

if os.stat("/home/pi/Programs/log/HTVlog.csv").st_size == 0:
	file.write("Date,Time,Humidity,Temperature,Pressure\n")

while True:
	hum = sense.get_humidity()
	temp = sense.get_temperature()
	pres = sense.get_pressure()
	
	hum = round(hum, 2)
	temp = round(temp, 2)
	pres = round(pres, 2)

	date = time.strftime("%Y-%m-%d")
        log_time = time.strftime("%H:%M:%S")
	file.write(str(date)+","+str(log_time)+","+str(hum)+","+str(temp)+","+str(pres)+"/n")
	file.flush()
	time.sleep(5)
file.close()
