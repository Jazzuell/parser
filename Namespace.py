#! /usr/bin/env python
# -*- coding: utf-8 -*- 
from Class import Class,ClassRegister
from ParsingMethods import ParseNamespaceCode
from settings import *

class Namespace:
    def __init__(self,name,code):
        self.Name = name
        self.Files=[]
        self.Code = ParseNamespaceCode(self.Name,code)

    def __str__(self):
        return self.Name
        
    def __repr__(self):
        return self.__str__()        