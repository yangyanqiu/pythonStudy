import os
import sys

def findFilePath(dir, file):
	for filename in os.listdir(dir):
		if os.path.isdir(dir+filename):
			if filename == file:
				print "Directory path: " + dir + filename
			filename = dir + filename
			findFilePath(filename, file)
		else:
			if not dir.endswith("/"):
				dir = dir + "/"
			if filename == file :
				print dir + filename

def main(argv):
	if len(argv) >= 3:
		path = argv[1]
		if argv[2] == "-name":
			file = argv[3]
		else:
			file = argv[2]
	else:
		print "Please enter right format:"
		print "e.g. python superFind.py / -name file.py"
		return
	findFilePath(path, file)
if __name__ == "__main__":
	main(sys.argv)
		
