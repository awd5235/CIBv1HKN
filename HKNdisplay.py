"""
Adam Dykhouse
9/6/17

CIBv1HKN
This program is used to read, interpret, and display data taken from the CIB by
an Arduino Nano. The Nano converts all CIB signals to digital numbers and
transfers those raw numbers to this program via serial USB (ASCII).
"""

import serial # Make use of serial library

# Initialize USB serial communication to Arduino
arduino = serial.Serial('/dev/cu.usbserial-A105OHGP', 9600, timeout=10)


while True:
	data = arduino.readline()[:-1] #the last bit gets rid of the new-line char
        if data:
            print data