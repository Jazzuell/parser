#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class Parameter:
    def __init__(self,name,type,defaultvalue=None):
        self.Name = name
        self.Type=type
        self.DefaultValue=defaultvalue
        
    def __str__(self):
        if (DefaultValue):
            return self.Type + " " + self.Name + "=" + self.DefaultValue
        return self.Type + " " + self.Name 