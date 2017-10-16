"""
Adam Dykhouse
9/6/17

CIBv1HKN
This program is used to read, interpret, and display data taken from the CIB by
an Arduino Nano. The Nano converts all CIB signals to digital numbers and
transfers those raw numbers to this program via serial USB (ASCII).
"""

import signal
import sys
import serial # Library allowing serial communication
import datetime # Library allowing time stamp functionality
#import num.py as np
#import matplotlib.pyplot as plt # Library allowing plotting functionality

# Write functions to convert each Arduino DAC output (string) to a physical value (float)
def d2p_vsub(x):
    return (float(x)*5)/1024

def d2p_vdda(x):
    return (float(x)*5)/1024

def d2p_vdd3p3(x):
    return (float(x)*5)/1024

def d2p_vdd2p5(x):
    return (float(x)*5)/1024

def d2p_vddio(x):
    return (float(x)*5)/1024

def d2p_tsense2(x):
    return (((float(x)*5)/1024)-0.5)*100

def d2p_tsense(x):
    return (((float(x)*5)/1024)-0.5)*100

def d2p_tsense0(x):
    return (((float(x)*5)/1024)-0.5)*100

def d2p_fheart(x):
    return int(x)

# When control+c is entered, end program
def signal_handler(signal, frame):
    file.close()
    sys.exit(0)

# Initialize Interrupt
signal.signal(signal.SIGINT, signal_handler)

# Initialize USB serial communication to Arduino
arduino = serial.Serial('/dev/cu.usbserial-A105OHGP', 9600, timeout=10)

# Initialize text file to write
file = open('cib_hkn_{:%m-%d-%Y-%H-%M-%S}.txt'.format(datetime.datetime.now()),'w+')

# Print header to console (':'=modifier, '>'=justify right, '>'=justify left) 
print'{:27} {:>5}  {:>4}  {:>6}  {:>6}  {:>5}  {:>7}  {:>6}  {:>7}  {:>6}'.format(' ','VSUB','VDDA','VDD3P3','VDD2P5','VDDIO','TSENSE2','TSENSE','TSENSE0','FHEART')

# print header to text file
file.write('{:27} {:>5}  {:>4}  {:>6}  {:>6}  {:>5}  {:>7}  {:>6}  {:>7}  {:>6}\n'.format(' ','VSUB','VDDA','VDD3P3','VDD2P5','VDDIO','TSENSE2','TSENSE','TSENSE0','FHEART'))

# Continuously loop
while True:
    data = arduino.readline()[:-1] # Read in single lines of raw data from Arduino Serial and remove "\n".
    rawData = data.split()    # split single line of raw data at whitespace and insert values into array
    
    # If list, rawData, is full, convert each DAC output parameter (string) to a physical numerical quantity
    if len(rawData) == 9:
        VSUB = d2p_vsub(rawData[0])
        VDDA = d2p_vdda(rawData[1]) 
        VDD3P3 = d2p_vdd3p3(rawData[2])
        VDD2P5 = d2p_vdd2p5(rawData[3])
        VDDIO = d2p_vddio(rawData[4])
        TSENSE2 = d2p_tsense2(rawData[5])
        TSENSE = d2p_tsense(rawData[6])
        TSENSE0 = d2p_tsense0(rawData[7])
        FHEART = d2p_fheart(rawData[8])
        
        # Print actual values to the console with time stamp
        print '{}  {:>5.2f}  {:>4.2f}  {:>6.2f}  {:>6.2f}  {:>5.2f}  {:>7.2f}  {:>6.2f}  {:>7.2f}  {:>6d}'.format(datetime.datetime.now(),VSUB,VDDA,VDD3P3,VDD2P5,VDDIO,TSENSE2,TSENSE,TSENSE0,FHEART)
    
        # Write a line to the text file
        file.write('{}  {:>5.2f}  {:>4.2f}  {:>6.2f}  {:>6.2f}  {:>5.2f}  {:>7.2f}  {:>6.2f}  {:>7.2f}  {:>6d}\n'.format(datetime.datetime.now(),VSUB,VDDA,VDD3P3,VDD2P5,VDDIO,TSENSE2,TSENSE,TSENSE0,FHEART))
        
    # Otherwise, rawData is not a full line, skip until sensible data is read from Serial
