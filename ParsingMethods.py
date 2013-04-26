#! /usr/bin/env python
# -*- coding: utf-8 -*- 

from Comment import CommentRegister
from LogicalBlock import LogicalBlock as LB

from Method import Method
from Parameter import Parameter
from Property import Property
from Attribute import Attribute
from settings import DataTypes 

from settings import LogicalBlock,StringChars,Tag,CommentChars,ClassDefinition,EndlineSeparator
from settings import EndlineSeparator
#from Class import Class,ClassRegister
from Method import Method    

def CleanCommentsAndStrings(text):
    cleanCode = text
    for strc in StringChars:
        if len(strc)!=2:
            raise ValueError('string musi mat zaciatocny a ukoncovaci znak v settings/StringChars')
        else:
            while (cleanCode.find(strc[0])!=-1):
                comnt,startP,endP =FindText(cleanCode,strc[0],strc[1])
                CommentRegister.AddComment(comnt)
                cleanCode = ReplaceAtPositons(cleanCode,Tag.format(name="Comment",idValue=str(CommentRegister.ID)),startP,endP)
    for cmt in CommentChars:
        if len(cmt)==2:
            while (cleanCode.find(cmt[0])!=-1):
                comnt,startP,endP =FindText(cleanCode,cmt[0],cmt[1])
                CommentRegister.AddComment(comnt)
                cleanCode = ReplaceAtPositons(cleanCode,Tag.format(name="Comment",idValue=str(CommentRegister.ID)),startP,endP)
        elif len(cmt)==1:
            while (cleanCode.find(cmt[0])!=-1):
                comnt,startP,endP =FindText(cleanCode,cmt[0],"\n")
                CommentRegister.AddComment(comnt)
                cleanCode = ReplaceAtPositons(cleanCode,Tag.format(name="Comment",idValue=str(CommentRegister.ID)),startP,endP-1)
        else:
            raise ValueError('nespravna hodnota v settings/CommentChars')
    return cleanCode    

def FindText(text,startchar,endchar):
    startpos=text.find(startchar)
    endpos = text[startpos+len(startchar):].find(endchar)+startpos+len(startchar)
    extracted = text[startpos:endpos+len(endchar)]
    return extracted,startpos,endpos

def ExtractText(text,startchar,endchar):
    startpos=text.find(startchar)
    endpos = text[startpos:].find(endchar)+startpos
    cleanText= text[:startpos]+text[endpos+1:]
    extracted = text[startpos:endpos+1]
    return cleanText,extracted,startpos,endpos

def ReplaceAtPositons(originalText,NewText,StartPosition,EndPosition):
    return originalText[:StartPosition]+NewText+originalText[EndPosition+1:]

def CleanLogicalBlocks (text):
    for lb in LogicalBlock:
        if len(lb)==1:
            raise NotImplemented("Tento typ logickeho bloku nie je implementovany")
        elif len(lb)==2:
            start = lb[0]
            end = lb[1]
            #if (start.find(end)==-1 and end.find(start)==-1):
            BlockIDlist=[]
            while (text.find(end)>-1):
                endPos = text.find(end)
                tmpText = text[:endPos]
                while (tmpText.find(start)>-1):
                    LB.ID+=1 # LB = LogicalBlock.LogicalBlock
                    pos = tmpText.find(start)
                    tmpText = tmpText[:pos] + Tag.format(name="LogicalBlockStart",idValue=LB.ID) + tmpText[pos+len(start):]
                    BlockIDlist.append(LB.ID)
                text = tmpText + Tag.format(name="LogicalBlockEnd",idValue=max(BlockIDlist)) + text[endPos+len(end):]
                BlockIDlist.remove(max(BlockIDlist))
        else:
            raise ValueError("Logicky blok musi mat definovanvy zaciatok")
    return text

def CleanEmptyRowsAndSpaces(inn):
    text = inn
    while (text.find("  ")>-1):
        text=text.replace("  "," ")
        text=text.replace("\t"," ")
        text=text.replace("  "," ")
        text = text.replace(" \n","\n")
        text = text.replace("\n\n","\n")
        text = text.replace("\n \n","\n")
        text = text.replace("\n\n","\n")
        text=text.replace("  "," ")
        text = text.replace("\n\n","\n")
        text=text.replace("  "," ")
        text = text.replace("  "," ")
    text=text.replace("\t"," ").replace("  "," ")
    return text
    
def ParseParameters(text):
    Parameters=[]
    text = text.replace("(","").replace(")","")
    text = text.split(",")
    for parameter in text:
        if parameter=="":
            break
        values = parameter.split()
        if len(values)==1:
            Parameters.append(Parameter(values[0],""))
        elif len(values)==2:
            Parameters.append(Parameter(values[1],values[0]))
        else:
            raise ValueError("Chyba pri parsovani parametra metody",parameter,text)
    return Parameters

def ParseMethodName(text):
    from settings import PrivateDefinition,PublicDefinition
    from settings import ProtectedDefinition,StaticDefinition
    from settings import OverrideDefinition,AbstractDefinition
    from settings import VirtualDefinition
    Parameters=[]
    original = text
    if (text.find("(")>-1):
        Parameters=ParseParameters(text[text.find("(")+1:text.find(")")])
        text = text[:text.find("(")]
    text=text+" " 
    original = text
    m  = Method()
    words = text.split()
    for word in words:
        if (word==PrivateDefinition.replace(" ","")):
            m.Private=True
            text=text.replace(word,"")
        elif (word==PublicDefinition.replace(" ","")):
            m.Public =True
            text=text.replace(word,"")
        elif (word==ProtectedDefinition.replace(" ","")):
            m.Protected=True
            text=text.replace(word,"")
        elif (word==StaticDefinition.replace(" ","")):
            m.Static=True
            text=text.replace(word,"")
        elif (word==OverrideDefinition.replace(" ","")):
            m.Override=True
            text=text.replace(word,"")
        elif (word==AbstractDefinition.replace(" ","")):
            m.Abstract=True
            text=text.replace(word,"")
        elif (word==VirtualDefinition.replace(" ","")):
            m.Virtual=True
            text=text.replace(word,"")
        elif (word in DataTypes):
            m.ReturnType=word
            text=text.replace(word,"")
            
    if len(text.split())==2:
        m.ReturnType=text.split()[0]
        m.Name=text.split()[1]
    elif len(text.split())==1:
        m.ReturnType = ""
        m.Name=text.split()[0]
    else:
        raise ValueError("nerozpoznane paramtre v nazve metody v pocte "+str(len(text.split()))+" text: ",text)
        
    m.Parameters = Parameters
    return m

def GetMethods(text):
    from settings import MethodDefinition
    Methods = []
    # MD = MethodDefinition, M = Method
    for MD in MethodDefinition: #setting.MethodDefinition
        pos = 0
        while (text[pos:].find(MD[0])>-1):
            MstartPos = text.find(MD[0])+pos
            MendPos = text[MstartPos:].find(MD[1]) + MstartPos
            i = MstartPos
            while not(text[i-1] in ["\n",EndlineSeparator,Tag.format(name="LogicalBlockEnd",idValue=0)[-1]] or i==1):
                i=i-1
           # Mname = method name
            MnameStartPos=i
            MnameEndPos=MendPos
            if (text[MnameStartPos:MnameEndPos].find("=")>-1 or text[MnameStartPos:MnameEndPos].find(EndlineSeparator)>-1 ):
                pos =text[MstartPos:].find("\n")+MstartPos
            else:
                NewMethod = ParseMethodName(text[MnameStartPos:MnameEndPos])
                # LB = LogicalBlock
                LBstartPos = text[MnameEndPos:].find(Tag.format(name="LogicalBlockStart",idValue=0)[:19]) + MnameEndPos
                LBid = text[LBstartPos:]
                LBid = LBid[LBid.find("ID=")+3:]
                LBid = LBid[:LBid.find(Tag.format(name="LogicalBlockStart",idValue=0)[-3:])]
                
                
                LBendPos = text.find(Tag.format(name="LogicalBlockEnd",idValue=str(LBid)))+len(Tag.format(name="LogicalBlockEnd",idValue=str(LBid)))
                NewMethod.Body= text[LBstartPos:LBendPos]
                Methods.append(NewMethod)
                tmp = text
                text = text[:MnameStartPos] + text[LBendPos:]
                if (len(tmp) == len (text)):
                    raise ValueError("Parsovanie triedy sposobilo chybu")
                

    return Methods,text


 
def GetAttributes(text):
    from settings import AttributeDefinition,FinalDefinition
    from settings import PrivateDefinition,PublicDefinition
    from settings import ProtectedDefinition,StaticDefinition
    text = CleanUnusedLogicalBlocks(text)
    Attributes = []
    for attributedef in AttributeDefinition:
        lines = text.split(attributedef[1])
        for line in lines:
            type = ""
            tmp_line = line.replace("\n","").replace("  "," ")
            if tmp_line.replace(" ","") =="":
                break
            for attribute in tmp_line.split(','):
                a = Attribute()
                atr = attribute
                if atr.find("=")>-1:
                    a.Value=atr[atr.find("=")+1:]
                    atr = atr[:atr.find("=")]
                for word in atr.split():
                    if (word==PrivateDefinition.replace(" ","")):
                        a.Private=True
                        atr= atr.replace(word,"")
                    elif (word==PublicDefinition.replace(" ","")):
                        a.Public =True
                        atr= atr.replace(word,"")
                    elif (word==ProtectedDefinition.replace(" ","")):
                        a.Protected=True
                        atr= atr.replace(word,"")
                    elif (word==FinalDefinition.replace(" ","")):
                        a.Final = True
                        atr=atr.replace(word,"")
                    elif (word==StaticDefinition.replace(" ","")):
                        a.Static=True
                        atr= atr.replace(word,"")
                    elif (word in DataTypes):
                        type=word
                        atr= atr.replace(word,"")
                        
                if len(atr.split())==1:
                    a.Name=atr.split()[0]
                elif len(atr.split())==2:
                    type = atr.split()[0]
                    a.Name=atr.split()[1]
                else:
                    raise ValueError("nerozpoznane paramtre v nazve atributu v pocte "+str(len(atr.split()))+" text: ",atr)
                a.Type = type
                Attributes.append(a)
        text = text.replace(line,"")
    return Attributes,text
    
def ParsePropertyName(text):
    from settings import PrivateDefinition,PublicDefinition
    from settings import ProtectedDefinition,StaticDefinition
    p = Property()
    words = text.split()
    for word in words:
        if (word==PrivateDefinition.replace(" ","")):
            p.Private=True
            text=text.replace(word,"")
        elif (word==PublicDefinition.replace(" ","")):
            p.Public =True
            text=text.replace(word,"")
        elif (word==ProtectedDefinition.replace(" ","")):
            p.Protected=True
            text=text.replace(word,"")
        elif (word==StaticDefinition.replace(" ","")):
            p.Static=True
            text=text.replace(word,"")
        elif (word in DataTypes):
            p.Type=word
            text=text.replace(word,"")    
            
    if len(text.split())==2:
        p.Type=text.split()[0]
        p.Name=text.split()[1]
    elif len(text.split())==1:
        p.Name=text.split()[0]
    else:
        raise ValueError("nerozpoznane paramtre v nazve property v pocte "+str(len(text.split()))+" text: ",text)    
    return p    
    
def CleanUnusedLogicalBlocks(text):
    pos = 0
    while text[pos:].find(Tag.format(name="LogicalBlockStart",idValue=0)[:19])>-1:
        pos = text[pos:].find(Tag.format(name="LogicalBlockStart",idValue=0)[:19])+pos
        ID = text[pos:]
        ID = ID[ID.find("=")+1:]
        ID = ID[:ID.find(Tag.format(name="LogicalBlockStart",idValue=0)[-3:])]
        if (text.find(Tag.format(name="LogicalBlockEnd",idValue=ID))==-1):
            text = text.replace(Tag.format(name="LogicalBlockStart",idValue=ID),"")
        pos+=1
    pos = 0
    while text[pos:].find(Tag.format(name="LogicalBlockEnd",idValue=0)[:19])>-1:
        pos = text[pos:].find(Tag.format(name="LogicalBlockEnd",idValue=0)[:19]) + pos
        ID = text[pos:]
        ID = ID[ID.find("=")+1:]
        ID = ID[:ID.find(Tag.format(name="LogicalBlockEnd",idValue=0)[-3:])]
        if (text.find(Tag.format(name="LogicalBlockStart",idValue=ID))==-1):
            text = text.replace(Tag.format(name="LogicalBlockEnd",idValue=ID),"")
        pos+=1
    return text.replace("  ","").replace("\n\n","\n")
    
def GetProperties(text):
        from settings import ProperyDefinition
        Properties = []
        for prop in ProperyDefinition:
            start = prop[0]
            end = prop[1]
            StartIsLogicalBlock = False
            EndIsLogicalBlock = False
            for LB in LogicalBlock:
                if start in LB:
                    StartIsLogicalBlock = True
                if end in LB:
                    EndIsLogicalBlock = True
            
            if StartIsLogicalBlock or EndIsLogicalBlock:
                pos = 0
                while text[pos:].find(Tag.format(name="LogicalBlockStart",idValue=0)[:19])>-1:
                    propStartPos = text[pos:].find(Tag.format(name="LogicalBlockStart",idValue=0)[:19])+pos
                    i = propStartPos
                    while not(text[i-1] in ["\n",Tag.format(name="LogicalBlockEnd",idValue=0)[-1],EndlineSeparator,]):
                        i-=1
                    
                    PropertyName=text[i:propStartPos]
                    if (PropertyName.find("=")>-1):
                        pos = propStartPos
                        break
                    ID = text[propStartPos:]
                    ID = ID[ID.find("=")+1:]
                    ID = ID[:ID.find(Tag.format(name="LogicalBlockStart",idValue=0)[-3:])]
                    
                    endpos = text.find(Tag.format(name="LogicalBlockEnd",idValue=ID)) + len(Tag.format(name="LogicalBlockEnd",idValue=ID))
                    
                    p = ParsePropertyName(PropertyName)
                    p.Body = text[propStartPos:endpos]
                    Properties.append(p)
                    
                    text = text[:i]+text[endpos:]
        return Properties,text
        
def CleanClassCode(text):
    text = text[text.find("\n"):]
    text = text[::1]
    text = text[text.find("\n"):]
    text = text[::1]
    return text
    
def ParseClassCode(cls):
    cls.Methods,cls.Code=GetMethods(cls.Code)
    cls.Properties,cls.Code=GetProperties(cls.Code)
    cls.Attributes,cls.Code=GetAttributes(cls.Code)
    cls.Code = CleanUnusedLogicalBlocks(cls.Code)


def ConvertLogicalBlocks(text):
    left = LogicalBlock[0][0]
    right = LogicalBlock[0][1]
    pos = 0
    while text[pos:].find(Tag.format(name="LogicalBlockStart",idValue=0)[:19])>-1:
        pos = text[pos:].find(Tag.format(name="LogicalBlockStart",idValue=0)[:19])+pos
        ID = text[pos:]
        ID = ID[ID.find("=")+1:]
        ID = ID[:ID.find(Tag.format(name="LogicalBlockStart",idValue=0)[-3:])]
        text = text.replace(Tag.format(name="LogicalBlockStart",idValue=ID),left)
        text = text.replace(Tag.format(name="LogicalBlockEnd",idValue=ID),right)
    pos = 0
    while text[pos:].find(Tag.format(name="LogicalBlockEnd",idValue=0)[:19])>-1:
        pos = text[pos:].find(Tag.format(name="LogicalBlockEnd",idValue=0)[:19]) + pos
        ID = text[pos:]
        ID = ID[ID.find("=")+1:]
        ID = ID[:ID.find(Tag.format(name="LogicalBlockEnd",idValue=0)[-3:])]
        text = text.replace(Tag.format(name="LogicalBlockStart",idValue=ID),left)
        text = text.replace(Tag.format(name="LogicalBlockEnd",idValue=ID),right)
    return text

  

def ParseNamespaceCode(NamespaceName,code):
    from Class import Class,ClassRegister
    from settings import PrivateDefinition,PublicDefinition
    from settings import ProtectedDefinition,PartialDefinition
    from settings import StaticDefinition
    tmp = code
    for CLdef in ClassDefinition: #settings.ClassDefinition
        CLstart = CLdef[0]
        CLend = CLdef[1]
        while (tmp.find(CLstart)>-1):
            CLstartPos = tmp.find(CLstart)
            CLlogBlockStartPos = tmp[CLstartPos:].find(Tag.format(name="LogicalBlockStart",idValue=0)[:19]) + CLstartPos
            CLlogBlockID=tmp[CLlogBlockStartPos:]
            CLlogBlockID = CLlogBlockID[CLlogBlockID.find("ID=")+3:]
            CLlogBlockID = CLlogBlockID[:CLlogBlockID.find(Tag.format(name="LogicalBlockStart",idValue=0)[-3:])]
            CLlogBlockEndPos = tmp.find(Tag.format(name="LogicalBlockEnd",idValue=CLlogBlockID)) + len(Tag.format(name="LogicalBlockEnd",idValue=CLlogBlockID))
            CLendPos = CLlogBlockEndPos
            i = CLstartPos
            while not(tmp[i-1] in ['\n',EndlineSeparator] or i==0):
                i=i-1
            FullClassName=tmp[i:CLlogBlockStartPos].replace(CLstart," "+NamespaceName+".").replace("\n","").replace("  "," ")
            if FullClassName[0]==" ":
                FullClassName=FullClassName[1:]
                    
            cls = Class(FullClassName,tmp[CLlogBlockStartPos:CLlogBlockEndPos])
                
            if (FullClassName.find(PrivateDefinition)>-1):
                cls.Private=True
                FullClassName = FullClassName.replace(PrivateDefinition,"")
                    
            if (FullClassName.find(PublicDefinition)>-1):
                cls.Public=True
                FullClassName = FullClassName.replace(PublicDefinition,"")
                    
            if (FullClassName.find(ProtectedDefinition)>-1):
                cls.Protected=True
                FullClassName = FullClassName.replace(ProtectedDefinition,"")
                    
            if (FullClassName.find(PartialDefinition)>-1):
                cls.Partial=True
                FullClassName = FullClassName.replace(PartialDefinition,"")
                    
            if (FullClassName.find(StaticDefinition)>-1):
                cls.Static=True
                FullClassName = FullClassName.replace(StaticDefinition,"")
                    
            if (len(FullClassName.replace(" ",""))>0):
                cls.Name = FullClassName
            
            ParseClassName(cls)
            
            ClassRegister.AddClass(cls)
                
            tmp = tmp[:i]+Tag.format(name="Class",idValue=cls.ID) + tmp[CLendPos:]    
    return tmp
 
def ParseClassName(cls):
    cls.Name=cls.Name.replace(" ","")
    return cls

from settings import *
