#########################################################################
#
# Core file for SpicyMango
# Author: Chris Centore
#
# Description: Core functions for SpicyMango.
#
# SpicyMango written by: Chris Centore, Steve Swann, Jason Gunnoe
# Website: http://code.google.com/p/spicymango/
# Download: svn co http://spicymango.googlecode.com/svn/trunk/ spicymango/
#
#########################################################################

import os,re

# Get configuation options from the config file.
def check_config(param):
	path = os.path.join(os.path.dirname(__file__), '..', 'config')
        fileopen = file(path, "r")
        # iterate through lines in file
        for line in fileopen:
		if not re.search('#.', line):
                	match = re.search(param, line)
                	if match:
                        	line = line.rstrip()
                        	line = line.replace('"', "")
                        	line = line.split("=")
                        	return line[1]

# Get Keyword/Module pairs from the keywords file.
def get_keywords(param):
        path = os.path.join(os.path.dirname(__file__), '..', 'keywords')
        fileopen = file(path, "r")
	wordlist = []
        # iterate through lines in file
        for line in fileopen:
                if not re.search('#.', line):
                        match = re.search(param, line)
                        if match:
				wordlist.append(eval(line))
        return wordlist
