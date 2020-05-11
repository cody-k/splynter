# python3
#  
# Author: Cody Keller
# Description: https://www.github.com/cody-k
######################################################################################

# IMPORTS
import wx
import ctypes
import pygame

# GLOBAL VARS
user32 = ctypes.windll.user32
scrWidth, scrHeight = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
winWidth, winHeight = 350, 230

# Main Class
class MainWindow(wx.Frame):

	# Initializer
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(winWidth,winHeight), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
		self.Center()

		# Create File Menu & Set Icon for Splyntery
		filemenu = wx.Menu()
		iconImage = wx.Icon()
		iconImage.CopyFromBitmap(wx.Bitmap("images/png/icon.png", wx.BITMAP_TYPE_ANY))

		# About and Exit
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About","Information about this program")
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, "&Exit","Terminate the program")

		# Create Menubar
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "File")
		self.SetMenuBar(menuBar)

		

		# Main Panel
		pygame.mixer.init(48000, -16, 4, 1024)
		pygame.mixer.music.load("audio/0004.mp3")
		pygame.mixer.music.set_volume(0.2)
		panel = wx.Panel(self)
		self.SetBackgroundColour(wx.Colour(35, 37, 48))
		self.startImage = wx.Image("images/png/startbutton.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.startButton = wx.BitmapButton(self , -1, self.startImage, pos=(winWidth-122,0), style=wx.NO_BORDER) #winHeight-112
		self.startButton.SetBackgroundColour(wx.Colour(35, 37, 48))
		self.dbdTitle = wx.Image("images/png/dbd.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.bmp1 = wx.StaticBitmap(self, -1, self.dbdTitle, (10,10))
		self.statusBar = self.CreateStatusBar(style=wx.BORDER_NONE)
		self.statusBar.SetStatusStyles([wx.SB_FLAT])
		self.statusBar.SetBackgroundColour("grey")
		self.statusBar.SetForegroundColour(wx.Colour(255,255,255))
		self.statusBar.SetStatusText("waiting for commands...")

		# Radio Box -- May change to single rbuttons due to lack of wx.SetForegroundColour() intregration
		lblist = ["Perks", "Addons", "Random"]
		self.rbox = wx.RadioBox(self, label="Method of Progress", pos = (10,50), choices = lblist, style = wx.RA_SPECIFY_ROWS)
		self.rbox.SetForegroundColour(wx.Colour(255, 255, 255))
		self.rbox.SetBackgroundColour(wx.Colour(46, 48, 62))


		# Set Events
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		self.Bind(wx.EVT_BUTTON, self.Start, self.startButton)
		self.startButton.Bind(wx.EVT_ENTER_WINDOW, self.Hover)
		self.startButton.Bind(wx.EVT_LEAVE_WINDOW, self.HoverLeave)
		self.SetIcon(iconImage)

		# self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.startButton.SetDefault()


		# Show Window
		self.Show(True)



	def OnAbout(self, e):
		abt = wx.MessageDialog(self, "Created by: Cody Keller\n--------------------------\nhttps://github.com/cody-k","About", wx.OK)
		abt.ShowModal() # Show Message
		abt.Destroy()

	def OnExit(self, e):
		self.Close(True)

	def Start(self, e):
		print(":>> initializing bloodweb progression...")
		self.statusBar.SetStatusText("initializing bloodweb progression...")
		pygame.mixer.music.play()


	def Hover(self, e):
		newPic = wx.Image("images/png/startbuttonhover.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.startButton.SetBitmap(newPic)
		

	def HoverLeave(self, e):
		newPic = wx.Image("images/png/startbutton.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.startButton.SetBitmap(newPic)

	
	# OLD CODE FROM V1 IN USE UNTIL V2 OBJECT DETECTION IS COMPLTED





# START APPLICATION
app = wx.App(False)
frame = MainWindow(None, 'Splyntery')
frame.Show()

app.MainLoop()
