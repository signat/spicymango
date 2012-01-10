#########################################################################
#
# Facebook Module for SpicyMango
# Author(s): Chris Centore, Jason Gunnoe
#
# Description: This module queries Facebook using its graph API and returns the
#	       results to the specified output.  
#
# SpicyMango written by: Chris Centore, Steve Swann, Jason Gunnoe
# Website: http://code.google.com/p/spicymango/
# Download: svn co http://spicymango.googlecode.com/svn/trunk/ spicymango/
#
#########################################################################

import thread,sys
sys.path.append("..")
from src.core import *
from src.output import *
import json, urllib2, time

#Read in code to dynamically get the module name.
execfile('src/getname')

#Get configuration options
interval = int(check_config("MOD_FACEBOOK_INTERVAL="))

def main(query,*args):
	global interval
	while True:
            

            url = "http://graph.facebook.com/search?q=%s&type=post" % (query) 

            data = json.load(urllib2.urlopen(url))

#            Enable this print to see the raw data dump for troubleshooting
#            print json.dumps(data)

            for post in data['data']:
                if post['type'] == 'link':
			modOutput = Output()
                    	modOutput.modname = module
                    	modOutput.username = post['from']['name']
                   	try:
				modOutput.msg = post['message']
                    	except KeyError:
                    		pass
			modOutput.send_output()
	    
            #Set delay should be at least 5 seconds maybe more for facebook.
	    time.sleep(interval)

#Start the module
print_status(module,"loading...")
keywords = get_keywords("mod_facebook")
#Create a new thread for each search phrase
for keyword in keywords:
	thread.start_new_thread(main, (keyword[1],2))
