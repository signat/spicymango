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
from src.bottle import route, run, template, static_file
from src.core import *

execfile('src/getname')

def main():
	#Get config options
	ip = check_config("WEB_VIEW_IP=")
	port = check_config("WEB_VIEW_PORT=")
	outfile = check_config("OUTPUT_FILE_NAME=")

	#Route for the webroot
	@route('/')
	def mainview():
		display_main = template('base')
		return display_main
	
	@route('/get_data_table')
	def data_table_view():
                filelines = reversed(open(outfile).readlines())
                display_datatable = template('get_data', lines=filelines)
                return display_datatable

	@route('/images/:filename#.*\.png#')
	def send_image(filename):
    		return static_file(filename, root='web/images/', mimetype='image/png')

	@route('/css/:filename#.*\.css#')
        def send_image(filename):
                return static_file(filename, root='web/css/')

	@route('/js/:filename#.*\.js#')
        def send_image(filename):
                return static_file(filename, root='web/js/')

	# Run Web View webserver on specified ip and port
	print_status(module,"Connect to http://%s:%s" % (ip, port))
	run(port=port, host=ip, quiet="True")

#If the output file option is not set in the config, don't run.
check_output = check_config("OUTPUT_FILE=")
if check_output == 'ON':
	print_status(module,"loading...")
	thread.start_new_thread(main, ())
else:
	print_error(module,"Cannot start, no output configured.")
