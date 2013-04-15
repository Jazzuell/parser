#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class Attribute:
    def __init__(self,name,type,visibility="private"):
        self.Name = name
        self.Type=type
        self.Visibility=visibility
    def __str__(self):
        return self.Visibility+" " + self.Type + " " + self.Name 