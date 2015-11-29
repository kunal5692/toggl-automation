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

def gitBranchName():
	result = gitCommands("git status")
	branch = result[0]
	return branch[10:-1]

def gitLog():
	commit = gitCommands("git log")
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
	result = readGitChanges()
	os.chdir(path)
	return result

def readGitChanges():
	result =[]
	with open('gitChanges.txt') as f:
		for line in f:
			#print line[:-1]
			result.append(line)
	os.chdir(path)
	return result

def main():
	global path
	path = raw_input("Please enter patht to your working git directory: ")
	global cwd
	cwd = os.getcwd()
	branch = gitBranchName()
	print "You are on branch: ",branch
	head = gitLog()
	print "the commit head is at: ",head
	command = "git diff --name-only " + head
	result = gitCommands(command)
	print result
	#branch = getBranchName(result)
	#print("your workiong branch is: ",branch)

if __name__ == '__main__':
	main()
