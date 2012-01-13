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
from xml.parsers import expat
import time, urllib

#Read in code to dynamically get the module name.
execfile('src/getname')

#Get configuration options
count = check_config("MOD_TWITTER_COUNT=")
interval = int(check_config("MOD_TWITTER_INTERVAL="))

def main(query,*args):
	id = 0
	global count, interval
	while True:

		try:
			url = "http://search.twitter.com/search.atom?rpp=" + count + "&q=%s&since_id=%s" % (query, id)
			xml = urllib.urlopen(url)
			doc = minidom.parse(xml)
			entries = doc.getElementsByTagName("entry")

			if len(entries) > 0:
				entries.reverse()
				#If entries, interate through entries and output results.
				for e in entries:
					title = e.getElementsByTagName("title")[0].firstChild.data.replace("\n", "")
		    			pub = e.getElementsByTagName("published")[0].firstChild.data
		    			id = e.getElementsByTagName("id")[0].firstChild.data.split(":")[2]
		    			name = e.getElementsByTagName("name")[0].firstChild.data.split(" ")[0]
		    			#Try output...non-ascii will throw an exception otherwise.
		 			try:
						modOutput = Output()
						modOutput.modname = module
						modOutput.username = name
						modOutput.msg = title
						modOutput.send_output()
	 	    			except UnicodeEncodeError:
						pass
						#print_warning(module, "Couldn't print line because it contains non-ASCII values.
		except expat.ExpatError:
			print_warning(module, "Rate limit exceeded...delaying 120 seconds.")
			time.sleep(120)
		#Set delay should be at least 5 seconds.
		time.sleep(interval)

#Start the module
print_status(module,"loading...")
keywords = get_keywords("mod_twitter")
#Create a new thread for each search phrase
for keyword in keywords:
	thread.start_new_thread(main, (keyword[1],2))
