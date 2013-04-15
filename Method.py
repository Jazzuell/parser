#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class Method:
    def __init__(self,name,returntype,visibility="public"):
        self.Name = name
        self.ReturnType=returntype
        self.Visibility=visibility
        self.Parameters=[]
        self.Variables=[]
        self.Body=""
    def __str__(self):
        return self.Visibility+" " + self.Type + " " + self.Name