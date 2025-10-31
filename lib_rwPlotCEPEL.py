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

import pandas as pd

def readPlotCEPEL(file_in):

	# Ler o o arquivo PLT
	with open(file_in, 'r', encoding="latin-1") as f:
		
		# Ler quantidade de variáveis
		qtdvar = int(f.readline())

		# Ler descrição das variáveis
		vars = []
		for i in range(0,qtdvar):
			vars.append(f.readline().strip())

		# Ler resultados na memória, como string		
		dados = f.read()
			
	# Processar os resultados, gerando uma lista de strings
	dados = dados.replace('\n','').strip().split(' ')

	# Organizar os resultados em lista de listas, para formato adequado ao Pandas
	dadoslst = []
	for i in range(0,len(dados),qtdvar):
		dadoslst.append( [float(dados[i+j]) for j in range(0,qtdvar)] )

	return(pd.DataFrame(data=dadoslst,columns=vars))
	
def writePlotCEPEL(file_out,df,var=[]):
	
	if len(var) == 0:
		var = df.columns
		
	# Abrir arquivo para escrita
	with open(file_out, 'w+', encoding="latin-1") as f:
		
		# Escrever quantidade de variáveis
		f.write("%i\n"%len(var))
		
		# Listar variáveis
		print(var)
		for i in var:
			f.write("%s\n"%i)			
		
		dadoslst = df[var].to_numpy().flatten()
		for i in range(0,len(dadoslst)+1,6):			
			file_row = ' '.join(map(str, dadoslst[i:i+6]))
			f.write(" %s\n"%file_row)
			
	return(0)