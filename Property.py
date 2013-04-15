#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class Property:
    def __init__(self,name,type,short, visibility="public"):
        self.Short=short
        if not(self.Short):
            self.GetBody=""
            self.SetBody=""
        self.Name = name
        self.Type=type
        self.Visibility=visibility
    def __str__(self):
        return self.Visibility+" " + self.Type + " " + self.Name 