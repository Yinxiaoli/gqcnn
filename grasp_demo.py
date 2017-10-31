''' 
A python script to run grasp demo.

Each time, a grasp.txt file will be saved in the save location.
The previous grasp.txt, if any, will be removed first.
'''

import os


# Remove grasp.txt file if any.
filename='grasp.txt'

try:
    os.remove(filename)
except OSError:
    pass

# Call the main function, which will generate the grasp.txt.
os.system('sudo python examples/policy.py --config_filename=cfg/examples/policy.yaml')

