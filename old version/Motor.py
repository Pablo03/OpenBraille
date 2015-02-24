"""
 * Motor.py 
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
#-*- coding: utf-8 -*-

import time
from pusb import *
from Tkinter import *		
try:
	pinguino = PynguinoUSB(vboot="v4")
	for i in range(0,7):
		pinguino.pinMode(i,"OUTPUT")
	pinguino.pinMode(7,"INPUT")
	pinguino.pinMode(10,"INPUT")
except Exception:
	v0=Tk()
	v0.title("ERROR")
	l1=Label(v0,text='El Hardware "NO" esta conectado') 
	l1.grid(row=0,column=1)
	v0.update_idletasks()
	w=v0.winfo_width()
	h=v0.winfo_height()
	extraW=v0.winfo_screenwidth()-w
	extraH=v0.winfo_screenheight()-h
	v0.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))	 
	v0.mainloop()	
#770
def enviar(puerto,num):
	if(num==1):
		pinguino.digitalWrite(puerto, "HIGH")
	else:
		pinguino.digitalWrite(puerto, "LOW")
	
def leer(puerto):
	return (pinguino.digitalRead(puerto))

def parar():
	for i in range(0,8):
		pinguino.digitalWrite(i, "LOW")
#Mueve el motor paso a paso hacia la derecha 

def moverMpp_D(conf):
	t=(conf["TiempoEntreBobina"] / 1000)
	enviar(conf["MPPD"],0)
	enviar(conf["MPPA"],1)
	time.sleep(t)
	enviar(conf["MPPA"],0)
	enviar(conf["MPPB"],1)
	time.sleep(t)
	enviar(conf["MPPB"],0)
	enviar(conf["MPPC"],1)
	time.sleep(t)
	enviar(conf["MPPC"],0)
	enviar(conf["MPPD"],1)
	time.sleep(t)
	enviar(conf["MPPD"],0)

#Mueve el motor paso a paso hacia la izquierda

def moverMpp_I(conf):
	t=(conf["TiempoEntreBobina"] / 1000)
	enviar(conf["MPPB"],0)
	enviar(conf["MPPA"],1)
	time.sleep(t)
	enviar(conf["MPPA"],0)
	enviar(conf["MPPD"],1)	
	time.sleep(t)
	enviar(conf["MPPD"],0)
	enviar(conf["MPPC"],1)
	time.sleep(t)
	enviar(conf["MPPC"],0)
	enviar(conf["MPPB"],1)
	time.sleep(t)
	enviar(conf["MPPB"],0)

#Mueve el motor corriente continua hacia la derecha 
		
def moverMc_D(conf):
	enviar(conf["MCCB"],1)
	
#Mueve el motor corriente continua hacia la izquierda	
	
def moverMc_I(conf):
	enviar(conf["MCCA"],1)
		
#Realiza un Punto con el electroIman

def moverSL(conf):
	pinguino.analogWrite(12,conf["pwm"])
	pinguino.analogWrite(11,conf["pwm"])	
	if(SL(conf)== 1):
		while(SL(conf)== 1):
			enviar(conf["MCCB"],1)
	else:
		while(SL(conf)== 0):
			enviar(conf["MCCB"],1)
	enviar(conf["MCCB"],0)

def EIman(conf):
	pinguino.analogWrite(12,"1023")
	pinguino.analogWrite(11,"1023")
	enviar(conf["Electro"],1)
	time.sleep(conf["TiempoEi"])
	enviar(conf["Electro"],0)
	time.sleep(conf["TiempoEiZ"])
	pinguino.analogWrite(12,conf["pwm"])
	pinguino.analogWrite(11,conf["pwm"])
	
def SMCC_D(conf):
	if(pinguino.digitalRead(conf["SMCC_D"]) == '1'):
		return True
	else:
		return False
	
#Sensor del Carro Izquierda	
	
def SMCC_I(conf):
	if(pinguino.digitalRead(conf["SMCC_I"]) == '1'):
		return True
	else:
		return False
	
#Sensor de linea	
	
def SL(conf):
	if(int(pinguino.analogRead(conf["SL"])) >= conf['valorbase']):
		return 1
	else:
		return 0
	
#Sensor del Carro Derecho	
	
def testSMCC_D(conf):
	for i in range(0,8):
		print ("Hola",pinguino.digitalRead(conf["SMCC_D"]))
		time.sleep(1)
		
def testSMCC_I(conf):
	for i in range(0,8):
		print ("Hola",pinguino.digitalRead(conf["SMCC_I"]))
		time.sleep(1)

def testSL(conf):
	for i in range(0,20):
		AvansarSMCC_I2(conf)
	i=0
	a=0
	while(not(SMCC_D(conf))):
		if(SL(conf)==1):
			moverSL(conf)
			i=i+1
		if(SL(conf)==0):
			moverSL(conf)
			a=a+1
	enviar(conf["MCCB"],0)
	print("Transparentes: ",i,"Negras : ",a)
		
def inicializar(conf):
	pinguino.analogWrite(12,conf["pwm"])
	pinguino.analogWrite(11,conf["pwm"])
	carC=conf["anchoCarroIzq"]
	AvansarSMCC_I(conf)
	enviar(conf["MCCB"],1)
	time.sleep(0.1)
	enviar(conf["MCCB"],0)
	for i in range(0,10):
		AvansarSMCC_I2(conf)
	time.sleep(0.1)
	for i in range(0,carC):
		moverSL(conf)
	enviar(conf["MCCB"],0)
	
def punto(conf):
	t=(conf["TMCC"] / 1000)
	while(not(SMCC_D(conf))):
		while(SL(conf))and(not(SMCC_D(conf))):
			moverMc_D(conf)	
			time.sleep(t)
			parar()
		EIman(conf)
		while(not(SL(conf)))and(not(SMCC_D(conf))):
			moverMc_D(conf)	
			time.sleep(t)
			parar()

def tomarP(conf):	
	pinguino.analogWrite(12,"1023")
	pinguino.analogWrite(11,"1023")
	t=(conf["TMCC"] / 1000)
	AvansarSMCC_I2(conf)
	i=0
	while(i < 200):
		moverMc_D(conf)
		t=(conf["TiempoEntreBobina"] / 1000)
		enviar(conf["MCCB"],1)
		enviar(conf["MPPA"],1)
		time.sleep(t)
		enviar(conf["MPPA"],0)
		enviar(conf["MPPB"],1)
		time.sleep(t)
		enviar(conf["MPPB"],0)
		enviar(conf["MPPC"],1)
		time.sleep(t)
		enviar(conf["MPPC"],0)
		enviar(conf["MPPD"],1)
		time.sleep(t)
		enviar(conf["MPPD"],0)
		i+=1	
	parar()
	moverMc_I(conf)	
	time.sleep(0.5)
	parar()
	moverMc_D(conf)	
	time.sleep(0.5)
	parar()
	AvansarSMCC_I(conf)
	i=0
	while (i<25):
		AvansarSMPP_D(conf)
		i+=1
	pinguino.analogWrite(12,conf["pwm"])
	pinguino.analogWrite(11,conf["pwm"])
	
def AvansarSMCC_D(conf):
	while(not(SMCC_D(conf))):
		moverMc_D(conf)	
	parar()
		
def AvansarSMCC_I(conf):
	while(not(SMCC_I(conf))):
		moverMc_I(conf)	
	parar()
	
def AvansarSMCC_D2(conf):
	moverMc_D(conf)	
	time.sleep(0.2)
	enviar(conf["MCCB"],0)
			
def AvansarSMCC_I2(conf):
	moverMc_I(conf)	
	time.sleep(0.2)
	enviar(conf["MCCA"],0)
		
def AvansarSMPP_D(conf):
	i=0
	while(i != 5):
		moverMpp_D(conf)	
		i+=1
	parar()
	
def AvansarSMPP_I(conf):
	i=0
	while(i != 100):
		moverMpp_I(conf)	
		i+=1
	parar()
		
def sacarPapel(conf):
	i=0
	while(i != 400):
		moverMpp_D(conf)	
		i+=1
	parar()	
		
def sacarPapel2(conf):
	i=0
	while(i != 400):
		moverMpp_I(conf)	
		i+=1
	parar()	
	
