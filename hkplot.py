"""
Adam Dykhouse
9/18/17

This program defines a command line protocol for plotting data from a text file.
"""

import matplotlib.pyplot as plt
import numpy as np
import argparse

# Initialize Parser 
parser = argparse.ArgumentParser(description = 'Plot the user specified parameter with respect to time. The value of the parameter is found in the text file, also specified by the user.')

# Create mutually exclusive group for voltage/temperature parameter so only
#   one parameter can be plot at a time. 
group = parser.add_mutually_exclusive_group()

# Define All Potential Arguments
group.add_argument('vsub', action = 'store_true', help = 'plot vsub with respect to time')
group.add_argument('vdda', action = 'store_true', help = 'plot vdda with respect to time')
group.add_argument('vdd3p3', action = 'store_true', help = 'plot vdd3p3 with respect to time')
group.add_argument('vdd2p5', action = 'store_true', help = 'plot vdd2p5 with respect to time')
group.add_argument('vddio', action = 'store_true', help = 'plot vddio with respect to time')
group.add_argument('tsense2', action = 'store_true', help = 'plot tsense2 with respect to time')
group.add_argument('tsense', action = 'store_true', help = 'plot tsense with respect to time')
group.add_argument('tsense0', action = 'store_true', help = 'plot tsense0 with respect to time')
group.add_argument('fheart', action = 'store_true', help = 'plot fheart with respect to time')
