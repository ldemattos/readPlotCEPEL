#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  lib_readPlotCEPEL.py
#  https://github.com/ldemattos/readPlotCEPEL
#  
#  Copyright 2023 Leonardo M. N. de Mattos <l@mattos.eng.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3.0.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

def readPlotCEPEL(file):
	print(file)
	with open(file, 'r', encoding="latin-1") as f:
		
		# Ler quantidade de variáveis
		qtdvar = int(f.readline())
		print(qtdvar)

		# Ler descrição das variáveis
		vars = []
		for i in range(0,qtdvar):
			vars.append(f.readline().strip())
		print(vars)

		# Ler os dados
		i = 0
		for line in f:
			print("%s"%line)
			i+=1
			if i == qtdvar+1+6:
				break



