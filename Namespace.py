#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class Namespace:
    def __init__(self,name):
        self.__name = name
        self.Classes=[]
        self.Files=[]
        
    def __str__(self):
        return self.__name