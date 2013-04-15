#! /usr/bin/env python
# -*- coding: utf-8 -*- 
FileExtensions=["py","PY"]Spacing = "    "Template = "cshaprtemplate.txt"Datatypes = ["byte","sbyte","short","ushort","int","uint","long","ulong","float","double","decimal","char","string","bool","object"]

ReservedWords=["abstract","event","new","struct","as","explicit","null","switch","base","extern","object","this","bool","false","operator","throw",
"break","finally","out","true","byte","fixed","override","try","case","float","params","typeof","catch","for","private","uint","char",
"foreach","protected","ulong","checked","goto","public","unchecked","class","if","readonly","unsafe","const","implicit","ref",
"ushort","continue","in","return","using","decimal","int","sbyte","virtual","default","interface","sealed","volatile","delegate",
"internal","short","void","do","is","sizeof","while","double","lock","stackalloc","else","long","static","enum","namespace","string"]

PrivateDefinition = "_"
PublicDefinition = ""
ProtectedDefinition = ""
DefaultDefiniton= PublicDefinition
PartialDefinition = ""
StaticDefinition = "@static\n"

MethodNonReturn = None
MethodDefinition = [["def","):"],]
ImportDefiniton = [["from","\n"],["import","\n"],]
LogicalBlock = [[":\n",],]
ClassDefinition = "class"
ParameterSeparator=","
EndlineSeparator=";"
ChainCommandSeparator="."
Comment = [["//"],["/*","*/"]]