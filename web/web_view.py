#########################################################################
# Filename: web_view.py
# Description: Invokes a stand-alone webserver to create an interactive
#	       GUI to SpicyMango.
# Copyright (C) 2011-2012 Chris Centore
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or any later 
#    version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# SpicyMango written by: Chris Centore, Steve Swann, Jason Gunnoe
# Website: http://code.google.com/p/spicymango/
# Download: svn co http://spicymango.googlecode.com/svn/trunk/ spicymango/
#
#########################################################################

from __future__ import division
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
		display_main = template('webview')
		if request.get_cookie("loggedin", secret='sm2345-45634'):
			return display_main
		else:
			redirect('/login')
	
	#Routes for Login
	@route('/login')
	def login():
		return template('login')	
	
	@post('/login-check')
	def logincheck():
		if request.forms.get('user') == 'smadmin' and request.forms.get('pass') == 'sm1234':
                        response.set_cookie("loggedin", "Success", secret='sm2345-45634')
                        redirect('/')
		else:
			redirect('/login')

	#Route for AJAX call for JSON Data
	@route('/get_json')
	def get_json():
		import sqlite3, json
		from math import ceil
		database = check_config("OUTPUT_SQLITE3_DB_PATH=")
		conn = sqlite3.connect(database)
                c = conn.cursor()

		ops = {'eq' : '=', 'cn' : 'LIKE'}
		def getWhere(col, oper, val):
			if oper == 'cn':
				val = '%'+val+'%'
			return "WHERE " + col + " " + ops[oper] + " '" + val + "' "	
		
		where = ""
		if request.query.searchField:
			where = getWhere(request.query.searchField, request.query.searchOper, request.query.searchString)
		start = int(request.query.rows) * int(request.query.page) - int(request.query.rows)
		
		sqlcount = "select count(*) from spicymango " + where
		c.execute(sqlcount)
		count = c.fetchone()

		sqlquery = "select timeStamp,modname,username,hostname,ircchan,msg from spicymango " + where + "order by " + request.query.sidx + " " + request.query.sord + " LIMIT " + request.query.rows + " OFFSET " + str(start) 
		results = c.execute(sqlquery)

		if count > 0:
			total_pages = int(ceil(float(count[0]) / float(int(request.query.rows))))
		else:
			total_pages = 0		
		
		if int(request.query.page) > total_pages:
			page = str(total_pages)
		else:
			page = str(request.query.page)

		json_data = {}
		json_data['page'] = page
		json_data['total'] = str(total_pages)
		json_data['records'] = str(count[0])
		
		cell_id = 1
		json_data['rows'] = []
		for row in results:
			msg_row = row[5]
		        r1 = r"(http://\S*(?=(]|\)|\b)))"
        		msg_row = re.sub(r1,r'<a rel="nofollow" target="_blank" href="\1">\1</a>',msg_row)
			json_data['rows'].append({'id' : str(cell_id), 'cell' : [row[0], row[1], row[2], row[3], row[4], msg_row]})
			cell_id += 1
	
		response.set_header('Content-type', 'application/json')
		return json.dumps(json_data, indent=4) 

	#TEST JSON FILE
	@route('/get_json_file')
	def send_json_file():
		return static_file('json.txt', root='web/')

	#Route for png images
	@route('/images/:filename#.*\.png#')
	def send_image(filename):
    		return static_file(filename, root='web/images/', mimetype='image/png')

	@route('/css/ui-darkness/images/:filename#.*\.png#')
        def send_cssimage(filename):
                return static_file(filename, root='web/css/ui-darkness/images/', mimetype='image/png')

	#Route for style sheets
	@route('/css/:filename#.*\.css#')
        def send_image(filename):
                return static_file(filename, root='web/css/')

	#Route for javascript
	@route('/js/:filename#.*\.js#')
        def send_image(filename):
                return static_file(filename, root='web/js/')

	#Route for HTML
	@route('/:filename#.*\.html#')
        def send_image(filename):
                return static_file(filename, root='web/')


	# Run Web View webserver on specified ip and port
	print_status(module,"Connect to http://%s:%s" % (ip, port))
	run(port=port, host=ip, quiet="True")

#If the output file option is not set in the config, don't run.
check_outputsqlitedb = check_config("OUTPUT_SQLITE3")
if check_outputsqlitedb == "ON":
	print_status(module,"loading...")
	thread.start_new_thread(main, ())
else:
	print_error(module,"Cannot start, no database configured.")
