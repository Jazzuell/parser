#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# Filename: Project.py

if __name__ == '__main__':
    print "snazis sa len spustit"
else:
    print "importujes ma"
    from os import listdir,walk
    from os.path import isfile, join
    from File import File
    from Comment import CommentRegister

    def GetFileNamesInDirectory(path,extensions):
        f = []
        for (dirpath, dirname, filenames) in walk(path):
            for file in filenames:
                for extension in extensions:
                    if (file.endswith(extension)):
                        f.append([dirpath,file])
        return f

    class Project:
        def __init__(self,path,extensions):
            print "project init", path,extensions
            self.Path=path
            self.Name=(path.split("\\"))[-1]
            if (len(path.split("\\"))==1):
                self.Name=(path.split("/"))[-1]
            fnames = GetFileNamesInDirectory(path,extensions)
            self.Files=[]
            self.X = self.Name
            for name in fnames:
                self.Files.append(File(name[0],name[1]))
            for f in self.Files:
                f.Clean()
            for f in self.Files:
                f.GetClasses()
        def Save(self):
            for f in self.Files:
                print "saving file ",f
                f.Save()
                
        def __str__(self):
            return self.Name