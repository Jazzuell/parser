#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class Method:
    def __init__(self):
        self.Private = False
        self.Public = False
        self.Static = False
        self.Overrride = False
        self.Virtual = False
        self.Abstract = False
        self.Protected=False
        self.Final = False
        
        self.Name = ""
        self.ReturnType=None
        self.Parameters=[]
        self.Variables=[]
        self.Body=""
    
    def AddParameter(self,parameter):
        self.Parameters.append(parameter)
        
    def GetParameter(self,parameterName):
        for param in self.Parameters:
            if param.Name==parameter.Name:
                return param
        return None
        
    def RemoveParameters(self,paramName):
        self.Parameters.remove(GetParameter(paramName))
        
    def __repr__(self):
        return self.__str__()      
        
    def __str__(self):
        if not self.ReturnType:
            self.RetrunType=""
        return self.ReturnType + " " + self.Name + str(self.Parameters) 