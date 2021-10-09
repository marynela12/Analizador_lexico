#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author:
"""

import AnalizadorLexico

l=AnalizadorLexico.AnalizadorLexico("programa.txt")

l.crearLista()

t=l.obtenerToken()
while t != None:
    print("Token: ",t)
    t=l.obtenerToken()
