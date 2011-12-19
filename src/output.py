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

import os,sys
from core import *

class Output(object):
	#Define all attributes for module output
        modname = None
        msg = None
	
	#Method to send output to various enabled destinations
        def send_output(self):
		#Method function for writing to a file
                def to_File():
                        path = check_config("OUTPUT_FILE_NAME=")
                	if not os.path.isfile(path):
                        	outputfile = file(path, "w")
                	else:
                       		outputfile = file(path, "a")

                	outputfile.write(self.modname + ": " + self.msg + "\n")
                	outputfile.close()

                
		#Check config and send output where enabled, but first make sure required attributes are set.
		if self.modname is None:
			print_error("Output", "modname attribute must be defined in instance")
		
		file_enable = check_config("OUTPUT_FILE")
        	if file_enable == "ON":
			to_File()
		
		#If no output destinations are defined in config, send output to console
		else:
			print self.modname + ": " + self.msg
