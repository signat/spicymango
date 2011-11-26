import os,re

def check_config(param):
	path = os.path.join(os.path.dirname(__file__), '..', 'config')
        fileopen = file(path, "r")
        # iterate through lines in file
        for line in fileopen:
		if not re.search('#.', line):
                	match = re.search(param, line)
                	if match:
                        	line = line.rstrip()
                        	line = line.replace('"', "")
                        	line = line.split("=")
                        	return line[1]

def get_keywords(param):
        path = os.path.join(os.path.dirname(__file__), '..', 'keywords')
        fileopen = file(path, "r")
	wordlist = []
        # iterate through lines in file
        for line in fileopen:
                if not re.search('#.', line):
                        match = re.search(param, line)
                        if match:
				wordlist.append(eval(line))
        return wordlist
