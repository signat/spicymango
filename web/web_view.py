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
from src.bottle import route, run, template, static_file, request, response, redirect, post
from src.core import *

#Read code to dynamically get name of this module.
execfile('src/getname')

def main():
	#Get config options
	ip = check_config("WEB_VIEW_IP=")
	port = check_config("WEB_VIEW_PORT=")
	
	#Route for the webroot
	@route('/')
	def mainview():
		display_main = template('base')
		if request.get_cookie("loggedin", secret='sm2345-45634'):
			return display_main
		else:
			redirect('/login')

	@route('/login')
	def login():
		return "<form action='/login-check' method='POST'>Username: <input type=text name=user><br>Password: <input type=text name=pass><br><input type=submit value=Enter></form>"
	
	@post('/login-check')
	def logincheck():
		if request.forms.get('user') == 'smadmin' and request.forms.get('pass') == 'sm1234':
                        response.set_cookie("loggedin", "Success", secret='sm2345-45634')
                        redirect('/')
		else:
			redirect('/login')

	#Route for the AJAX call to get data from a file
	@route('/get_data_table')
	def data_table_view():
		if check_config("WEB_VIEW_DATA_SRC=") == "FILE":
			outfile = check_config("OUTPUT_FILE_NAME=")
                	rowlines = reversed(open(outfile).readlines())
			display_datatable = template('get_data_FILE', lines=rowlines)
		elif check_config("WEB_VIEW_DATA_SRC=") == "SQLITE3":
			import sqlite3, os
			outdb = check_config("OUTPUT_SQLITE3_DB_PATH=")
			if not os.path.isfile(outdb):
				print_error(module, "DB File does not exist")
			else:
				if request.query.field:
					sqlquery = "SELECT * FROM spicymango WHERE " + request.query.field + " LIKE '%" + request.query.term + "%' ORDER BY id DESC LIMIT 50"
				else:
					sqlquery = "SELECT * FROM spicymango ORDER BY id DESC LIMIT 50"

				conn = sqlite3.connect(outdb)
				c = conn.cursor()
				c.execute(sqlquery)
				rowlines = c
			display_datatable = template('get_data_SQLITE3', lines=rowlines)
		else:
			print_error(module, "WEB_VIEW_DATA_SRC is not set or set incorrectly in the config file")
                
		if request.get_cookie("loggedin", secret='sm2345-45634'):
                        return display_datatable
                else:
                        redirect('/login')	

	#Route for png images
	@route('/images/:filename#.*\.png#')
	def send_image(filename):
    		return static_file(filename, root='web/images/', mimetype='image/png')

	#Route for style sheets
	@route('/css/:filename#.*\.css#')
        def send_image(filename):
                return static_file(filename, root='web/css/')

	#Route for javascript
	@route('/js/:filename#.*\.js#')
        def send_image(filename):
                return static_file(filename, root='web/js/')

	# Run Web View webserver on specified ip and port
	print_status(module,"Connect to http://%s:%s" % (ip, port))
	run(port=port, host=ip, quiet="True")

#If the output file option is not set in the config, don't run.
check_outputfile = check_config("OUTPUT_FILE=")
check_outputsqlitedb = check_config("OUTPUT_SQLITE3")
if check_outputfile == "ON" or check_outputsqlitedb == "ON":
	print_status(module,"loading...")
	thread.start_new_thread(main, ())
else:
	print_error(module,"Cannot start, no output configured.")
