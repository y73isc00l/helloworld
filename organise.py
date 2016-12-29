#this is a python script to find a particular type of file(i.e. with a particular extension and store it to specified folder path
#the script is accompanied with its own readme file
import os;
import shutil;
import sys;
searchdir=sys.argv[1];
for file in os.listdir(searchdir):
	if file.endswith("."+sys.argv[2]):
		shutil.move(sys.argv[1]+"/"+file,sys.argv[3]);

		
