#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import Comment
import os
import sys
from Project import Project
from Class import ClassRegister
from Comment import CommentRegister
#from settings import *
from RefactoringMethods import *    
def usage():
    print "==================="
    print "     USAGE"
    print "==================="
    print "     Commands"
    print """
        -help,help,h,-h  for displaying this help
        language=language , -l=language  to set up input programing language
        projectpath=path, -pp=path  sets path of project direcotry
        parse , -p execute parsing algorithm
        getclassnames , -cln print out names of parsed classes
        getmethods=class, getmethodnames=class prints out method names of class
        all,-a prints out everything about stored classes
        
         
        """

def main(argv):
    path = "input/"
    #print "==",argv,"=="
    
    global p
    from settings import FileExtensions
    
    #p.Save()
    
    #for cls in ClassRegister.Classes:
     #   print cls
    
    if len(argv) == 0:
        usage()
        sys.exit()
    for arg in argv:
        if (arg in ["-help","help","h","-h"]):
            usage()
            sys.exit()
        if (arg.startswith("language=") or arg.startswith("-l=")):
                language = arg[arg.find("=")+1:].lower()
                from shutil import copy2
                if (language == "python"):
                    copy2("Python/settings.py","settings.py")
                elif (language == "java"):
                    copy2("Java/settings.py","settings.py")
                elif (language == "csharp" or language =="c#"):
                    copy2("Csharp/settings.py","settings.py")
                else:
                    print "Not supported language"
                import imp
                import settings
                imp.reload(settings)
                print "Language set to",settings.LanguageName
                
        if (arg.lower().startswith("projectpath=") or arg.lower().startswith("-pp=")):
            newpath = arg[arg.find("=")+1:]
            t = open("actualproject.py")
            f = t.read()
            t.close()
            pos=f.find("ActualProjectPath=")+18
            f = f[:pos] + '"'+newpath+'"'+ f[f[pos:].find("\n")+pos:]
            u = open("actualproject.py","w")
            u.write(f)
            u.close()
            print "Project path set to",newpath
            
        if (arg.lower() ==("parse") or arg.lower()==("-p")):
            import imp
            import actualproject
            imp.reload(actualproject)
            p = Project(actualproject.ActualProjectPath,FileExtensions)
            import pickle
            pickle.dump(p,open(actualproject.ActualProjectPath+"project.data","wb"))
            pickle.dump(ClassRegister.Classes,open(actualproject.ActualProjectPath+"classes.data","wb"))
            pickle.dump(CommentRegister.Comments,open(actualproject.ActualProjectPath+"strings.data","wb"))
            
        if (arg.lower()=="getclassnames" or arg.lower()=="-cln"):
            PickUpData()
            for c in ClassRegister.Classes:
                print c.Name
                
        if (arg.lower().startswith("getmethods=") or arg.lower().startswith("getmethodnames=") or arg.lower().startswith("-gmn=")):
            classname = arg[arg.find("=")+1:]
            PickUpData()
            from RefactoringMethods import FindClass
            for method in FindClass(classname).Methods:
                print method.Name
            
        if (arg.lower()== "all" or arg.lower()=="-a"):
            PickUpData()
            for cls in ClassRegister.Classes:
                print cls

def PickUpData():
        import pickle
        import actualproject
        ClassRegister.Classes = pickle.load( open( actualproject.ActualProjectPath+"classes.data", "rb" ) )
        CommentRegister.Comments  = pickle.load( open( actualproject.ActualProjectPath+"strings.data", "rb" ) )
        p = pickle.load( open( actualproject.ActualProjectPath+"project.data", "rb" ) )

            
if __name__ == "__main__":
   main(sys.argv[1:])            
 