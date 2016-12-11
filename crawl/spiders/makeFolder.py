# -*- coding: utf-8 -*-
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def makeFolder(dirName):
	dirNameArr = dirName.split("/")
	fullDir = "./"
	for name in dirNameArr:
		fullDir = fullDir + "/" + name
#print fullDir
		if not os.path.exists(fullDir):
				os.makedirs(fullDir)
