import os, sys, string
from os import listdir
from os.path import isfile, join

mypath = sys.argv[1]
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for f in onlyfiles:
	print(f + "\n")
	#raw_input()
	str = mypath + f
	cmd = "head -n 1 " + str
	#print genome name
	os.system(cmd)