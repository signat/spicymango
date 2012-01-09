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

import os,sys,datetime
from core import *
from string import printable

def rmNonprint(myStr):
	filtered_string = ''.join(filter(lambda x: x in printable, myStr))
	return filtered_string

class Output(object):
	#Define all attributes for module output
        modname = ''
        username = ''
	hostname = ''
	ircchan = ''
	msg = ''
	
	
	#Method to send output to various enabled destinations
        def send_output(self):
		#Method function for writing to a file
                def to_File():
                        path = check_config("OUTPUT_FILE_NAME=")
                	if not os.path.isfile(path):
                        	outputfile = file(path, "w")
                	else:
                       		outputfile = file(path, "a")

			outString = str(datetime.datetime.now()) + ": " + rmNonprint(self.modname)
			if self.username != '':
				outString += ": " + rmNonprint(self.username)
			if self.hostname != '':
                                outString += ": " + rmNonprint(self.hostname)
			if self.ircchan != '':
                                outString += ": " + rmNonprint(self.ircchan)
			if self.msg != '':
                                outString += ": " + rmNonprint(self.msg)
                	outputfile.write(outString + "\n")
                	outputfile.close()
		def to_Sqlite3():
			import sqlite3
			path = check_config("OUTPUT_SQLITE3_DB_PATH=")
			if not os.path.isfile(path):
				conn = sqlite3.connect(path)
				c = conn.cursor()
				c.execute('CREATE TABLE spicymango (modname TEXT, username TEXT, hostname TEXT, ircchan TEXT, msg TEXT, timeStamp DATE, id INTERGER PRIMARY KEY)')
			else:
				conn = sqlite3.connect(path)
				c = conn.cursor()
			sql = "INSERT INTO spicymango VALUES (?, ?, ?, ?, ?, ?, NULL)"
			c.execute(sql, (rmNonprint(self.modname), rmNonprint(self.username), rmNonprint(self.hostname), rmNonprint(self.ircchan), rmNonprint(self.msg), datetime.datetime.now()))
			conn.commit()
			c.close()
			                
		#Check config and send output where enabled, but first make sure required attributes are set.
		if self.modname is None:
			print_error("Output", "modname attribute must be defined in instance")
		
		#Counter var to determine if any ouput is enabled.
		output_count = 0
		
		file_enable = check_config("OUTPUT_FILE")
        	if file_enable == "ON":
			to_File()
			output_count = 1
		sqlite3_enable = check_config("OUTPUT_SQLITE3=")
		if sqlite3_enable == "ON":
			to_Sqlite3()
			output_count = 1
		#If no output destinations are defined in config, send output to console
		if output_count == 0 or check_config("OUTPUT_CONSOLE=") == "ON":
                        conString = ''
			if self.username != '':
                                conString += ": " + rmNonprint(self.username)
                        if self.hostname != '':
                                conString += ": " + rmNonprint(self.hostname)
                        if self.ircchan != '':
                                conString += ": " + rmNonprint(self.ircchan)
                        if self.msg != '':
                                conString += ": " + rmNonprint(self.msg)

			print '\033[94m' + rmNonprint(self.modname) + ": " + '\033[0m' + str(datetime.datetime.now()) + conString
