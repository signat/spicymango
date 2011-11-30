#########################################################################
#
# Output file for SpicyMango
# Author: Chris Centore
#
# Description: Defines functions for each output module.
#
# SpicyMango written by: Chris Centore, Steve Swann, Jason Gunnoe
# Website: http://code.google.com/p/spicymango/
# Download: svn co http://spicymango.googlecode.com/svn/trunk/ spicymango/
#
#########################################################################

import os
from core import *

# Write output to a file specified in the config.
def send_output(mod_name,data):
	output_file_enable = check_config("OUTPUT_FILE")
        if output_file_enable == "ON":
		path = check_config("OUTPUT_FILE_NAME=")
		if not os.path.isfile(path):
                	outputfile = file(path, "w")
		else:
			outputfile = file(path, "a")
                
		outputfile.write(mod_name + ": " + data + "\n")
        	outputfile.close()
	#put other output conditions before else
	else:
		print mod_name + ": " + data
