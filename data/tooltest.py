"""
	tooltest.py -- Función de testeo de la impreso braille casera.
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
import wx
import os
import pickle
import unicodedata
from data.configuracion  import Config
from Motor import *

class Test(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, 'wxButton',pos=(300, 150), size=(520, 450))
		config = Config()
		self.conf = config.getConf2()
		for key in self.conf:
			self.conf[key] =(float(self.conf[key]))
		self.menuConf()
        
	def menuConf(self):
		wx.StaticText(self, -1, "Testeador de funciones de la Impresora", pos=(120, 0))
		self.button1 = wx.Button(self, id=1, label="Mover el MCC hasta Sensor izquierdo",pos=(10, 50), size=(250, 25))
		self.button1 = wx.Button(self, id=2, label="Mover el MCC hasta Sensor derecho",pos=(260, 50), size=(250, 25))
		self.button1 = wx.Button(self, id=5, label='Mover hacia la izquierda el MCC',pos=(10, 75), size=(250, 25))
		self.button1 = wx.Button(self, id=6, label='Mover hacia la derecha el MCC',pos=(260, 75), size=(250, 25))
		self.button1 = wx.Button(self, id=3, label='Girar el MPP hacia izquierda',pos=(10, 100), size=(250, 25))
		self.button1 = wx.Button(self, id=4, label='Girar el MPP hacia derecha',pos=(260, 100), size=(250, 25))
		self.button1 = wx.Button(self, id=7, label="Pulso electro iman",pos=(10, 125), size=(250, 25))
		self.button1 = wx.Button(self, id=8, label="Tomar Papel",pos=(260, 125), size=(250, 25))
		self.button1 = wx.Button(self, id=9, label='sacar Hoja',pos=(10, 150), size=(250, 25))
		self.button1 = wx.Button(self, id=10, label='Lectura de sensores',pos=(260, 150), size=(250, 25))
		self.button1 = wx.Button(self, id=11, label='Parar',pos=(120, 175), size=(250, 25))
		
		self.button1 = wx.Button(self, id=17, label='Aceptar',pos=(100, 400), size=(70, 25))
		self.button1 = wx.Button(self, id=18, label='Cancelar',pos=(170, 400), size=(70, 25))
		self.button1 = wx.Button(self, id=19, label='Ayuda',pos=(240, 400), size=(70, 25))
		
		self.Bind(wx.EVT_BUTTON, self.OnMovermccsi,id=1)
		self.Bind(wx.EVT_BUTTON, self.OnMovermccsd,id=2)
		self.Bind(wx.EVT_BUTTON, self.OnMovermccd,id=3)
		self.Bind(wx.EVT_BUTTON, self.OnMovermcci,id=4)
		self.Bind(wx.EVT_BUTTON, self.OnGirarmppd,id=5)
		self.Bind(wx.EVT_BUTTON, self.OnGirarmppi,id=6)
		self.Bind(wx.EVT_BUTTON, self.OnPulsoelectroi,id=7)
		self.Bind(wx.EVT_BUTTON, self.OnTomarpapel,id=8)
		self.Bind(wx.EVT_BUTTON, self.OnSacarhoja,id=9)
		self.Bind(wx.EVT_BUTTON, self.OnLeersensores,id=10)
		self.Bind(wx.EVT_BUTTON, self.OnParar,id=11)

		self.Bind(wx.EVT_BUTTON, self.Aceptar,id=17)
		self.Bind(wx.EVT_BUTTON, self.QuitApplication,id=18)
		self.Bind(wx.EVT_BUTTON, self.Ayuda,id=19)

		self.Show(True)
        
	def OnMovermccsi(self, event):
		AvansarSMCC_I(self.conf)
	def OnMovermccsd(self, event):
		AvansarSMCC_D(self.conf)
	def OnMovermccd(self, event):
		AvansarSMCC_D2(self.conf)
	def OnMovermcci(self, event):
		AvansarSMCC_I2(self.conf)
	def OnGirarmppd(self, event):
		AvansarSMPP_D(self.conf)
	def OnGirarmppi(self, event):
		AvansarSMPP_I(self.conf)
	def OnPulsoelectroi(self, event):
		EIman(self.conf)
	def OnTomarpapel(self, event):
		tomarP(self.conf)
	def OnSacarhoja(self, event):
		sacarPapel(self.conf)
	def OnLeersensores(self, event):
		testSensores(self.conf)
	def OnParar(self, event):
		parar()
	def Ayuda(self, event):
		os.startfile("1.jpg")
	
	def Aceptar(self, event):
		self.Destroy()
     
	def QuitApplication(self, event):
		self.Destroy()
        

