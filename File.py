#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import os

from os.path import join

from Comment import CommentRegister

from LogicalBlock import LogicalBlock as LB

from Namespace import Namespace

from ParsingMethods import *

from settings import *

class File:
    def __init__(self,projectpath,name):
        self.Path = join(projectpath,name)
        self.Path = "/output/" + self.Path[self.Path.find("in")+3:]
        f = open(join(projectpath,name))
        self.OriginalText = f.read()
        self.Namespaces=[]
        f.close()
        
        
    def Clean(self):
        self.CleanCode = CleanCommentsAndStrings(self.OriginalText)
        self.CleanCode = CleanLogicalBlocks(self.CleanCode)
        self.CleanCode = CleanEmptyRowsAndSpaces(self.CleanCode)
        
    def GetClasses(self):
        tmp = self.CleanCode
        for NSdef in NamespaceDefinition:
            start = NSdef[0]
            if (len(NSdef)==1):
                end = Tag.format(name="LogicalBlockStart",idValue=0)[:19]
            else:
                end= NSdef[1]
            if (tmp.find(start)>-1):
                pos = 0
                while (tmp[pos:].find(start)>-1):
                    NSpos=tmp.find(start) + len(start)
                    NSname = tmp[NSpos:tmp[NSpos:].find(end)+NSpos].replace(" ","").replace("\n","")
                    NSlogBlockStartPos= tmp[NSpos:].find(Tag.format(name="LogicalBlockStart",idValue=0)[:19]) + NSpos
                    NSlogBlockID=tmp[NSlogBlockStartPos:]
                    NSlogBlockID = NSlogBlockID[NSlogBlockID.find("ID=")+3:]
                    NSlogBlockID = NSlogBlockID[:NSlogBlockID.find(Tag.format(name="LogicalBlockStart",idValue=0)[-3:])]
                    NSlogBlockEndPos=tmp.find(Tag.format(name="LogicalBlockEnd",idValue=NSlogBlockID)) + len(Tag.format(name="LogicalBlockEnd",idValue=NSlogBlockID))
                    self.Namespaces.append(Namespace(NSname,tmp[NSlogBlockStartPos:NSlogBlockEndPos]))
                    tmp = tmp[:NSlogBlockStartPos] + Tag.format(name="Namespace",idValue=NSname) + tmp[NSlogBlockEndPos:]
                    pos = NSlogBlockStartPos
            else:
                self.Namespaces.append(Namespace("BaseNamespace",tmp))
        
    def __str__(self):
        return self.Path
        
    def __repr__(self):
        return self.__str__()
        
    def Save(self):
        tmpPath = self.Path[::-1]
        tmpPath = tmpPath[tmpPath.find("\\"):]
        tmpPath = tmpPath[::-1]
        
        if not os.path.exists(tmpPath):
            os.makedirs(tmpPath)
        f = open(self.Path,'w')
        f.write(self.CleanCode)
        f.close()

