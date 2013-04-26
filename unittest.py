#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import subprocess
import sys

def ExecuteThis(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    ex = ""
    work = True
    while work:
        out = process.stdout.readline(1)
        if out == '' and process.poll() != None:
            work=False
        else:
            ex+=out
    return ex

print "*"*50    
print ExecuteThis("Python start.py language=csharp")
print "*"*50
print ExecuteThis("Python start.py projectpath=input/csharpproject2/")
print "*"*50
print ExecuteThis("Python start.py parse")
print "Parsing completed"
print "*"*50
classnames = ExecuteThis("Python start.py getclassnames")
print "Class names>>>\n",classnames
classname=classnames.split("\n")[5].replace("\r","")
print "Choosen >>>",classname
print "*"*50
print "Class methods >>> ",classname
print ExecuteThis("Python start.py getmethods="+classname)
print "*"*50
