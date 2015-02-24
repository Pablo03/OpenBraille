"""
 * configuracion.py 
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

import wx
import os
import pickle
import unicodedata

class Config(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, 'wxButton',pos=(300, 150), size=(500, 500))
		self.configuracion={
		"TiempoEntreBobina":u"4.5",
		"anchoCarroIzq":u"20",
		"TMCC":u"25.0",
		"TSL":u"150",
		"CantCar":u"14",
		"MPPA":u"4",
		"MPPB":u"5",
		"MPPC":u"3",
		"MPPD":u"6",
		"MCCA":u"2",
		"MCCB":u"1",
		"Electro":u"0",
		"TiempoEi":u"0.035",
		"TiempoEiZ":u"0.12",
		"SMCC_D":u"10",
		"SMCC_I":u"11",
		"SL":u"12",
		"SH":u"7"
		}
		self.abrirConf()
        
	def checkfile(self,archivo):  
		if os.path.exists(archivo): 
			return True
		else: 
			return False
        
	def abrirConf(self):
		if(self.checkfile("cfg.txt")):
			configuracion2 = pickle.load( open( "cfg.txt", "rb" ) )
			self.configuracion.update(configuracion2)
		
	def guardarConf(self):
		pickle.dump( self.configuracion, open( "cfg.txt", "wb" ) )
        
	def getConf(self,value):
		return self.configuracion[value]
		
	def getConf2(self):
		return self.configuracion
		
	def setConf(self,valor,key):
		self.configuracion[valor]=key
        
	def menuConf(self):
		image1 = wx.Image("img/Help.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		wx.StaticText(self, -1, "Configuracion de los Tiempos\nde los Pulsos enviados al\nHardware de la impresora:", pos=(10, 0))
		wx.StaticText(self, -1, "TiempoE/Bobina:", pos=(10, 60))
		self.TiempoEntreBobina = wx.TextCtrl(self,-1,self.getConf("TiempoEntreBobina"), pos=(110, 60), size=(50, 25))
		
		wx.StaticText(self, -1, "TiempoMCC:", pos=(10, 90))
		self.TMCC = wx.TextCtrl(self,-1,self.getConf("TMCC"), pos=(110, 90), size=(50, 25))
		
		wx.StaticText(self, -1, "TiempoSL:", pos=(10, 120))
		self.TSL = wx.TextCtrl(self,-1,self.getConf("TSL"), pos=(110, 120), size=(50, 25))

		wx.StaticText(self, -1, "TiempoEi:", pos=(10, 150))
		self.TiempoEi = wx.TextCtrl(self,-1,self.getConf("TiempoEi"), pos=(110, 150), size=(50, 25))
		
		wx.StaticText(self, -1, "Configuracion de la cantidad de\n caracteres que puede imprimir\n la impresora:", pos=(10, 220))
		wx.StaticText(self, -1, "CantCar:", pos=(10, 280))
		self.CantCar = wx.TextCtrl(self,-1,self.getConf("CantCar"), pos=(100, 280), size=(50, 25))
		

		wx.StaticText(self, -1, "Configuracion de los pines\n	   del \nHardware de la impresora:", pos=(250, 0))
		wx.StaticText(self, -1, "PinMPP_A:", pos=(250, 60))
		self.MPPA = wx.TextCtrl(self,-1,self.getConf("MPPA"), pos=(350, 60), size=(50, 25))

		wx.StaticText(self, -1, "PinMPP_B:", pos=(250, 90))
		self.MPPB = wx.TextCtrl(self,-1,self.getConf("MPPB"), pos=(350, 90), size=(50, 25))

		wx.StaticText(self, -1, "PinMPP_C:", pos=(250, 120))
		self.MPPC = wx.TextCtrl(self,-1,self.getConf("MPPC"), pos=(350, 120), size=(50, 25))

		wx.StaticText(self, -1, "PinMPP_D:", pos=(250, 150))
		self.MPPD = wx.TextCtrl(self,-1,self.getConf("MPPD"), pos=(350, 150), size=(50, 25))

		wx.StaticText(self, -1, "PinMCC_A:", pos=(250, 180))
		self.MCCA = wx.TextCtrl(self,-1,self.getConf("MCCA"), pos=(350, 180), size=(50, 25))

		wx.StaticText(self, -1, "PinMCC_B:", pos=(250, 210))
		self.MCCB = wx.TextCtrl(self,-1,self.getConf("MCCB"), pos=(350, 210), size=(50, 25))

		wx.StaticText(self, -1, "PinElectroIman:", pos=(250, 240))
		self.Electro = wx.TextCtrl(self,-1,self.getConf("Electro"), pos=(350, 240), size=(50, 25))

		wx.StaticText(self, -1, "PinSMCC_I:", pos=(250, 270))
		self.SMCC_I = wx.TextCtrl(self,-1,self.getConf("SMCC_I"), pos=(350, 270), size=(50, 25))

		wx.StaticText(self, -1, "PinSMCC_D:", pos=(250, 300))
		self.SMCC_D = wx.TextCtrl(self,-1,self.getConf("SMCC_D"), pos=(350, 300), size=(50, 25))

		wx.StaticText(self, -1, "PinSLinea:", pos=(250, 330))
		self.SL = wx.TextCtrl(self,-1,self.getConf("SL"), pos=(350, 330), size=(50, 25))

		wx.StaticText(self, -1, "PinSHoja:", pos=(250, 360))
		self.SH = wx.TextCtrl(self,-1,self.getConf("SH"), pos=(350, 360), size=(50, 25))

		
		self.button1 = wx.Button(self, id=17, label='Aceptar',pos=(100, 400), size=(70, 25))
		self.button1 = wx.Button(self, id=18, label='Cancelar',pos=(170, 400), size=(70, 25))
		self.button1 = wx.Button(self, id=19, label='Ayuda',pos=(240, 400), size=(70, 25))
		self.button1 = wx.Button(self, id=20, label='Valores Predeterminados',pos=(310, 400), size=(140, 25))
		
		self.Bind(wx.EVT_BUTTON, self.Aceptar,id=17)
		self.Bind(wx.EVT_BUTTON, self.QuitApplication,id=18)
		self.Bind(wx.EVT_BUTTON, self.Ayuda,id=19)
		self.Bind(wx.EVT_BUTTON, self.RestaurarValores,id=20)
		
		

		self.Show(True)
        
	def Ayuda(self, event):
		os.startfile("1.jpg")
	
	def Aceptar(self, event):
		self.configuracion["TiempoEntreBobina"]=self.TiempoEntreBobina.GetValue()
		self.configuracion["TMCC"]=self.TMCC.GetValue()
		self.configuracion["TSL"]=self.TSL.GetValue()
		self.configuracion["TiempoEi"]=self.TiempoEi.GetValue()
		self.configuracion["CantCar"]=self.CantCar.GetValue()
		self.configuracion["MPPA"]=self.MPPA.GetValue()
		self.configuracion["MPPB"]=self.MPPB.GetValue()
		self.configuracion["MPPC"]=self.MPPC.GetValue()
		self.configuracion["MPPD"]=self.MPPD.GetValue()
		self.configuracion["MCCA"]=self.MCCA.GetValue()
		self.configuracion["MCCB"]=self.MCCB.GetValue()
		self.configuracion["Electro"]=self.Electro.GetValue()
		self.configuracion["SMCC_I"]=self.SMCC_I.GetValue()
		self.configuracion["SMCC_D"]=self.SMCC_D.GetValue()
		self.configuracion["SL"]=self.SL.GetValue()
		self.configuracion["SH"]=self.SH.GetValue()
		self.guardarConf()
		self.Destroy()
	
	def RestaurarValores(self, event):
		self.Destroy()
		os.remove("cfg.txt")
		conf = Config()
     
	def QuitApplication(self, event):
		self.guardarConf()
		self.Destroy()
        
