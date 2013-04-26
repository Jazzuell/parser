#! /usr/bin/env python
# -*- coding: utf-8 -*- 

from Method import Method
from Parameter import Parameter
#from Property import Property
from Attribute import Attribute

from ParsingMethods import CleanClassCode,ParseClassCode

from settings import *

class Class:
    def __init__(self,name,code):
        self.ID=0
        
        self.Public = False
        self.Private = False
        self.Protected = False
        self.Static = False
        self.Partial = False
        self.Final = False
        
        self.Name = name
        self.Code = code
        self.Attributes=[]
        self.Properties=[]
        self.Methods=[]
        self.Ancestors=[]
        #f = open("c://dip/s/"+name.replace(".","_").replace(":","___")+".txt","w")
        #f.write(code)
        #f.close()
        self.Code = CleanClassCode(self.Code)

    def  GetMethod(self,methodName):
        for method in self.Methods:
            if method.Name==methodName:
                return method
        return None
        
    def AddMethod(self,method):
        self.Methods.append(method)
        
    def RemoveMethod(self,methodName):
        self.Methods.remove(GetMethod(methodName))
        
    def ConvertParameterToAttribute(self,param):
        atr = Attribute()
        atr.Name=param.Name
        atr.Type = param.Type
        self.Attributes.append(atr)
        
    def __str__(self):
        print "="*70
        print "="*70
        print "======== class name >",self.Name,"="*(47-len(self.Name))
        print "="*70
        
        print "                Attributes"
        for atr in self.Attributes:
            print atr
       
        print ""
        print "                Properties"
        for prop in self.Properties:
            print prop
        print ""
        print "                  Mehods"
        for meth in self.Methods:
            print meth
        print ""
        print "="*70
        print ""
        return ""
       
    def __repr__(self):
        return self.__str__()

class ClassRegister:

    @staticmethod
    def AddClass(name,code):
        c = Class(name,code)
        ClassRegister.AddClass(c)
     
    @staticmethod
    def AddClass(cls):
        ClassRegister.ID+=1
        cls.ID=ClassRegister.ID
        ParseClassCode(cls)
        ClassRegister.Classes.append(cls)

    @staticmethod
    def GetClass(IdName):
        if len(ClassRegister.Classes)==0:
            raise ("Nie su registrovanie ziadne triedy")
        for cl in ClassRegister.Classes:
            if cl.Name==IdName or cl.ID==IdName:
                return cl
        print "Dostupne nazvy tried"
        for cl in ClassRegister.Classes:
           print "|"+cl.Name+"|"
        raise ValueError("IdName danej triedy nie je registrovane",IdName)

ClassRegister.ID=0
ClassRegister.Classes=[]

