#!/usr/bin/env python

import sys,time, sqlite3
from src.core import *

#Read code to dynamically call the name of this script.
execfile('src/getname')

#Print Banner
print ""
print " ___      _         __  __"                    
print "/ __|_ __(_)__ _  _|  \/  |__ _ _ _  __ _ ___" 
print "\__ \ '_ \ / _| || | |\/| / _` | ' \/ _` / _ \\"
print "|___/ .__/_\__|\_, |_|  |_\__,_|_||_\__, \___/"
print "    |_|        |__/                 |___/"     
print "The Open Source Intelligence Analysis Engine"
print ""
print "SpicyMango v0.1 Alpha"
print "Written by: Chris Centore, Steve Swann, Jason Gunnoe"
print "Website: http://code.google.com/p/spicymango/"
print "Download: svn co http://spicymango.googlecode.com/svn/trunk/ spicymango/"
print ""

# First setup configured output destinations
# If configured and doesn't exist, setup output file
if check_config("OUTPUT_FILE=") == 'ON':
	path = check_config("OUTPUT_FILE_NAME=")
	if not os.path.isfile(path):
		outputfile = file(path, "w")
		outputfile.close()

# If configured and doesn't exist, setup output DB
if check_config("OUTPUT_SQLITE3=") == 'ON':
	path = check_config("OUTPUT_SQLITE3_DB_PATH=")
	if not os.path.isfile(path):
		conn = sqlite3.connect(path)
		c = conn.cursor()
		c.execute('CREATE TABLE spicymango (modname TEXT, username TEXT COLLATE NOCASE, hostname TEXT COLLATE NOCASE, ircchan TEXT, msg TEXT COLLATE NOCASE, timeStamp DATE, hash TEXT UNIQUE, id INTERGER PRIMARY KEY)')
		conn.commit()
		c.close()

# Setup counter for determining how many modules are loaded at runtime.
mod_counter = 0

# Check to see which modules are enabled. Then run them.
enable_modirc = check_config("MOD_IRC=")
if enable_modirc == 'ON':
        import modules.mod_irc
	mod_counter += 1
enable_modtwitter = check_config("MOD_TWITTER=")
if enable_modtwitter == 'ON':
        import modules.mod_twitter
	mod_counter += 1
enable_modfacebook = check_config("MOD_FACEBOOK=")
if enable_modfacebook == 'ON':
        import modules.mod_facebook
	mod_counter += 1
#If no modules are enabled in the config, error and exit.
if mod_counter == 0:
	print_error(module,"Please enable a module in the config file.")
	sys.exit()

# Run Web View if enabled in the config
enable_webview = check_config("WEB_VIEW=")
if enable_webview == 'ON':
	import web.web_view

# Let the program continue to run until an interrupt is recieved.
while 1:
        try:
                time.sleep(100000)
        except KeyboardInterrupt:
                print_warning(module,"Quiting SpicyMango...")
                sys.exit()
