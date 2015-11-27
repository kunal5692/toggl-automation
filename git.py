#!/usr/bin/env python

"""
Python script to automatically get the changes in the git directory.
Author : Kunal Chavhan
Email : kunal.chavhan005@gmail.com
"""

import subprocess
import os
import sys

path=""
cwd=""

def getBranchName(result):
	branch = result[0]
	return branch[10:-1]

def getCommmit(commit):
	head = commit[0]
	return head[7:-1]


def gitCommands(command):
	os.chdir(path)
	try:
		output = subprocess.check_output(command,
			stderr=subprocess.STDOUT,
			shell = True)
	except subprocess.CalledProcessError as error:
		print error

	os.chdir(cwd)
	fobj = open("gitChanges.txt","w")
	for i in output:
 		fobj.write(i)
	fobj.close()

def readGitChanges():
	result =[]
	with open('status.txt') as f:
		for line in f:
			#print line[:-1]
			result.append(line)
	os.chdir(path)


def main():
	global path 
	path = raw_input("Please enter patht to your working git directory: ")
	global cwd 
	cwd = os.getcwd()
	os.chdir(path)	
	gitCommands("ls")

	#branch = getBranchName(result)
	#print("your workiong branch is: ",branch)

if __name__ == '__main__':
	main()

