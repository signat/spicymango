import thread,sys,re
from includes import irc
sys.path.append("..")
from src.core import *
from src.output import *

def main():
	#Get parameters from config file
	irc_server = check_config("MOD_IRC_SERVER=")
	irc_channels = check_config("MOD_IRC_CHANNELS=")
	irc_user = check_config("MOD_IRC_USER=")

	def handle_state(newstate):
	    if newstate==4:
		channels = irc_channels.split(',')
		for channel in channels:
	        	MyConn.send_string("JOIN #" + channel)
			print "[!] MOD_IRC: Joined channel #" + channel

	def handle_raw(line):
	    print line

	def handle_parsed(prefix, command, params):
	    if command=="PRIVMSG":
		keywords = get_keywords("mod_irc")
		for keyword in keywords:
			hit = re.search(keyword[1], params[1])
			if hit:
				output_file_enable = check_config("OUTPUT_FILE")
                    		if output_file_enable == "ON":
                        		output_file("MOD_IRC: " + prefix + " : " + params[0] + " : " + params[1])
                        	else:
                        		print "MOD_IRC: " + prefix + " : " + params[0] + " : " + params[1]


	MyIRC=irc.IRC_Object( )
	MyConn=MyIRC.new_connection( )

	MyConn.nick=irc_user
	MyConn.ident=irc_user
	MyConn.server=(irc_server, 6667)
	MyConn.realname=irc_user

	MyConn.events['state'].add_listener(handle_state)
#	MyConn.events['raw'].add_listener(handle_raw)
	MyConn.events['parsed'].add_listener(handle_parsed)

	while 1:
	    MyIRC.main_loop( )

print "[!] MOD_IRC: loading..."
thread.start_new_thread(main, ())
