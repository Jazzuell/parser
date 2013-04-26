#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# setting fo Java

LanguageName="Java"

FileExtensions=["java","JAVA"]

Tag = "<§{name} ID={idValue}§>"

Spacing = "    "

Template = "cshaprtemplate.txt"

DataTypes = ["byte","sbyte","short","ushort","int","uint","long","ulong","float","double","decimal","char","string","bool","object"]


ReservedWords=["abstract","event","new","struct","as","explicit","null","switch","base","extern","object","this","bool","false","operator","throw",
"break","finally","out","true","byte","fixed","override","try","case","float","params","typeof","catch","for","private","uint","char",
"foreach","protected","ulong","checked","goto","public","unchecked","class","if","readonly","unsafe","const","implicit","ref",
"ushort","continue","in","return","using","decimal","int","sbyte","virtual","default","interface","sealed","volatile","delegate",
"internal","short","void","do","is","sizeof","while","double","lock","stackalloc","else","long","static","enum","namespace","string"]

PrivateDefinition = "private "
PublicDefinition = "public "
ProtectedDefinition = "protected "
DefaultDefiniton= PrivateDefinition
PartialDefinition = "partial "
StaticDefinition = "static "
OverrideDefinition = "override "
AbstractDefinition = "abstract "
VirtualDefinition = "virtual "
FinalDefinition = "final "

ClassDefinition = [[" class ",Tag.format(name="LogicalBlockStart",idValue=0)[:19]],]
NamespaceDefinition = [["namespace",],]
ParameterSeparator=","
EndlineSeparator=";"
ChainCommandSeparator="."
CommentChars = [["//",],["/*","*/"]]
StringChars = [['"','"'],["'","'"]]
LogicalBlock=[["{","}"],]

MethodNonReturn = "void"
MethodDefinition = [["(",Tag.format(name="LogicalBlockStart",idValue=0)[:19]],]
ProperyDefinition = [["{","}"],]
AttributeDefinition = [["\n",";"],]
ImportDefiniton = [["import",";"],]

def ParseClassName(cls):
    name = cls.Name
    if name.find(" implements ")>-1:
        anc = name[name.find(" implements ")+12:]
        anc = anc[:anc.find(" ")]
        cls.Ancestors.append(anc)
        name = name.replace(" implements ","").replace(anc,"")
        
    if name.find(" extends ")>-1:
        anc = name[name.find(" extends ")+12:]
        anc = anc[:anc.find(" ")]
        cls.Ancestors.append(anc)
        name = name.replace(" extends ","").replace(anc,"")
    cls.Name = name.replace(" ","").replace("\t","").replace("\r","")
    return cls