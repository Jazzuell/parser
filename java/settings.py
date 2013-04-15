#! /usr/bin/env python
# -*- coding: utf-8 -*- 
FileExtensions=["java","JAVA"]Spacing = "    "Template = "cshaprtemplate.txt"Datatypes = ["byte","sbyte","short","ushort","int","uint","long","ulong","float","double","decimal","char","string","bool","object"]

BeginLogicalBlock = "{"

EndLogicalBlock = "}"

ReservedWords=["abstract","event","new","struct","as","explicit","null","switch","base","extern","object","this","bool","false","operator","throw",
"break","finally","out","true","byte","fixed","override","try","case","float","params","typeof","catch","for","private","uint","char",
"foreach","protected","ulong","checked","goto","public","unchecked","class","if","readonly","unsafe","const","implicit","ref",
"ushort","continue","in","return","using","decimal","int","sbyte","virtual","default","interface","sealed","volatile","delegate",
"internal","short","void","do","is","sizeof","while","double","lock","stackalloc","else","long","static","enum","namespace","string"]

PrivateDefinition = "private"
PublicDefinition = "public"
ProtectedDefinition = "protected"
DefaultDefiniton= PrivateDefiniton
PartialDefinition = "partial"
StaticDefinition = "static"

MethodNonReturn = "void"
MethodDefinition = None
ImportDefiniton = "using"
ClassDefinition = "class"
ParameterSeparator=","
EndlineSeparator=";"
ChainCommandSeparator="."
Comment = [["//"],["/*","*/"]]