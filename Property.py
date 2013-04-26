#! /usr/bin/env python
# -*- coding: utf-8 -*- 

#from ParsingMethods import ConvertLogicalBlocks

#import ParsingMethods

class Property:
    def __init__(self):
        self.Body = ""
        self.Name = ""
        self.Type = ""
        self.Public = False
        self.Private = False
        self.Static = False
        self.Protected = False
        
    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        return self.Type + " " + self.Name + "| " + ConvertLogicalBlocks(self.Body) + "|" 