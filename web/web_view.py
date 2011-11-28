#########################################################################
#
# Web View Module for SpicyMango
# Author: Chris Centore
#
# Description: (Experimental) The Web View is the intitial stages of a web
#	       GUI for SpicyMango. Right now, it simply shows output sent to
#	       to an output file in reverse order from most recent to last.
#
# SpicyMango written by: Chris Centore, Steve Swann, Jason Gunnoe
# Website: http://code.google.com/p/spicymango/
# Download: svn co http://spicymango.googlecode.com/svn/trunk/ spicymango/
#
#########################################################################

import thread,sys
sys.path.append("..")
from src.bottle import route, run, template
from src.core import *

def main():
	#Get config options
	ip = check_config("WEB_VIEW_IP=")
	port = check_config("WEB_VIEW_PORT=")
	outfile = check_config("OUTPUT_FILE_NAME=")

	#Route for the webroot
	@route('/')
	def mainview():
		filelines = reversed(open(outfile).readlines())
    		display_output = template('base', lines=filelines)
		return display_output

	# Run Web View webserver on specified ip and port
	print "[!] Connect to http://%s:%s" % (ip, port)
	run(port=port, host=ip, quiet="True")

#If the output file option is not set in the config, don't run.
check_output = check_config("OUTPUT_FILE=")
if check_output == 'ON':
	print "[!] Starting Web View..."
	thread.start_new_thread(main, ())
else:
	print "[!] Web View will not start: No output configured."
