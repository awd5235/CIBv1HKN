import matplotlib.pyplot as plt
import matplotlib.dates as dts
import datetime
import argparse


# Wrapper function to handle plotting
def paramPlot(time,param,ylabel):
    plt.plot(time,param)
    plt.xlabel('Time (Fractional Days)')
    plt.ylabel(ylabel)
    plt.show()
    plt.waitforbuttonpress()
    plt.close()
    return

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
 
# Get filename   
fin = args.filename

# Extract times from text file for later plotting
timestr = []
for line in fin:
    timestr.append(line.split()[1])
timestr.pop(0)      # Remove element from first header row
fin.seek(0)         # Reset pointer to beginning of file
    
# Convert from list of strings to list of times
time_obj = []       # use time objects as intermediary step
for i in range(0,len(timestr)):
    time_obj.append(datetime.datetime.strptime(timestr[i],'%H:%M:%S.%f'))
time = dts.date2num(time_obj)
    
# Check each optional argument and if true, plot the specified option with respect to time.
if args.vsub:
    vs_str = []                             # Initialize string list
    for line in fin:
        vs_str.append(line.split()[2])      # Add each subsequent string value to list
    vs_str.pop(0)                           # Remove initial header string value
    vs = [float(i) for i in vs_str]         # Convert values from string to float
    paramPlot(time,vs,'VSUB (V)')           # Plot with respect to time
    
elif args.vdda:
    vda_str = []                            # Initialize string list
    for line in fin:
        vda_str.append(line.split()[3])     # Add each subsequent string value to list
    vda_str.pop(0)                          # Remove initial header string value
    vda = [float(i) for i in vda_str]       # Convert values from string to float
    paramPlot(time,vda,'VDDA (V)')          # Plot with respect to time

elif args.vdd3p3:
    v3p3_str = []                           # Initialize string list
    for line in fin:
        v3p3_str.append(line.split()[4])    # Add each subsequent string value to list    
    v3p3_str.pop(0)                         # Remove initial header string value
    v3p3 = [float(i) for i in v3p3_str]     # Convert values from string to float
    paramPlot(time,v3p3,'VDD3P3 (V)')       # Plot with respect to time
    
elif args.vdd2p5:
    v2p5_str = []                           # Initialize string list
    for line in fin:
        v2p5_str.append(line.split()[5])    # Add each subsequent string value to list
    v2p5_str.pop(0)                         # Remove initial header string value
    v2p5 = [float(i) for i in v2p5_str]     # Convert values from string to float
    paramPlot(time,v2p5,'VDD2P5 (V)')       # Plot with respect to time
    
elif args.vddio:
    vio_str = []                            # Initialize string list
    for line in fin:
        vio_str.append(line.split()[6])     # Add each subsequent string value to list
    vio_str.pop(0)                          # Remove initial header string value
    vio = [float(i) for i in vio_str]       # Convert values from string to float
    paramPlot(time,vio,'VDDIO (V)')         # Plot with respect to time
    
elif args.tsense2:
    t2_str = []                             # Initialize string list
    for line in fin:
        t2_str.append(line.split()[7])      # Add each subsequent string value to list
    t2_str.pop(0)                           # Remove initial header string value
    t2 = [float(i) for i in t2_str]         # Convert values from string to float
    paramPlot(time,t2,'Tsense2 (C)')        # Plot with respect to time
    
elif args.tsense:
    t_str = []                              # Initialize string list
    for line in fin:
        t_str.append(line.split()[8])       # Add each subsequent string value to list
    t_str.pop(0)                            # Remove initial header string value
    t = [float(i) for i in t_str]           # Convert values from string to float
    paramPlot(time,t,'Tsense (C)')          # Plot with respect to time
    
elif args.tsense0:
    t0_str = []                             # Initialize string list
    for line in fin:
        t0_str.append(line.split()[9])      # Add each subsequent string value to list
    t0_str.pop(0)                           # Remove initial header string value
    t0 = [float(i) for i in t0_str]         # Convert values from string to float
    paramPlot(time,t0,'Tsense0 (C)')        # Plot with respect to time
    
elif args.fheart:
    fheart_str = []                         # Initialize string list
    for line in fin:
        fheart_str.append(line.split()[10]) # Add each subsequent string value to list
    fheart_str.pop(0)                       # Remove initial header string value
    fheart = [float(i) for i in fheart_str] # Convert values from string to float
    paramPlot(time,fheart,'FHEART')         # Plot with respect to time

    
fin.close()   