import os
import sys

input = sys.argv[1]
filecount = 1

#批次修改檔名
for filename in os.listdir(input):
	os.rename(input + filename, input + str(filecount) + ".jpg")      
	filecount += 1
