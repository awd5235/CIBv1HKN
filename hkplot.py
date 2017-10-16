"""
Adam Dykhouse
9/18/17

This program defines a command line protocol for plotting data from a text file.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as dts
import datetime
#import numpy as np
import argparse
#import os.path

# Function to check if the argument is a valid filename
'''def is_valid_file(parser, filename):
    if not os.path.exists(filename):
        parser.error("The file %s does not exist!" % filename)
    else:
        fin = open(filename,'r')
        return fin  # return an open file handle
'''

# Initialize Parser 
parser = argparse.ArgumentParser(description = 'Plot the user specified parameter with respect to time. The value of the parameter is found in the text file, also specified by the user.')

# Define required arguments
parser.add_argument('filename', help="text file containing numeric values to plot", metavar="FILE", type=argparse.FileType('r')) #type=lambda x: is_valid_file(parser, x)

# Define optional arguments
# Create mutually exclusive group for voltage/temperature parameter so only
#   one parameter can be plot at a time. 
group = parser.add_mutually_exclusive_group()
group.add_argument('-vs','--vsub', action = 'store_true', help = 'plot vsub with respect to time')
group.add_argument('-vda','--vdda', action = 'store_true', help = 'plot vdda with respect to time')
group.add_argument('-3p3','--vdd3p3', action = 'store_true', help = 'plot vdd3p3 with respect to time')
group.add_argument('-2p5','--vdd2p5', action = 'store_true', help = 'plot vdd2p5 with respect to time')
group.add_argument('-vio','--vddio', action = 'store_true', help = 'plot vddio with respect to time')
group.add_argument('-t2','--tsense2', action = 'store_true', help = 'plot tsense2 with respect to time')
group.add_argument('-t','--tsense', action = 'store_true', help = 'plot tsense with respect to time')
group.add_argument('-t0','--tsense0', action = 'store_true', help = 'plot tsense0 with respect to time')
group.add_argument('-f','--fheart', action = 'store_true', help = 'plot fheart with respect to time')

# Retrieve arguments from user input
args = parser.parse_args()

with args.filename as fin:
    # Extract times from text file for later plotting
    for line in fin:
        timestr = line.split(' ')[1]
    
    time_obj = datetime.datetime.strptime(timestr,'%H:%M:%S.%f')
    time = dts.date2num(time_obj)
    
    # Check each optional argument and if true, plot the specified option with respect to time.
    if args.vsub:
        for line in fin:
            vsub = float(line.split(' ')[2])
            plt.plot_date(time,vsub)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()

    elif args.vdda:
        for line in fin:
            vdda = float(line.split(' ')[3])
            plt.plot_date(time,vdda)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
    elif args.vdd3p3:
        for line in fin:
            vdd3p3 = float(line.split(' ')[4])
            plt.plot_date(time,vdd3p3)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
    elif args.vdd2p5:
        for line in fin:
            vdd2p5 = float(line.split(' ')[5])
            plt.plot_date(time,vdd2p5)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
    elif args.vddio:
        for line in fin:
            vddio = float(line.split(' ')[6])
            plt.plot_date(time,vddio)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
    elif args.tsense2:
        for line in fin:
            tsense2 = float(line.split(' ')[7])
            plt.plot_date(time,tsense2)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
    elif args.tsense:
        for line in fin:
            tsense = float(line.split(' ')[8])
            plt.plot_date(time,tsense)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()

    elif args.tsense0:
        for line in fin:
            tsense0 = float(line.split(' ')[9])
            plt.plot_date(time,tsense0)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
    elif args.fheart:
        for line in fin:
            fheart = float(line.split(' ')[10])
            plt.plot_date(time,fheart)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
 
# Else no optional argument specified, proceed to plot each parameter individually with respect to time.
#   Display only one plot at a time by waiting for a keypress between each plot       
    else:
        for line in fin:
            vsub = float(line.split(' ')[2])
            plt.plot(time,vsub)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
        for line in fin:
            vdda = float(line.split(' ')[3])
            plt.plot(time,vdda)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
        for line in fin:
            vdd3p3 = float(line.split(' ')[4])
            plt.plot(time,vdd3p3)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
       
        for line in fin:
            vdd2p5 = float(line.split(' ')[5])
            plt.plot(time,vdd2p5)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
  
        for line in fin:
            vddio = float(line.split(' ')[6])
            plt.plot(time,vddio)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
        for line in fin:
            tsense2 = float(line.split(' ')[7])
            plt.plot(time,tsense2)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
        for line in fin:
            tsense = float(line.split(' ')[8])
            plt.plot(time,tsense)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
        for line in fin:
            tsense0 = float(line.split(' ')[9])
            plt.plot(time,tsense0)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
        
        for line in fin:
            fheart = float(line.split(' ')[10])
            plt.plot(time,fheart)
            plt.show()
            plt.waitforbuttonpress()
            plt.close()
            
        fin.close()