#! /usr/bin/env python
# -*- coding: utf-8 -*- 

class Comment:
    def __init__(self,id,text):
        self.ID=id
        self.Text=text
        
        def __str__(self):
            return Text
            
        def __repr__(self):
            return self.__str__()        

class CommentRegister:
    @staticmethod
    def AddComment(Text):
        CommentRegister.ID+=1
        CommentRegister.Comments.append(Comment(CommentRegister.ID,Text))

    @staticmethod
    def GetComment(ID):
        for comnt in CommentRegister.Comments:
            if comnt.ID==ID:
                return comnt
                
CommentRegister.ID = 0
CommentRegister.Comments=[]