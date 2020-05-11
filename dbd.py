# python3
#  
# Author: Cody Keller
# Description: Progress through Dead by Daylight's Bloodweb in a goal-oriented manner
######################################################################################

# IMPORTS
import wx
import ctypes
import pygame

# GLOBAL VARS
user32 = ctypes.windll.user32
scrWidth, scrHeight = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
winWidth, winHeight = 350, 230

class MainWindow(wx.Frame):


	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(winWidth,winHeight), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
		self.Center()

		# MENU
		filemenu = wx.Menu()
		iconImage = wx.Icon()
		iconImage.CopyFromBitmap(wx.Bitmap("icon.png", wx.BITMAP_TYPE_ANY))

		# ABOUT AND EXIT
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About","Information about this program")
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, "&Exit","Terminate the program")

		# Create Menubar
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "File")
		self.SetMenuBar(menuBar)

		

		# MAIN PANEL
		pygame.mixer.init(48000, -16, 4, 1024)
		pygame.mixer.music.load("0004.mp3")
		pygame.mixer.music.set_volume(0.2)
		panel = wx.Panel(self)
		self.SetBackgroundColour(wx.Colour(94,97,101))
		self.startImage = wx.Image("startbutton.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.startButton = wx.BitmapButton(self , -1, self.startImage, pos=(winWidth-122,0), style=wx.NO_BORDER) #winHeight-112
		self.startButton.SetBackgroundColour(wx.Colour(94,97,101))
		self.dbdTitle = wx.Image("dbd.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.bmp1 = wx.StaticBitmap(self, -1, self.dbdTitle, (10,10))
		self.statusBar = self.CreateStatusBar(style=wx.BORDER_NONE)
		self.statusBar.SetStatusStyles([wx.SB_FLAT])
		self.statusBar.SetBackgroundColour("grey")
		self.statusBar.SetForegroundColour(wx.Colour(255,255,255))
		self.statusBar.SetStatusText("waiting for commands...")


		
		# startButton.SetBitmap(wx.Image("startbuttonhover.png", wx.BITMAP_TYPE_PNG))
		# Choices
		lblist = ["Perks", "Addons", "Random"]
		self.rbox = wx.RadioBox(self, label="Method of Progress", pos = (10,50), choices = lblist, style = wx.RA_SPECIFY_ROWS)
		self.rbox.SetForegroundColour(wx.Colour(255,255,255))


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
		abt = wx.MessageDialog(self, "Created by: Cody Keller\n--------------------------\nThis program is meant to help progress through Dead by Daylight's Bloodweb in a goal-oriented manner.","About", wx.OK)
		abt.ShowModal() # Show Message
		abt.Destroy()

	def OnExit(self, e):
		self.Close(True)

	def Start(self, e):
		print(":>> initializing bloodweb progression...")
		self.statusBar.SetStatusText("initializing bloodweb progression...")
		pygame.mixer.music.play()


	def Hover(self, e):
		newPic = wx.Image("startbuttonhover.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.startButton.SetBitmap(newPic)
		

	def HoverLeave(self, e):
		newPic = wx.Image("startbutton.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.startButton.SetBitmap(newPic)




# START APPLICATION
app = wx.App(False)
frame = MainWindow(None, 'DBD Bloodweb Autopather')
frame.Show()

app.MainLoop()