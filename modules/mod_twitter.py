import thread,sys
sys.path.append("..")
from src.core import *
from xml.dom import minidom
import time, urllib

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

		    print "MOD_TWITTER: " + name + ": " + title + " [" + pub + "]"
	 
	    time.sleep(interval)

print "[!] MOD_TWITTER: loading..."
keywords = get_keywords("mod_twitter")
for keyword in keywords:
	thread.start_new_thread(main, (keyword[1],2))
