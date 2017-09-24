#main file to run the program and upload data into Thingspeak


import RPi.GPIO as GPIO
import dht11
import time
import datetime

import thingspeak
channel_id = 327635 #
write_key_id= "997BZAO2O7MMQBZQ" #

channel = thingspeak.Channel(id=channel_id, write_key=write_key_id)

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=4)

while True:
	result = instance.read()
	try:
		if result.is_valid():
			response = channel.update({1:result.temperature, 2:result.humidity})
			pt_str = "Last valid input: " + str(datetime.datetime.now()) + "  Temperature: %d C" % result.temperature + "  Humidity: %d %%" % result.humidity
			if response != 0:
				print (pt_str)

	except:
		print ("Connection failed")	
		
	time.sleep(10)
		
		
#while True:
#    result = instance.read()
	
#		if result.is_valid():
#			pt_str = "Last valid input: " + str(datetime.datetime.now()) + "  Temperature: %d C" % result.temperature + "  Humidity: %d %%" % result.humidity
#			response = channel.update({1:result.temperature, 2:result.humidity}) 
#			#print("Last valid input: " + str(datetime.datetime.now()))
#			#print("Temperature: %d C" % result.temperature)
#			#print("Humidity: %d %%" % result.humidity)
#			if response <> 0:
#				print(pt_str)

#   time.sleep(1)
