#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class Parameter:
    def __init__(self,name,type,defaultvalue=None):
        self.Name = name
        self.Type=type
        self.Value=defaultvalue
        
    def __str__(self):
        if (self.Value):
            return self.Type + " " + self.Name + "=" + Value
        return self.Type + " " + self.Name 

    def __repr__(self):
        return self.__str__()        