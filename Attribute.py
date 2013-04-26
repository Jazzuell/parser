#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class Attribute:
    def __init__(self):
        self.Name = ""
        self.Type= ""
        self.Private = False
        self.Public = False
        self.Static = False
        self.Protected = False
        self.Final = False
        self.Value = ""
        
    def __str__(self):
        return self.Type + " " + self.Name 

    def __repr__(self):
        return self.__str__()        