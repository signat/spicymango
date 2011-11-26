#!/usr/bin/env python

import sys,time
from src.core import *

#Print Banner
print ""
print " ___      _         __  __"                    
print "/ __|_ __(_)__ _  _|  \/  |__ _ _ _  __ _ ___" 
print "\__ \ '_ \ / _| || | |\/| / _` | ' \/ _` / _ \\"
print "|___/ .__/_\__|\_, |_|  |_\__,_|_||_\__, \___/"
print "    |_|        |__/                 |___/"     
print "The Open Source Intelligence Analysis Tool"
print ""
print "SpicyMango v0.1"
print "Written by: Chris Centore, Steve Swann, Jason Gunnoe"
print "Website: http://code.google.com/p/spicymango/"
print "Download: svn co http://spicymango.googlecode.com/svn/trunk/ spicymango/"
print ""

mod_counter = 0

# Check to see if mod_irc is enabled, if so, run it.
enable_modirc = check_config("MOD_IRC=")
if enable_modirc == 'ON':
        import modules.mod_irc
	mod_counter += 1
enable_modtwitter = check_config("MOD_TWITTER=")
if enable_modtwitter == 'ON':
        import modules.mod_twitter
	mod_counter += 1
if mod_counter == 0:
	print "\n[!] Error: Please enable a module in the config file.\n"
	sys.exit()

while 1:
        try:
                time.sleep(100000)
        except KeyboardInterrupt:
                print "\n[!] Quiting SpicyMango...\n"
                sys.exit()
