#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  readPlotCEPEL.py
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

import sys
from lib_readPlotCEPEL import readPlotCEPEL

def main(args):
	
	# Call the library
	df = readPlotCEPEL(sys.argv[1])
	
	# Launch ipython session
	import IPython as ipy
	ipy.embed()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
