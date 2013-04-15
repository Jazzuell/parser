#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class ClassRegister:
    @staticmethod
    def GetClass(IdName):
        for cl in ClassRegister.Classes:
            if cl.Name==idName:
                return cl
        raise ValueError("IdName danej triedy nie je registrovane",IdName)

ClassRegister.Classes=[]

class Class:
    def __init__(self,name,code):
        self.Public = False
        self.Private = False
        self.Protected = False
        self.Static = False
        
        self.Name = name
        self.__code = code
        self.Attributes=[]
        self.Propperties=[]
        self.Methods=[]
        
    def __str__(self):
        return self.Name