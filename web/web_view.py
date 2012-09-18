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

import thread,sys
sys.path.append("..")
from src.bottle import route, run, template, static_file, request, response, redirect, post
from src.core import *
import sqlite3, datetime
from time import strftime
import json

#Read code to dynamically get name of this module.
execfile('src/getname')

def main():
	#Get config options
	ip = check_config("WEB_VIEW_IP=")
	port = check_config("WEB_VIEW_PORT=")
	
	#Route for the webroot
	@route('/')
	def mainview():
		username = request.get_cookie("loggedin", secret='sm2345-45634')
		if username:
			database = check_config("OUTPUT_SQLITE3_DB_PATH=")
                	conn = sqlite3.connect(database)
                	events = conn.cursor().execute('select count(id) from spicymango').fetchone()
			high_events = conn.cursor().execute('select count(id) from alerts where weight >= 30').fetchone()
			medium_events = conn.cursor().execute('select count(id) from alerts where weight between 10 and 30').fetchone()
			low_events = conn.cursor().execute('select count(id) from alerts where weight <= 10').fetchone()
			chart_highs = conn.cursor().execute("select count(s.id), strftime('%H', s.timeStamp) from spicymango s join alerts a on s.id = a.id where a.weight > 30 and s.timeStamp >= datetime('now', 'localtime', '-12 hour') group by strftime('%H', s.timeStamp)").fetchall()
			chart_mediums = conn.cursor().execute("select count(s.id), strftime('%H', s.timeStamp) from spicymango s join alerts a on s.id = a.id where a.weight between 10 and 30 and s.timeStamp >= datetime('now', 'localtime', '-12 hour') group by strftime('%H', s.timeStamp)").fetchall()
			chart_lows = conn.cursor().execute("select count(s.id), strftime('%H', s.timeStamp) from spicymango s join alerts a on s.id = a.id where a.weight < 10 and s.timeStamp >= datetime('now', 'localtime', '-12 hour') group by strftime('%H', s.timeStamp)").fetchall()
			recent_alls = conn.cursor().execute("select a.weight, s.msg, s.timeStamp from spicymango s join alerts a on s.id=a.id order by timeStamp DESC limit 7").fetchall()
			recent_highs = conn.cursor().execute("select s.msg, s.timeStamp from spicymango s join alerts a on s.id=a.id where a.weight >= 30 order by timeStamp DESC limit 7").fetchall()
			recent_mediums = conn.cursor().execute("select s.msg, s.timeStamp from spicymango s join alerts a on s.id=a.id where a.weight between 10 and 30 order by timeStamp DESC limit 7").fetchall()
			recent_lows = conn.cursor().execute("select s.msg, s.timeStamp from spicymango s join alerts a on s.id=a.id where a.weight <= 10 order by timeStamp DESC limit 7").fetchall()
			top_users = conn.cursor().execute("select s.username, count(s.username) from spicymango s join alerts a on s.id = a.id group by username order by count(username) DESC LIMIT 5").fetchall()
			top_alerts = conn.cursor().execute("select s.msg, a.weight from spicymango s join alerts a on s.id = a.id order by a.weight DESC LIMIT 5").fetchall()
			top_keywords = conn.cursor().execute("select keyword, count from keywords order by count DESC LIMIT 5").fetchall()
			conn.close()
			
			i = 0
			last_12 = []
			while i < 13:
				d = datetime.datetime.now() - datetime.timedelta(hours=i)
				hr = d.strftime("%H")
				last_12.append(hr)
				i += 1

			last_12.reverse()
			c_hours = ""
			c_highs = ""
			c_mediums = ""
			c_lows = ""
			for hour in last_12:
				high_count = "0"
				medium_count = "0"
				low_count = "0"
				for chigh in chart_highs:
					if hour == chigh[1]:
						high_count = str(chigh[0])
				for cmedium in chart_mediums:
					if hour == cmedium[1]:
						medium_count = str(cmedium[0])
				for clow in chart_lows:
					if hour == clow[1]:
						low_count = str(clow[0])
				c_hours = c_hours + "<th>"+hour+":00</th>"
				c_highs = c_highs + "<td>"+high_count+"</td>"
				c_mediums = c_mediums + "<td>"+medium_count+"</td>"
				c_lows = c_lows + "<td>"+low_count+"</td>"
			r_all = ""
			r_high = ""
			r_medium = ""
			r_low = ""
			for rall in recent_alls:
				if rall[0] >= 30:
					priority = "high"
					priority_label = "High"
				if 10 < rall[0] < 30:
					priority = "medium"
					priority_label = "Medium"
				if rall[0] <= 10:
					priority = "low"
					priority_label = "Low"
					
				r_all = r_all + "<tr><td><span class='ticket {!s}'>{!s}</span></td><td class='full'><a href='#'>{!s}</a></td><td class='who'>{!s}</td></tr>".format(priority, priority_label, rall[1], rall[2])
			for rhigh in recent_highs:
				r_high = r_high + "<tr><td><span class='ticket high'>High</span></td><td class='full'><a href='#'>{!s}</a></td><td class='who'>{!s}</td></tr>".format(rhigh[0], rhigh[1])
			for rmedium in recent_mediums:
				r_medium = r_medium + "<tr><td><span class='ticket medium'>Medium</span></td><td class='full'><a href='#'>{!s}</a></td><td class='who'>{!s}</td></tr>".format(rmedium[0], rmedium[1])
			for rlow in recent_lows:
				r_low = r_low + "<tr><td><span class='ticket low'>Low</span></td><td class='full'><a href='#'>{!s}</a></td><td class='who'>{!s}</td></tr>".format(rlow[0], rlow[1])
				
			return template('webview', eventcount=events[0], highs=high_events[0], mediums=medium_events[0], lows=low_events[0], chart_hours=c_hours, chart_highs=c_highs, chart_mediums=c_mediums, chart_lows=c_lows, recent_all=r_all, recent_highs=r_high, recent_mediums=r_medium, recent_lows=r_low, topusers=top_users, topalerts=top_alerts, topkeywords=top_keywords)
		else:
			redirect('/login')
	
	#Routes for Login
	@route('/login')
	def login():
		action = request.query.action
		if action == "logout":
			my_notice = "Logged Out"
			response.delete_cookie("loggedin")
		elif action == "error":
			my_notice = "Username or Password Incorrect"
		else:
			my_notice = ""
		return template('login', notice=my_notice)	
	
	@post('/login-check')
	def logincheck():
		if request.forms.get('login_user') == 'admin' and request.forms.get('login_password') == 'sm1234':
                        response.set_cookie("loggedin", request.forms.get('login_user'), secret='sm2345-45634')
                        redirect('/')
		else:
			redirect('/login?action=error')

	#Route for Events
	@route('/events')
	def eventpage():
		username = request.get_cookie("loggedin", secret='sm2345-45634')
		if username:
			return template('events')
		else:
			redirect('/login')
	
	#Route for AJAX Events
	@route('/events.txt')
	def eventpage():
		username = request.get_cookie("loggedin", secret='sm2345-45634')
		if username:
			database = check_config("OUTPUT_SQLITE3_DB_PATH=")
			conn = sqlite3.connect(database)
			rows = conn.cursor().execute("select modname, timeStamp, username, msg from spicymango order by timeStamp DESC").fetchall()
			conn.close()
			
			json_events = {}
                	json_events['aaData'] = []
                
			for row in rows:
				json_events['aaData'].append([row[0], row[1], row[2], row[3]])
        
			response.set_header('Content-type', 'application/json')
			return json.dumps(json_events, indent=4)

	#Route for Alerts
	@route('/alerts')
	def eventpage():
		username = request.get_cookie("loggedin", secret='sm2345-45634')
		if username:
			database = check_config("OUTPUT_SQLITE3_DB_PATH=")
			conn = sqlite3.connect(database)
			alows = conn.cursor().execute("select count(id) from alerts where weight <= 10").fetchone() 
			amediums = conn.cursor().execute("select count(id) from alerts where weight between 10 and 30").fetchone() 
			ahighs = conn.cursor().execute("select count(id) from alerts where weight >= 30").fetchone() 
			conn.close()
			return template('alerts', total_alert_highs=ahighs[0], total_alert_mediums=amediums[0], total_alert_lows=alows[0])
		else:
			redirect('/login')

	#Route for AJAX Alerts
	@route('/alerts.txt')
	def eventpage():
		username = request.get_cookie("loggedin", secret='sm2345-45634')
		if username:
			database = check_config("OUTPUT_SQLITE3_DB_PATH=")
			conn = sqlite3.connect(database)
			rows = conn.cursor().execute("select a.weight, s.modname, s.timeStamp, s.username, s.msg from spicymango s join alerts a on s.id=a.id").fetchall()
			conn.close()
			
			json_alerts = {}
                        json_alerts['aaData'] = []

                        for row in rows:
				if row[0] <= 10:
					priority = "Low"
					tdclass = "low"
				if 10 < row[0] < 30:
					priority = "Medium"
					tdclass = "medium"
				if row[0] >= 30:
					priority = "High"
					tdclass = "high"
				
				total_weight = "<span class=\'ticket "+tdclass+"\'>"+priority+"</span>"
                                json_alerts['aaData'].append([total_weight, row[0], row[1], row[2], row[3], row[4]])

                        response.set_header('Content-type', 'application/json')
                        return json.dumps(json_alerts, indent=4)

	#Route for png images
	@route('/images/:filename#.*\.png#')
	def send_image(filename):
    		return static_file(filename, root='web/images/', mimetype='image/png')

	#Route for jpg images
	@route('/images/:filename#.*\.jpg#')
	def send_image(filename):
    		return static_file(filename, root='web/images/', mimetype='image/jpg')
	
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
