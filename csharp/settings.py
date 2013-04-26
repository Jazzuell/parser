#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# setting fo C#

LanguageName="C#"
FileExtensions=["cs","CS"]
Tag = "<§{name} ID={idValue}§>"
Spacing = "    "Template = "cshaprtemplate.txt"DataTypes = ["byte","sbyte","short","ushort","int","uint","long","ulong","float","double",
                    "decimal","char","string","bool","object"]

ReservedWords=["abstract","event","new","struct","as","explicit","null","switch","base",
                            "extern","object","this","bool","false","operator","throw",
                            "break","finally","out","true","byte","fixed","override","try",
                            "case","float","params","typeof","catch","for","private","uint","char",
                            "foreach","protected","ulong","checked","goto","public","unchecked",
                            "class","if","readonly","unsafe","const","implicit","ref",
                            "ushort","continue","in","return","using","decimal","int","sbyte","virtual",
                            "default","interface","sealed","volatile","delegate",
                            "internal","short","void","do","is","sizeof","while","double","lock","stackalloc",
                            "else","long","static","enum","namespace","string"]

DataTypes=["int","integer","string","String","char","void","List","double","float","bool"]

PrivateDefinition = "private "
PublicDefinition = "public "
ProtectedDefinition = "protected "
DefaultDefiniton= PrivateDefinition
PartialDefinition = "partial "
StaticDefinition = "static "
OverrideDefinition = "override "
AbstractDefinition = "abstract "
VirtualDefinition = "virtual "
FinalDefinition = ""

ClassDefinition = [[" class ",")"],]
NamespaceDefinition = [["namespace",],]
ParameterSeparator=","
EndlineSeparator=";"
ChainCommandSeparator="."
CommentChars = [["//",],["/*","*/"]]
StringChars = [['"','"'],["'","'"]]
LogicalBlock=[["{","}"],]

MethodNonReturn = "void"
MethodDefinition = [["(","\n"],]
ProperyDefinition = [["{","}"],]
AttributeDefinition = [["\n",";"],]
ImportDefiniton = [["using",";"],]