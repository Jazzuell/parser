#! /usr/bin/env python
# -*- coding: utf-8 -*- 

from Class import ClassRegister

def FindClass(className):
    return ClassRegister.GetClass(className)

def MoveMethod(cls1Name,cls2Name,methodName):
    cls1 = FindClass(cls1Name)
    cls2 = FindClass(cls2Name)
    cls2.AddMethod(cls1.GetMethod(methodName))
    cls1.RemoveMethod(methodName)
    
def RenameMethod(clsName,methodName,newName):
    cls = FindClass(clsName)
    method = cls.GetMethod(methodName)
    if cls.GetMethod(newName):
        raise ValueError("metoda s nazvom ",newName,"uz je v triede",clsName,"definovana")
    method.Name=newName
    
def ChangeClassName(clsName,newName):
    if ClassRegister.GetClass(newName):
        raise ValueError("trieda s nazvom ",newName," uz je v danom mennom prietore definovana")
    cls = ClassRegister.GetClass(clsName)
    cls.Name=newName
     
def ConvertParameterToAttribute(clsName,methodName,parameterName):
    cls = ClassRegister.GetClass(clsName)
    method = cls.GetMethod(methodName)
    param = method.GetParameter(parameterName)
    method.RemoveParameter(parameterName)
    cls.ConvertParameterToAttribute(param)