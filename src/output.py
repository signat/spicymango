import os
from core import *

def output_file(data):
	path = check_config("OUTPUT_FILE_NAME=")
	if not os.path.isfile(path):
                outputfile = file(path, "w")
                outputfile.write(data + "\n")
                outputfile.close()
	else:
		outputfile = file(path, "a")
                outputfile.write(data + "\n")
                outputfile.close()
