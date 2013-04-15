#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import Comment
import os
import sys
from Project import Project
from settings import *

    
def usage():
    print "==================="
    print "     USAGE                      "
    print "==================="

def main(argv):
    print "start"
    #extensions = [".cs",]
    
    path = "c:\\dip\\in\\"
    global p
    p = Project(path,FileExtensions)
    print "startujem save"
    p.Save()
    print "Koniec"
    """
    projectpath = ""
    filepath = ""
    if len(argv) == 0:
        usage()
        sys.exit()
    for arg in argv:
        if (arg in ["-help","help","h","-h"]):
            usage()
            sys.exit()
            
        if (arg.startswith("projectpath=") | arg.startswith("-pp=")):
            projectpath = arg[arg.find("="):]
            print "project path = ",projectpath
			Project(projectpath)
        elif (arg.startswith("filepath=") | arg.startswith("-fp=")):
            filepath = arg[arg.find("="):]
            print "file path = ",filepath
    """
main("aaaa")