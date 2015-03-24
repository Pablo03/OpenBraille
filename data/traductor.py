"""
	traductor.py -- Programa traductor de ascii a braille.
	Copyright (C) 2014  Pablo Luis Araujo
 
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with GNU gv; see the file COPYING.  If not, write to
	the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
	Boston, MA 02111-1307, USA.

	Author: Pablo Luis Araujo          Analista Programador Universitario
	Email: araujopablo1994@gmail.com
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Traductor(object):
	
	def __init__(self):
		super(PynguinoBase, self).__init__()
		
		self.lista=[[],[],[]]
		
		#Diccionario de los Numeros	
		self.dicNum = {"0":(0,1,1,1,0,0,0),"1":(1,0,0,0,0,0,0),"2":(1,0,1,0,0,0,0),"3":(1,1,0,0,0,0,0),"4":(1,1,0,1,0,0,0),"5":(1,0,0,1,0,0,0),"6":(1,1,1,0,0,0,0),"7":(1,1,1,1,0,0,0),"8":(1,0,1,1,0,0,0),"9":(0,0,1,1,0,0,0),"num":(0,1,0,1,1,1,1)}
		
		#Diccionario de las Minusculas	
		self.dicMin = {"a":(1,0,0,0,0,0,0),"b":(1,0,1,0,0,0,0),"c":(1,1,0,0,0,0,0),"d":(1,1,0,1,0,0,0),"e":(1,0,0,1,0,0,0),"f":(1,1,1,0,0,0,0),"g":(1,1,1,1,0,0,0),"h":(1,0,1,1,0,0,0),"i":(0,1,1,0,0,0,0),"j":(0,1,1,1,0,0,0),"k":(1,0,0,0,1,0,0),"l":(1,0,1,0,1,0,0),"m":(1,1,0,0,1,0,0),"n":(1,1,0,1,1,0,0),"ñ":(1,0,0,1,1,0,0),"o":(1,0,0,1,1,0,0),"p":(1,1,1,0,1,0,0),"q":(1,1,1,1,1,0,0),"r":(1,0,1,1,1,0,0),"s":(0,1,1,0,1,0,0),"t":(0,1,1,1,1,0,0),"v":(1,0,1,0,1,1,0),"u":(1,0,0,0,1,1,0),"w":(0,1,1,1,0,1,0),"y":(1,1,0,1,1,1,0),"x":(1,1,0,0,1,1,0),"z":(1,0,0,1,1,1,0),"á":(1),"é":(1),"í":(1),"ó":(1),"ú":(1)}
		
		#Diccionario de las Mayusculas	
		self.dicMay = {"A":(1,0,0,0,0,0,0),"B":(1,0,0,0,0,0,0),"C":(1,0,0,0,0,0,0),"D":(1,1,0,1,0,0,0),"E":(1,0,0,1,0,0,0),"F":(1,1,1,0,0,0,0),"G":(1,1,1,1,0,0,0),"H":(1,0,1,1,0,0,0),"I":(0,1,1,0,0,0,0),"J":(0,1,1,1,0,0,0),"K":(1,0,0,0,1,0,0),"L":(1,0,1,0,1,0,0),"M":(1,1,0,0,1,0,0),"N":(1,1,0,1,1,0,0),"Ñ":(),"O":(1,0,0,1,1,0,0),"P":(1,1,1,0,1,0,0),"Q":(1,1,1,1,1,0,0),"R":(1,0,1,1,1,0,0),"S":(0,1,1,0,1,0,0),"T":(0,1,1,1,1,0,0),"V":(1,0,0,0,1,1,0),"U":(1,0,1,0,1,1,0),"W":(0,1,1,1,0,1,0),"Y":(1,1,0,1,1,1,0),"X":(1,1,0,0,1,1,0),"Z":(1,0,0,1,1,1,0),"Á":(1),"É":(1),"Í":(1),"Ó":(1),"Ú":(1),"Mayus":(0,1,0,0,0,1,1)}	
		
		#Diccionario de los otros caracteres		
		self.otros = {".":(1),":":(1,0,0,0,0,0,0),";":(1,0,0,0,0,0,0),",":(1,0,0,0,0,0,0),"?":(1,0,0,0,0,0,0),"¿":(1,0,0,0,0,0,0),"(":(1,0,0,0,0,0,0),")":(1,0,0,0,0,0,0),"!":(1,0,0,0,0,0,0),"¡":(1,0,0,0,0,0,0),'"':(1,0,0,0,0,0,0),"-":(1,0,0,0,0,0,0),"\n":(1,0,0,0,0,0,0),"\r":(1,0,0,0,0,0,0),"\t":(1,0,0,0,0,0,0),"\0":(1,0,0,0,0,0,0),"/":(1,0,0,0,0,0,0)," ":(1,0,0,0,0,0,0),"":(1,0,0,0,0,0,0),"#":(1,0,0,0,0,0,0),"_":(1,0,0,0,0,0,0),"[":(1,0,0,0,0,0,0),"]":(1,0,0,0,0,0,0)," ":(0,0,0,0,0,0,0)}
		
		
	#Testea Si el documento tiene caracteres validos para imprimir	
	def test(self,arc):
		ok=True
		for linea in arc:
			i=0
			while i < len(linea):
				if(not((self.dicMin.has_key(linea[i]))or(self.dicMay.has_key(linea[i]))or(self.dicNum.has_key(linea[i]))or(self.otros.has_key(linea[i])))):
					ok=False
					print (linea[i],"\tNo reconocido")
				i=i+1
		#aviso()
		return ok
		
	#Inserta en la listas para imprimir los puntos		
	def insertar (self,tup):
		self.lista[0].append(tup[0])
		self.lista[0].append(tup[1])
		self.lista[1].append(tup[2])
		self.lista[1].append(tup[3])
		self.lista[2].append(tup[4])
		self.lista[2].append(tup[5])
		self.lista[0].append(tup[6])
		self.lista[1].append(tup[6])
		self.lista[2].append(tup[6])
		
	#Cuenta la cantidad de caracteres				
	def cantCar(self,s,num):
		if(len(s)<num):
			return True
		else:
			return False
	
	#Lee el caracter y lo busca en el diccionario para agregarlo	
	def cargarLista(self,car):
		if(self.dicMin.has_key(car)):
			self.insertar(self.dicMin[car])
		elif(self.dicMay.has_key(car)):
			self.insertar(self.dicMay["Mayus"])
			self.insertar(self.dicMay[car])
		elif(self.dicNum.has_key(car)):
			self.insertar(self.dicNum["num"])
			self.insertar(self.dicNum[car])
		elif(self.otros.has_key(car)):
			self.insertar(self.otros[car])
	
	#Devuelve el contenido de la lista
	def getLista(self):
		return self.lista
		
	#Procesa el texto a imprimir, convirtiendolo en una lista de unos y ceros					
	def procesar(self,archi,conf):
		cantCarac=conf["CantCar"]
		for linea in archi:
			if(len(linea)<cantCarac):
				i=0
				car=""
				while i < len(linea):
					print ("Entro while")
					car=car+linea[i]
					self.cargarLista(linea[i])
					i+=1
			else:
				i=0
				while (i < len(linea)):
					i2=0
					car=""
					while(i2 <cantCarac)and(i < len(linea)):
						print("Entro al otro while")
						self.cargarLista(linea[i])
						car=car+linea[i]
						i2+=1
						i+=1
					i+=1
		print ("Salio del procesar")
		return self.getLista()
	
