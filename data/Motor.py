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
 *   Licencia: https://github.com/Pablo03/OpenBraille/blob/master/LICENSE
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from pusb import *
import wx
import wx.animate	
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, 'wxBitmapButton',pos=(300, 150), size=(820, 400))
		self.panel1 = wx.Panel(self, -1)
		imageFile = "img/noconec.png"
		image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.button1 = wx.BitmapButton(self.panel1, id=1, bitmap=image1,pos=(0, 0), size = (image1.GetWidth()+5, image1.GetHeight()+5))
		self.Bind(wx.EVT_BUTTON, self.button1Click, id=1)
		self.Show(True)

	def button1Click(self,event):
		try:
			pinguino = PynguinoUSB(vboot="v4")
			for i in range(0,8):
				pinguino.pinMode(i,"OUTPUT")
			for i in range(10,13):
				pinguino.pinMode(i,"INPUT")
			self.Destroy()
			wx.Frame.__init__(self, None, wx.ID_ANY, 'wxBitmapButton',pos=(300, 150), size=(820, 400))
			self.panel1 = wx.Panel(self, -1)
			imageFile = "img/conec.png"
			image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			self.button1 = wx.BitmapButton(self.panel1, id=2, bitmap=image1,pos=(0, 0), size = (image1.GetWidth()+5, image1.GetHeight()+5))
			self.Bind(wx.EVT_BUTTON, self.adios, id=2)
			self.Show(True)
		except:
			print ("Aun no se detecta la coneccion")

	def adios(self,event):
		self.Destroy()

def conectar():
	try:
		pinguino = PynguinoUSB(vboot="v4")
		for i in range(0,8):
			pinguino.pinMode(i,"OUTPUT")
		for i in range(10,13):
			pinguino.pinMode(i,"INPUT")
			
	except Exception:
		application = wx.App()
		window = MyFrame()
		application.MainLoop()

conectar()

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
	if(SL(conf)):
		while(SL(conf)):
			moverMc_D(conf)
	else:
		while(not(SL(conf))):
			moverMc_D(conf)	
	enviar(conf["MCCB"],0)

def EIman(conf):
	enviar(conf["Electro"],1)
	time.sleep(conf["TiempoEi"])
	enviar(conf["Electro"],0)
	time.sleep(conf["TiempoEiZ"])
	
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
	for i in range(0,8):
		print ("Hola",pinguino.digitalRead(conf["SL"]))
		time.sleep(1)
		
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
	time.sleep(0.010)
	if(pinguino.digitalRead(conf["SL"]) == '1'):
		return 1
	else:
		return 0
		
def inicializar(conf):
	carC=conf["anchoCarroIzq"]
	AvansarSMCC_I(conf)
	time.sleep(0.1)
	AvansarSMCC_I(conf)
	time.sleep(0.4)
	i=0
	while(i < carC):
		moverSL(conf)
		i+=1
	
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
	t=(conf["TMCC"] / 1000)
	AvansarSMCC_I(conf)
	i=0
	while(i != 200):
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
	
