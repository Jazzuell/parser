#! /usr/bin/env python
# -*- coding: utf-8 -*- 
from os.path import join
import os
from Comment import CommentRegister
from settings import *
from LogicalBlock import LogicalBlock as LB
3

def FindText(text,startchar,endchar):
    startpos=text.find(startchar)
    endpos = text[startpos+len(startchar):].find(endchar)+startpos+len(startchar)
    extracted = text[startpos:endpos+len(endchar)]
    return extracted,startpos,endpos

def ExtractText(text,startchar,endchar):
    startpos=text.find(startchar)
    endpos = text[startpos:].find(endchar)+startpos
    cleanText= text[:startpos]+text[endpos+1:]
    extracted = text[startpos:endpos+1]
    return cleanText,extracted,startpos,endpos

def ReplaceAtPositons(originalText,NewText,StartPosition,EndPosition):
    return originalText[:StartPosition]+NewText+originalText[EndPosition+1:]

def CleanCommentsAndStrings(text):
    cleanCode = text
    for strc in StringChars:
        if len(strc)!=2:
            raise ValueError('string musi mat zaciatocny a ukoncovaci znak v settings/StringChars')
        else:
            while (cleanCode.find(strc[0])!=-1):
                comnt,startP,endP =FindText(cleanCode,strc[0],strc[1])
                CommentRegister.AddComment(comnt)
                cleanCode = ReplaceAtPositons(cleanCode,Tag.format(name="Comment",idValue=str(CommentRegister.ID)),startP,endP)
    for cmt in CommentChars:
        if len(cmt)==2:
            while (cleanCode.find(cmt[0])!=-1):
                comnt,startP,endP =FindText(cleanCode,cmt[0],cmt[1])
                CommentRegister.AddComment(comnt)
                cleanCode = ReplaceAtPositons(cleanCode,Tag.format(name="Comment",idValue=str(CommentRegister.ID)),startP,endP)
        elif len(cmt)==1:
            while (cleanCode.find(cmt[0])!=-1):
                comnt,startP,endP =FindText(cleanCode,cmt[0],"\n")
                CommentRegister.AddComment(comnt)
                cleanCode = ReplaceAtPositons(cleanCode,Tag.format(name="Comment",idValue=str(CommentRegister.ID)),startP,endP-1)
        else:
            raise ValueError('nespravna hodnota v settings/CommentChars')
    return cleanCode    

def CleanLogicalBlocks (text):
    for lb in LogicalBlock:
        if len(lb)==1:
            raise NotImplemented("Tento typ logickeho bloku nie je implementovany")
            """
            text=text.replace("\t",Spacing)
            while (text.find(lb[0])):
                pos = text.find(b[0])
                pomtext=text(:pos+len(lb[0]))
                pomtext+=Tag.format(name="LogicalBlockStart",idValue="0")
                posC=pos+len(lb[0])
                C=text[posC]
                count =0
                while (text.find("\n\n")>-1)
                    text=text.replace("\n\n","\n")
                while (count==0):
                    while (C==" "):
                        count+=1
                        posC+=1
                        C=text[posC]
                    if C=="\n":
                        count = 0
            """
        elif len(lb)==2:
            start = lb[0]
            end = lb[1]
            end = end[::-1]
            #if (start.find(end)==-1 and end.find(start)==-1):
            while (text.find(start)>-1):
                LB.ID+=1
                pos = text.find(start)
                text = text[:pos+len(start)].replace(start,Tag.format(name="LogicalBlockStart",idValue=LB.ID)) + text[pos+len(start):]
                text = text[::-1]
                pos = text.find(end)
                text = text[:pos+len(end)].replace(end,(Tag.format(name="LogicalBlockEnd",idValue=LB.ID))[::-1]) + text[pos+len(end):]
                text=text[::-1]
            
            
        else:
            raise ValueError("Logicky blok musi mat definovanvy zaciatok")
    return text

def CleanEmptyRowsAndSpaces(inn):
    text = inn
    while (text.find("  ")>-1):
        text=text.replace("  "," ")
        print "*==================="
        text=text.replace("\t"," ")
        text=text.replace("  "," ")
        text = text.replace(" \n","\n")
        text = text.replace("\n\n","\n")
        text = text.replace("\n \n","\n")
        text = text.replace("\n\n","\n")
        text=text.replace("  "," ")
        text = text.replace("\n\n","\n")
        text=text.replace("  "," ")
        text = text.replace("  "," ")
    print "----------",text.find("  ")
    return text
    
class File:
    def __init__(self,projectpath,name):
        self.Path = join(projectpath,name)
        self.Path = "c:/dip/out/" + self.Path[self.Path.find("in")+3:]
        f = open(join(projectpath,name))
        self.OriginalText = f.read()
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
                    NSname = tmp[NSpos:tmp[NSpos:].find(end)+NSpos].replace(" ","")
                    print "NAMESPACE ",NSname
                    pos = NSpos
        pass
    def __str__(self):
        return self.Path
        
    def Save(self):
        tmpPath = self.Path[::-1]
        tmpPath = tmpPath[tmpPath.find("\\"):]
        tmpPath = tmpPath[::-1]
        
        if not os.path.exists(tmpPath):
            os.makedirs(tmpPath)
        f = open(self.Path,'w')
        f.write(self.CleanCode)
        f.close()

