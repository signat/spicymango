#########################################################################
#
# Twitter Module for SpicyMango
# Author(s): Chris Centore, Jason Gunnoe
#
# Description: This module queries Twitter using its API and returns the
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
from xml.dom import minidom
import time, urllib

#Get configuration options
count = check_config("MOD_TWITTER_COUNT=")
interval = float(check_config("MOD_TWITTER_INTERVAL="))

def main(query,*args):
	id = 0
	global count, interval
	while True:

	    url = "http://search.twitter.com/search.atom?rpp=" + count + "&q=%s&since_id=%s" % (query, id)
	    xml = urllib.urlopen(url)
	    doc = minidom.parse(xml)
	    entries = doc.getElementsByTagName("entry")

	    if len(entries) > 0:
		entries.reverse()
		for e in entries:
		    title = e.getElementsByTagName("title")[0].firstChild.data
		    pub = e.getElementsByTagName("published")[0].firstChild.data
		    id = e.getElementsByTagName("id")[0].firstChild.data.split(":")[2]
		    name = e.getElementsByTagName("name")[0].firstChild.data.split(" ")[0]
		    
		    #Check for configured output, if not, write to console
		    output_file_enable = check_config("OUTPUT_FILE")
		    if output_file_enable == "ON":
			try:
		    		output_file("MOD_TWITTER: " + name + ": " + title + " [" + pub + "]")
	 	    	except:
				print "[!] MOD_TWITTER: Couldn't print line because it contains non-ASCII values."
		    else:
			print "MOD_TWITTER: " + name + ": " + title + " [" + pub + "]"
	    time.sleep(interval)

#Start the module
print "[!] MOD_TWITTER: loading..."
keywords = get_keywords("mod_twitter")
#Create a new thread for each search phrase
for keyword in keywords:
	thread.start_new_thread(main, (keyword[1],2))
