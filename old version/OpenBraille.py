"""
 * OpenBraille.py -- Programa traductor de ascii a braille y controlado de impresora braille casera.
 * Copyright (C) 2014  Pablo Luis Araujo
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU gv; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 *
 *   Author: Pablo Luis Araujo          Analista Programador Universitario
 *   Email: araujopablo1994@gmail.com
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time  
from Tkinter import *
from tkFileDialog import askopenfilename
from Motor import *
from traductor import *
import pickle
import os

def valorImp(cof):
	print("hola")
			
def imprimir(v0,conf):
	l1=[]
	aux3=0
	aux2=0
	opt = {'defaultextension':'.jpg','filetypes' : [('Texto', '*.txt')]}
	archivo= askopenfilename(**opt)
	archi = open(archivo,"r")
	v2=Toplevel(v0)
	v2.title("Por favor Espere")
	if(test(archi)):
		v2=Label(v2,text="Imprimiendo ...") 
		v2.grid(row=0,column=1)
		tomarP(conf)
		conf[open]=True
		archi.seek(0)
		l1=procesar(archi,conf)
		for linea in l1:
			AvansarSMCC_D(conf)
			linea.reverse()
			cantCarac=conf["CantCar"]
			cantCaracL=(len(linea)/2)
			l=[]
			while(cantCaracL < cantCarac):
				for i in range (0,8):
					l.append(0)
				cantCaracL=cantCaracL+1
			l.extend(linea)
			inicializar(conf)
			print ("Linea1: ",l,"\n")
			for pt in l:
				if(pt == 1):
					aux3=0
					aux2=0
					EIman(conf)
					aux2=SL(conf)
					moverSL(conf)
					for i in range(0,4):
						time.sleep(0.05)
						aux3=SL(conf)
						if(aux2 == aux3):
							moverSL(conf)
				else:
					aux3=0
					aux2=0
					aux2=SL(conf)
					moverSL(conf)
					for i in range(0,4):
						time.sleep(0.05)
						aux3=SL(conf)
						if(aux2 == aux3):
							moverSL(conf)
				pinguino.analogWrite(12,conf["pwm"])
				pinguino.analogWrite(11,conf["pwm"])
			AvansarSMPP_D(conf)
		AvansarSMCC_D(conf)
		sacarPapel(conf)
	else:
		v2=Label(v2,text="El archivo contiene caracteres no reconocidos") 
		v2.grid(row=0,column=1)

#--------------------------------------------Interface----------------------------------------------------

def readme():
	os.startfile("Leeme.txt")

#Abre el Leeme	
	
def ayuda():
	print("ayuda")
	
#Destruye la ventana que lo llamo	
	
def salir(v0):
	v0.destroy

#Muestra una ventana con un aviso, informando que se cambio el formato del archivo		
		
def aviso():
	v1=Tk()
	b1=Button(v1,text="ABRIR el Nuevo formato",command=lambda:os.startfile("temp.txt") )
	b1.pack()
	v1.title("Aviso Importante")
	v1.geometry("300x40")
	v1.resizable(0,0)
	v1.mainloop()

def tiempoPulso(entry,entry2,entry3,entry4,entry5,conf):	
	conf["CantCar"]=entry.get()
	conf["TiempoEntreBobina"]=entry2.get()
	conf["TMCC"]=entry3.get()
	conf["TSL"]=entry4.get()
	conf["TiempoEi"]=entry5.get()
		
def confMotor(entry,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,conf):
	conf["MPPA"]=entry.get()
	conf["MPPB"]=entry2.get()
	conf["MPPC"]=entry3.get()
	conf["MPPD"]=entry4.get()
	conf["MCCA"]=entry5.get()
	conf["MCCB"]=entry6.get()
	conf["Electro"]=entry7.get()	
	conf["SMCC_I"]=entry8.get()
	conf["SMCC_D"]=entry9.get()
	conf["SL"]=entry10.get()	
	conf["SH"]=entry11.get()	

def centrar(ventana):
    ventana.update_idletasks()
    w=ventana.winfo_width()
    h=ventana.winfo_height()
    extraW=ventana.winfo_screenwidth()-w
    extraH=ventana.winfo_screenheight()-h
    ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))

def propiedadesImpresion(v0,conf):
	v2=Toplevel(v0)
	
	l1=Label(v2,text="Cantidad de caracteres por Hoja") 
	l1.grid(row=0,column=1)
	entry = Entry(v2,justify=CENTER)
	entry.grid(row=2, column=1)
	entry.insert(0,conf["CantCar"])

	l1=Label(v2,text="Tiempo entre cada pulso entre las bobinas del MPP") 
	l1.grid(row=3,column=1)
	entry2 = Entry(v2,justify=CENTER)
	entry2.grid(row=4, column=1)
	entry2.insert(0,conf["TiempoEntreBobina"])
	
	l1=Label(v2,text="Tiempo entre cada pulso del MCC") 
	l1.grid(row=5,column=1)
	entry3 = Entry(v2,justify=CENTER)
	entry3.grid(row=6, column=1)
	entry3.insert(0,conf["TMCC"])
	
	l1=Label(v2,text="Tiempo entre cada pulso del MCC para la lectura del Sensor de linea") 
	l1.grid(row=7,column=1)
	entry4 = Entry(v2,justify=CENTER)
	entry4.grid(row=8, column=1)
	entry4.insert(0,conf["TSL"])
	
	l1=Label(v2,text="Tiempo entre cada pulso del Electro Iman") 
	l1.grid(row=9,column=1)
	entry5 = Entry(v2,justify=CENTER)
	entry5.grid(row=10, column=1)
	entry5.insert(0,conf["TiempoEi"])
	
	b1=Button(v2,text="Aceptar",command=lambda:tiempoPulso(entry,entry2,entry3,entry4,entry5,conf) )
	b1.grid(row=12,column=1)
	b2=Button(v2,text="Ayuda",command=lambda:readme() )
	b2.grid(row=12,column=2)
	
	v2.title("Configuración")
	v2.geometry("480x280")
	v2.resizable(0,0)
	centrar(v2)
	v2.mainloop()

def propiedadesImpresora(v0,conf):
	v2=Toplevel(v0)
	l1=Label(v2,text="MPP Bobina A") 
	l1.grid(row=0,column=1)
	entry = Entry(v2,justify=CENTER)
	entry.grid(row=2, column=1)
	entry.insert(0,conf["MPPA"])

	l1=Label(v2,text="MPP Bobina B") 
	l1.grid(row=0,column=2)
	entry2 = Entry(v2,justify=CENTER)
	entry2.grid(row=2, column=2)
	entry2.insert(0,conf["MPPB"])
	
	l1=Label(v2,text="MPP Bobina C") 
	l1.grid(row=0,column=3)
	entry3 = Entry(v2,justify=CENTER)
	entry3.grid(row=2, column=3)
	entry3.insert(0,conf["MPPC"])
	
	l1=Label(v2,text="MPP Bobina D") 
	l1.grid(row=0,column=4)
	entry4 = Entry(v2,justify=CENTER)
	entry4.grid(row=2, column=4)
	entry4.insert(0,conf["MPPD"])
	
	l1=Label(v2,text="MCC Bobina A") 
	l1.grid(row=3,column=1)
	entry5 = Entry(v2,justify=CENTER)
	entry5.grid(row=4, column=1)
	entry5.insert(0,conf["MCCA"])
	
	l1=Label(v2,text="MCC Bobina B") 
	l1.grid(row=3,column=2)
	entry6 = Entry(v2,justify=CENTER)
	entry6.grid(row=4, column=2)
	entry6.insert(0,conf["MCCB"])
	
	l1=Label(v2,text="Electroiman") 
	l1.grid(row=5,column=1)
	entry7 = Entry(v2,justify=CENTER)
	entry7.grid(row=6, column=1)
	entry7.insert(0,conf["Electro"])
	
	l1=Label(v2,text="Sensor Izquierdo") 
	l1.grid(row=7,column=1)
	entry8 = Entry(v2,justify=CENTER)
	entry8.grid(row=8, column=1)
	entry8.insert(0,conf["SMCC_I"])
	
	l1=Label(v2,text="Sensor Derecho") 
	l1.grid(row=7,column=2)
	entry9 = Entry(v2,justify=CENTER)
	entry9.grid(row=8, column=2)
	entry9.insert(0,conf["SMCC_D"])
	
	l1=Label(v2,text="Sensor de Linea") 
	l1.grid(row=7,column=3)
	entry10 = Entry(v2,justify=CENTER)
	entry10.grid(row=8, column=3)
	entry10.insert(0,conf["SL"])
	
	l1=Label(v2,text="Sensor de Hoja") 
	l1.grid(row=7,column=4)
	entry11 = Entry(v2,justify=CENTER)
	entry11.grid(row=8, column=4)
	entry11.insert(0,conf["SH"])
	
	l1=Label(v2,text="Para todos\nLos valores validos son\n 0,1,2,3,4,5,6,7") 
	l1.grid(row=10,column=1)
	b1=Button(v2,text="Aceptar",command=lambda:confMotor(entry,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,conf) )
	b1.grid(row=11,column=1)
	b2=Button(v2,text="Ayuda",command=lambda:readme() )
	b2.grid(row=11,column=2)
	v2.title("Configuración")
	v2.geometry("700x300")
	v2.resizable(0,0)
	centrar(v2)
	v2.mainloop()
	
	
def testear(v0,conf):
	v3=Toplevel(v0)
	v3.title("Test")
	b1=Button(v3,text="Avanza MCC hasta Sensor Derecho",command=lambda:AvansarSMCC_D(conf) )
	b1.grid(row=1,column=1)
	b2=Button(v3,text="Avanza MCC hasta Sensor Izquierdo",command=lambda:AvansarSMCC_I(conf) )
	b2.grid(row=1,column=2)
	b1=Button(v3,text="Gira MPP hacia derecha",command=lambda:AvansarSMPP_D(conf) )
	b1.grid(row=2,column=1)
	b2=Button(v3,text="Gira MPP hacia Izquierda",command=lambda:AvansarSMPP_I(conf) )
	b2.grid(row=2,column=2)
	b2=Button(v3,text="Parar",command=lambda:parar() )
	b2.grid(row=3,column=1)
	b2=Button(v3,text="Tomar Papel",command=lambda:tomarP(conf) )
	b2.grid(row=4,column=1)
	b2=Button(v3,text="Pulso electro iman",command=lambda:EIman(conf) )
	b2.grid(row=4,column=2)
	b2=Button(v3,text="Mover derecha MCC",command=lambda:AvansarSMCC_D2(conf) )
	b2.grid(row=5,column=1)
	b2=Button(v3,text="Mover izquierda MCC",command=lambda:AvansarSMCC_I2(conf) )
	b2.grid(row=5,column=2)
	b2=Button(v3,text="punto",command=lambda:punto(conf))
	b2.grid(row=6,column=1)
	b2=Button(v3,text="sacar Hoja",command=lambda:sacarPapel(conf))
	b2.grid(row=6,column=2)
	b2=Button(v3,text="sacar Hoja2",command=lambda:sacarPapel2(conf))
	b2.grid(row=6,column=3)
	b2=Button(v3,text="Mpp bobina a y b",command=lambda:mppAyB(conf))
	b2.grid(row=7,column=1)
	b2=Button(v3,text="Mpp bobina a y c",command=lambda:mppAyC(conf))
	b2.grid(row=7,column=2)
	b2=Button(v3,text="Mpp bobina a y d",command=lambda:mppAyD(conf))
	b2.grid(row=7,column=3)
	b2=Button(v3,text="Mpp bobina a",command=lambda:mppA(conf))
	b2.grid(row=7,column=4)
	b2=Button(v3,text="Sensor derecho",command=lambda:testSMCC_D(conf) )
	b2.grid(row=8,column=1)
	b2=Button(v3,text="Sensor izquierdo",command=lambda:testSMCC_I(conf))
	b2.grid(row=8,column=2)
	b2=Button(v3,text="Sensor de linea",command=lambda:testSL(conf))
	b2.grid(row=8,column=3)
	b2=Button(v3,text="Sensor de linea2",command=lambda:SL(conf))
	b2.grid(row=8,column=4)
	b2=Button(v3,text="Inicializar",command=lambda:inicializar(conf))
	b2.grid(row=8,column=5)
	l1=Label(v3,text="POR FAVOR ESPERE ...") 
	l1.grid(row=9,column=1)	
	centrar(v3)
	v3.mainloop()

def imprimirMain(v0,conf):
	v3=Toplevel(v0)
	v3.title("Imprimir")
	b1=Button(v3,text="Imprimir",command=lambda:imprimir(v0,conf) )
	b1.grid(row=1,column=1)
	b2=Button(v3,text="Testear",command=lambda:testear(v0,conf) )
	b2.grid(row=1,column=2)
	centrar(v3)
	v3.mainloop()
	
def creditos(v0):
	v3=Toplevel(v0)
	v3.title("Contacto")
	l1=Label(v3,text="Integrantes:\n\nPablo Luis Araujo\nSergio Oscar Fauez\nSebastian Suarez Cores") 
	l1.grid(row=0,column=1)
	l1=Label(v3,text="Universidad Nacional de La Plata\nFacultad de Informática") 
	l1.grid(row=1,column=1)
	v3.resizable(0,0)
	centrar(v3)	
	v3.mainloop()

def contacto(v0):
	v3=Toplevel(v0)
	v3.title("Contacto")
	l1=Label(v3,text="Email: araujopablo1994@gmail.com") 
	l1.grid(row=0,column=1)
	centrar(v3)	 
	v3.mainloop()

def menuPrincipal ():
	#0.028
	configuracion={"TiempoEntreBobina":4.5,"pwm":"770","anchoCarroIzq":50,"TMCC":25.0,"TSL":150,"CantCar":10,"MPPA":4,"MPPB":5,"MPPC":3,"MPPD":6,"MCCA":2,"MCCB":1,"Electro":0,"TiempoEi":0.030,"valorbase":450,"velosidadMCC":1,"pwmMCC":12,"TiempoEiZ":0.5,"SMCC_D":10,"SMCC_I":7,"SL":13,"SH":4}
	
	v0=Tk() 
	
	imagen1=PhotoImage(file="img.gif") 
	label1 = Label(v0, image=imagen1) 
	label1.grid(row=1,column=1)
	
	menu1 = Menu(v0) 
	v0.config(menu=menu1) 
	
	menu1_1 = Menu(menu1, tearoff=0) 
	menu1.add_cascade(label="Inicio", menu=menu1_1)  
	menu1_1.add_command(label="Salir",command=salir(v0))
	
	menu1_2 = Menu(menu1, tearoff=0) 
	menu1.add_command(label="Imprimir", command=lambda: imprimirMain(v0,configuracion)) 
	
	menu1_3 = Menu(menu1, tearoff=0) 
	menu1.add_cascade(label="Configuración", menu=menu1_3) 
	menu1_3.add_command(label="Propiedades de Impresion",command=lambda: propiedadesImpresion(v0,configuracion)) 
	menu1_3.add_command(label="Propiedades de los Impresora",command=lambda: propiedadesImpresora(v0,configuracion)) 
	menu1_3.add_command(label="Testear",command=lambda: testear(v0,configuracion)) 
	
	menu1_4 = Menu(menu1, tearoff=0) 
	menu1.add_cascade(label="Ayuda", menu=menu1_4) 
	menu1_4.add_command(label="Readme",command=lambda: readme(v0)) 
	menu1_4.add_command(label="Creditos",command=lambda: creditos(v0))
	menu1_4.add_command(label="Contacto",command=lambda: contacto(v0))
	
	v0.resizable(0,0)
	v0.title("Impresora Braille")
	centrar(v0)
	v0.mainloop()
	
menuPrincipal()


