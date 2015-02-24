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
import wx
import os
import sys
sys.path.append("..")
from data.configuracion  import Config
from data.tooltest  import Test

class OpenBraille(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(600, 500))
		self.modify = False
		self.last_name_saved = ''
		self.replace = False
		
		menubar = wx.MenuBar()
		file = wx.Menu()
		
		new = wx.MenuItem(file, 101, '&Nuevo\tCtrl+N', 'Crear un nuevo documento')
		new.SetBitmap(wx.Bitmap('img/Nuevo.png'))
		file.AppendItem(new)
		
		open = wx.MenuItem(file, 102, '&Abrir\tCtrl+O', 'Abrir un archivo existente')
		open.SetBitmap(wx.Bitmap('img/Open.png'))
		file.AppendItem(open)
		
		save = wx.MenuItem(file, 103, '&Guardar\tCtrl+S', 'Guardar un Archivo')
		save.SetBitmap(wx.Bitmap('img/Save.png'))
		file.AppendItem(save)
		file.AppendSeparator()
		
		imprimir = wx.MenuItem(file, 111, '&Imprimir\tCtrl+O', 'Imprimir texto')
		imprimir.SetBitmap(wx.Bitmap('img/Printer.png'))
		file.AppendItem(imprimir)
		file.AppendSeparator()
		
		quit = wx.MenuItem(file, 105, '&Salir\tCtrl+Q', 'Salir del programa')
		quit.SetBitmap(wx.Bitmap('img/close.png'))
		file.AppendItem(quit)
		
		edit = wx.Menu()
		cut = wx.MenuItem(edit, 106, '&Cortar\tCtrl+X', 'Cortar el texto seleccionado')
		cut.SetBitmap(wx.Bitmap('img/Cut.png'))
		edit.AppendItem(cut)
		
		copy = wx.MenuItem(edit, 107, '&Copiar\tCtrl+C', 'Copiar el texto seleccionado')
		copy.SetBitmap(wx.Bitmap('img/Copy.png'))
		edit.AppendItem(copy)
		
		paste = wx.MenuItem(edit, 108, '&Pegar\tCtrl+V', 'Pegar el texto seleccionado')
		paste.SetBitmap(wx.Bitmap('img/Paste.png'))
		edit.AppendItem(paste)
		
		delete = wx.MenuItem(edit, 109, '&Eliminar', 'Eliminar el texto seleccionado')
		delete.SetBitmap(wx.Bitmap('img/Delete.png',))
		edit.AppendItem(delete)
		
		conf = wx.Menu()
		impresoraConfiguracion = wx.MenuItem(edit, 110, '&Propiedades de Impresora', 'Configurar los parametros de la impresora')
		impresoraConfiguracion.SetBitmap(wx.Bitmap('img/Settings.png',))
		conf.AppendItem(impresoraConfiguracion)
		test = wx.MenuItem(edit, 114, '&Testear la Impresora', 'Testear las funciones de la impresora')
		test.SetBitmap(wx.Bitmap('img/Test.png',))
		conf.AppendItem(test)
		
		help = wx.Menu()
		about = wx.MenuItem(help, 112, '&Sobre el Proyecto\tF1', 'Sobre el proyecto')
		about.SetBitmap(wx.Bitmap('img/About.png'))
		contact = wx.MenuItem(help, 113, '&Contacto\tF1', 'Contactar con los integrantes del proyecto')
		contact.SetBitmap(wx.Bitmap('img/Gmail.png'))
		help.AppendItem(about)
		help.AppendItem(contact)
		
		menubar.Append(file, '&Archivo')
		menubar.Append(edit, '&Editar')
		menubar.Append(conf, '&Impresora')
		menubar.Append(help, '&Ayuda')
		
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU, self.NewApplication, id=101)
		self.Bind(wx.EVT_MENU, self.OnOpenFile, id=102)
		self.Bind(wx.EVT_MENU, self.OnSaveFile, id=103)
		self.Bind(wx.EVT_MENU, self.OnSaveAsFile, id=104)
		self.Bind(wx.EVT_MENU, self.QuitApplication, id=105)
		self.Bind(wx.EVT_MENU, self.OnCut, id=106)
		self.Bind(wx.EVT_MENU, self.OnCopy, id=107)
		self.Bind(wx.EVT_MENU, self.OnPaste, id=108)
		self.Bind(wx.EVT_MENU, self.OnDelete, id=109)
		self.Bind(wx.EVT_MENU, self.OnAbout, id=112)
		self.Bind(wx.EVT_MENU, self.OnConfig, id=110)
		self.Bind(wx.EVT_MENU, self.OnContact, id=113)
		self.Bind(wx.EVT_MENU, self.OnTest, id=114)
		# setting up toolbar
		
		self.toolbar = self.CreateToolBar( wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT )
		self.toolbar.AddSimpleTool(801, wx.Bitmap('img/Nuevo.png'),'Nuevo', '')
		self.toolbar.AddSimpleTool(802, wx.Bitmap('img/Open.png'),'Abrir', '')
		self.toolbar.AddSimpleTool(803, wx.Bitmap('img/Save.png'),'Guardar', '')
		
		self.toolbar.AddSeparator()
		self.toolbar.AddSimpleTool(804, wx.Bitmap('img/Cut.png'),'Cortar', '')
		self.toolbar.AddSimpleTool(805, wx.Bitmap('img/Copy.png'),'Copiar', '')
		self.toolbar.AddSimpleTool(806, wx.Bitmap('img/Paste.png'),'Pegar', '')
		self.toolbar.AddSeparator()
		self.toolbar.AddSimpleTool(808, wx.Bitmap('img/Printer.png'),'Imprimir', '')
		self.toolbar.AddSimpleTool(809, wx.Bitmap('img/Test.png'),'Testear', '')
		self.toolbar.AddSimpleTool(810, wx.Bitmap('img/Settings.png'),'Configurar', '')
		self.toolbar.AddSeparator()
		self.toolbar.AddSimpleTool(807, wx.Bitmap('img/close.png'),'Salir', '')
		self.toolbar.Realize()
		
		self.Bind(wx.EVT_TOOL, self.NewApplication, id=801)
		self.Bind(wx.EVT_TOOL, self.OnOpenFile, id=802)
		self.Bind(wx.EVT_TOOL, self.OnSaveFile, id=803)
		self.Bind(wx.EVT_TOOL, self.OnCut, id=804)
		self.Bind(wx.EVT_TOOL, self.OnCopy, id=805)
		self.Bind(wx.EVT_TOOL, self.OnPaste, id=806)
		self.Bind(wx.EVT_TOOL, self.QuitApplication, id=807)
		self.Bind(wx.EVT_TOOL, self.OnImprimir, id=808)
		self.Bind(wx.EVT_TOOL, self.OnTest, id=809)
		self.Bind(wx.EVT_TOOL, self.OnConfig, id=810)
		
		self.text = wx.TextCtrl(self, 1000, '', size=(-1, -1), style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
		self.text.SetFocus()
		self.text.Bind(wx.EVT_TEXT, self.OnTextChanged, id=1000)
		
		self.Bind(wx.EVT_CLOSE, self.QuitApplication)
		self.StatusBar()
		self.Centre()
		self.Show(True)
		
	def OnContact(self, event):
		app = wx.App()
		frame = wx.Frame(None, -1, 'simple.py',size=(150, 55))
		wx.StaticText(frame, -1, "openbraille@gmail.com", pos=(0, 0))
		frame.Centre()
		frame.Show()
		app.MainLoop()
		
	def OnImprimir(self, event):
		app = wx.App()
		frame = wx.Frame(None, -1, 'simple.py',size=(600, 400))
		gif_fname = "img/jaja.gif"
		gif = wx.animate.GIFAnimationCtrl(frame, -1, gif_fname,pos=(0,0),size=(10,10))
		wx.StaticText(frame, -1, "Aun no implementado jaja:", pos=(250, 250))
		gif.GetPlayer()
		gif.Play()
		frame.Centre()
		frame.Show()
		app.MainLoop()
		
	def NewApplication(self, event):
		editor = OpenBraille(None, -1, 'OpenBraille')
		editor.Centre()
		editor.Show()
		
	def OnOpenFile(self, event):
		file_name = os.path.basename(self.last_name_saved)
		if self.modify:
			dlg = wx.MessageDialog(self, 'Guardar Cambios?', '', wx.YES_NO |wx.YES_DEFAULT | wx.CANCEL | wx.ICON_QUESTION)
			val = dlg.ShowModal()
			if val == wx.ID_YES:
				self.OnSaveFile(event)
				self.DoOpenFile()
			elif val == wx.ID_CANCEL:
				dlg.Destroy()
			else:
				self.DoOpenFile()
		else:
			self.DoOpenFile()
			
	def DoOpenFile(self):
		wcd = 'All files (*)|*|Editor files (*.ef)|*.ef|'
		dir = os.getcwd()
		open_dlg = wx.FileDialog(self, "Open TXT file", "", "","TXT files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		if open_dlg.ShowModal() == wx.ID_OK:
			path = open_dlg.GetPath()
			try:
				file = open(path, 'r')
				text = file.read()
				file.close()
				if self.text.GetLastPosition():
					self.text.Clear()
				self.text.WriteText(text)
				self.last_name_saved = path
				self.statusbar.SetStatusText('', 1)
				self.modify = False
			except IOError, error:
				dlg = wx.MessageDialog(self, 'Error opening file\n' + str(error))
				dlg.ShowModal()
			except UnicodeDecodeError, error:
				dlg = wx.MessageDialog(self, 'Error opening file\n' + str(error))
				dlg.ShowModal()
		open_dlg.Destroy()
		
	def OnSaveFile(self, event):
		if self.last_name_saved:
			try:
				file = open(self.last_name_saved, 'w')
				text = self.text.GetValue()
				file.write(text)
				file.close()
				self.statusbar.SetStatusText(os.path.basename(self.last_name_saved) + ' saved', 0)
				self.modify = False
				self.statusbar.SetStatusText('', 1)
			except IOError, error:
				dlg = wx.MessageDialog(self, 'Error saving file\n' +str(error))
				dlg.ShowModal()
		else:
			self.OnSaveAsFile(event)
		
	def OnSaveAsFile(self, event):
		wcd='Text files (*.txt)|*.txt|'
		dir = os.getcwd()
		save_dlg = saveFileDialog = wx.FileDialog(self, "Save TXT file", "", "","TXT files (*.txt)|*.txt", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		if save_dlg.ShowModal() == wx.ID_OK:
			path = save_dlg.GetPath()
			try:
				file = open(path, 'w')
				text = self.text.GetValue()
				file.write(text)
				file.close()
				self.last_name_saved = os.path.basename(path)
				self.statusbar.SetStatusText(self.last_name_saved + 'saved', 0)
				self.modify = False
				self.statusbar.SetStatusText('', 1)
			except IOError, error:
				dlg = wx.MessageDialog(self, 'Error saving file\n' + str(error))
				dlg.ShowModal()
		save_dlg.Destroy()
		
	def OnCut(self, event):
		self.text.Cut()
		
	def OnCopy(self, event):
		self.text.Copy()
		
	def OnTest(self, event):
		test = Test()
		
	def OnConfig(self, event):
		conf = Config()
		conf.menuConf()
		
	def OnPaste(self, event):
		self.text.Paste()
		
	def QuitApplication(self, event):
		if self.modify:
			dlg = wx.MessageDialog(self, 'Save before Exit?', '', wx.YES_NO | wx.YES_DEFAULT | wx.CANCEL | wx.ICON_QUESTION)
			val = dlg.ShowModal()
			if val == wx.ID_YES:
				self.OnSaveFile(event)
				if not self.modify:
					wx.Exit()
			elif val == wx.ID_CANCEL:
				dlg.Destroy()
			else:
				self.Destroy()
		else:
			self.Destroy()
			
	def OnDelete(self, event):
		frm, to = self.text.GetSelection()
		self.text.Remove(frm, to)
		
	def OnSelectAll(self, event):
		self.text.SelectAll()
		
	def OnTextChanged(self, event):
		self.modify = True
		self.statusbar.SetStatusText(' modified', 1)
		event.Skip()
		
	def OnKeyDown(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_INSERT:
			if not self.replace:
				self.statusbar.SetStatusText('INS', 2)
				self.replace = True
			else:
				self.statusbar.SetStatusText('', 2)
				self.replace = False
			event.Skip()
			
	def ToggleStatusBar(self, event):
		if self.statusbar.IsShown():
			self.statusbar.Hide()
		else:
			self.statusbar.Show()
		
	def StatusBar(self):
		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetFieldsCount(3)
		self.statusbar.SetStatusWidths([-5, -2, -1])
		
	def OnAbout(self, event):
		dlg = wx.MessageDialog(self, '\tProyecto impresora braille -2014','Sobre el Proyecto', wx.OK | wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
	
	
		
app = wx.App()
OpenBraille(None, -1, 'OpenBraille')
app.MainLoop()
