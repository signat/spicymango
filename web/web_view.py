import thread,sys
sys.path.append("..")
from src.bottle import route, run, template
from src.core import *

def main():
	ip = check_config("WEB_VIEW_IP=")
	port = check_config("WEB_VIEW_PORT=")
	outfile = check_config("OUTPUT_FILE_NAME=")

	@route('/')
	def mainview():
		filelines = reversed(open(outfile).readlines())
    		display_output = template('base', lines=filelines)
		return display_output

	run(port=port, host=ip, quiet="True")

print "[!] Starting Web View..."
thread.start_new_thread(main, ())
