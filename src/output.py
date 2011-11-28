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
def output_file(data):
	path = check_config("OUTPUT_FILE_NAME=")
	if not os.path.isfile(path):
                outputfile = file(path, "w")
                outputfile.write(data + "\n")
                outputfile.close()
	else:
		outputfile = file(path, "a")
                outputfile.write(data + "\n")
                outputfile.close()
