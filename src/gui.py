import os


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# from tkinter import Tk, Canvas, Frame, BOTH


# import __main__



# def dodonothing():
# 	print("Hello gui.py")

class Gui(object):
	"""doc for Gui"""
	def __init__(self, master):
		self.master = master
		self.init_frames()
		self.init_menu()
		# self.init_control_frame()
		self.init_canvas_frame()
		# self.init_status_frame()
		self.styles()
		#GUI var
		self.status = StringVar()
		self.mode = StringVar()
		self.speed = StringVar()
		self.xcoord = IntVar()
		self.ycoord = IntVar()
		self.distance = IntVar()




	def init_frames(self):

		self.master.columnconfigure(0, weight=1)
		self.master.rowconfigure(0, weight=1)
		#Menu Bar frame
		self.menuBarFrame = ttk.Frame(self.master, padding="3 3 12 12", style="gray.TFrame")
		self.menuBarFrame.grid(column=0, row=0, sticky=(N, W, E, S))
		self.menuBarFrame.columnconfigure(0, weight=1)
		self.menuBarFrame.rowconfigure(0, weight=1)
		
		#Main window frame
		self.mainFrame = ttk.Frame(self.master, borderwidth=5, relief="raised")
		self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
		self.mainFrame.columnconfigure(0, weight=1)
		self.mainFrame.columnconfigure(1, weight=6)
		self.mainFrame.columnconfigure(2, weight=3)
		self.mainFrame.rowconfigure(0, weight=1)

		#Left frame/ Control Frame
		self.controlFrame = ttk.Frame(self.mainFrame, borderwidth=5, relief="raised") #relief="sunken" or "groove" or "ridge" or "flat" (default)
		self.controlFrame.grid(column=0, row=0, sticky=(N, W, E, S))
		self.controlFrame.columnconfigure(0, weight=1)		
		self.controlFrame.rowconfigure(0, weight=1)
		self.controlFrame.rowconfigure(1, weight=10)
		self.controlFrame.rowconfigure(2, weight=10)
		


		#Left frame Status frame
		self.controlStatus = ttk.Frame(self.controlFrame, borderwidth=5, relief="groove")
		self.controlStatus.grid(column=0, row=0, sticky=(N, W, E, S))
		self.controlStatus.columnconfigure(0, weight=1)	
		self.controlStatus.rowconfigure(0, weight=1)	
		self.controlStatus.rowconfigure(1, weight=1)	

		self.controlStatusConnect = ttk.Frame(self.controlStatus, borderwidth=0)
		self.controlStatusConnect.grid(column=0, row=0, sticky=(N, W, E, S))
		self.controlStatusConnect.rowconfigure(0, weight=1)
		self.controlStatusConnect.columnconfigure(0, weight=1)

		self.controlStatusView =ttk.Frame(self.controlStatus, borderwidth=5, relief="groove")
		self.controlStatusView.grid(column=0, row=1, sticky=(N, W, E, S))
		self.controlStatusView.columnconfigure(0, weight=1)
		self.controlStatusView.columnconfigure(1, weight=10)
		self.controlStatusView.rowconfigure(0, weight=1)
		self.controlStatusView.rowconfigure(1, weight=1)


		#Left frame Frame Automate definition
		##################################################################################################		
		self.controlModeAutomate = ttk.Frame(self.controlFrame, borderwidth=5, relief="groove")
		self.controlModeAutomate.grid(column=0, row=1, sticky=(N, W, E, S))
		self.controlModeAutomate.columnconfigure(0, weight=1)	
				

		self.controlModeAutomate.rowconfigure(0, weight=1)			
		self.controlModeAutomate.rowconfigure(1, weight=1)			
		self.controlModeAutomate.rowconfigure(2, weight=10)
		# self.controlModeManual.rowconfigure(2, weight=10)			
		#Left frame Label frame center
		self.controlModeAutomateLabel = ttk.Frame(self.controlModeAutomate, borderwidth=5, relief="groove")	
		self.controlModeAutomateLabel.grid(column=0, row=0, sticky=(N, W, E, S))								
		self.controlModeAutomateLabel.columnconfigure(0, weight=1)		
		#Left frame Speed control frame definition		
		self.controlModeAutomateControl = ttk.Frame(self.controlModeAutomate, borderwidth=5, relief="groove")	
		self.controlModeAutomateControl.grid(column=0, row=1, sticky=(N, W, E, S))
		self.controlModeAutomateControl.columnconfigure(0, weight=1)	
		self.controlModeAutomateControl.columnconfigure(1, weight=1)	
		self.controlModeAutomateControl.columnconfigure(2, weight=1)	
		self.controlModeAutomateControl.columnconfigure(3, weight=1)
		#Left frame Direction buttons frame definirion
		self.controlModeAutomateFile = ttk.Frame(self.controlModeAutomate, borderwidth=5, relief="groove")	
		self.controlModeAutomateFile.grid(column=0, row=2, sticky=(N, W, E, S))				
		self.controlModeAutomateFile.rowconfigure(0, weight=1)
		self.controlModeAutomateFile.rowconfigure(1, weight=1)
		self.controlModeAutomateFile.rowconfigure(2, weight=1)
		self.controlModeAutomateFile.columnconfigure(0, weight=1)		
		self.controlModeAutomateFile.columnconfigure(1, weight=10)		

		#Track preview
		self.controlModeAutomateTrack = ttk.Frame(self.controlModeAutomateFile, borderwidth=5, relief="groove")	
		self.controlModeAutomateTrack.grid(column=1, row=0, rowspan=3, sticky=(N, W, E, S))	
		self.controlModeAutomateTrack.rowconfigure(0, weight=1)
		self.controlModeAutomateTrack.columnconfigure(0, weight=1)		

		self.controlModeAutomateCanvas = Canvas(self.controlModeAutomateTrack, bg="#ffffff",height=50, width=30, borderwidth=1)
		self.controlModeAutomateCanvas.grid(column=0, row=0, sticky=(N, W, E, S))
		# self.controlModeAutomateCanvas.rowconfigure(0, weight=1)
		# self.controlModeAutomateCanvas.columnconfigure(0, weight=1)			

		##################################################################################################

		#Left frame Frame Manual definition		
		##################################################################################################
		self.controlModeManual = ttk.Frame(self.controlFrame, borderwidth=5, relief="groove")
		self.controlModeManual.grid(column=0, row=2, sticky=(N, W, E, S))		
		self.controlModeManual.columnconfigure(0, weight=1)			
		self.controlModeManual.rowconfigure(0, weight=1)			
		self.controlModeManual.rowconfigure(1, weight=1)			
		self.controlModeManual.rowconfigure(2, weight=10)			
		#Left frame Label frame center
		self.controlModeManualLabel = ttk.Frame(self.controlModeManual, borderwidth=5, relief="groove")	
		self.controlModeManualLabel.grid(column=0, row=0, sticky=(N, W, E, S))								
		self.controlModeManualLabel.columnconfigure(0, weight=1)			
		#Left frame Speed control frame definition
		self.controlModeManualSpeed = ttk.Frame(self.controlModeManual, borderwidth=5, relief="groove")	
		self.controlModeManualSpeed.grid(column=0, row=1, sticky=(N, W, E, S))
		self.controlModeManualSpeed.columnconfigure(0, weight=1)	
		self.controlModeManualSpeed.columnconfigure(1, weight=1)	
		self.controlModeManualSpeed.columnconfigure(2, weight=1)	
		#Left frame Direction buttons frame definirion
		self.controlModeManualControl = ttk.Frame(self.controlModeManual, borderwidth=5, relief="groove")
		self.controlModeManualControl.grid(column=0, row=2, sticky=(N, W, E, S))
		self.controlModeManualControl.columnconfigure(0, weight=1)	
		self.controlModeManualControl.columnconfigure(1, weight=1)	
		self.controlModeManualControl.columnconfigure(2, weight=1)	
		self.controlModeManualControl.rowconfigure(0, weight=1)			
		self.controlModeManualControl.rowconfigure(1, weight=1)			
		self.controlModeManualControl.rowconfigure(2, weight=1)							
		self.controlModeManualControl.rowconfigure(3, weight=1)							
		##################################################################################################
		
		#Central frame/ Canvas frame
		self.canvasFrame = ttk.Frame(self.mainFrame, borderwidth=5, relief="raised") #relief="sunken" or "groove" or "ridge" or "flat" (default)
		self.canvasFrame.grid(column=1, row=0, sticky=(N, W, E, S))
		self.canvasFrame.columnconfigure(0, weight=1)
		self.canvasFrame.rowconfigure(0, weight=1)
		self.canvasFrame.rowconfigure(1, weight=10)
		#Label config
		self.canvasLabel = ttk.Frame(self.canvasFrame, height=20, borderwidth=5, relief="groove")
		self.canvasLabel.grid(column=0, row=0, sticky=(N, W, E, S))
		self.canvasLabel.columnconfigure(0, weight=1)
		#Canvas frame border
		self.canvasFrameBorder = ttk.Frame(self.canvasFrame, borderwidth=5, relief="groove")
		self.canvasFrameBorder.grid(column=0, row=1, sticky=(N, W, E, S))
		self.canvasFrameBorder.columnconfigure(0, weight=1)
		self.canvasFrameBorder.rowconfigure(0, weight=1)
		#Canvas definition
		self.canvasFrameCanvas = Canvas(self.canvasFrameBorder, bg="#ffffff", borderwidth=1) #width=int(dimXMax.get()), height=int(dimYMax.get())
		self.canvasFrameCanvas.grid(column=0, row=0, sticky=(N, W, E, S))
		# self.canvasFrameCanvas.rowconfigure(0, weight=1)
		# self.canvasFrameCanvas.columnconfigure(0, weight=1)	

		#################################################################################################
		#Right frame/ Status frame
		self.statusFrame = ttk.Frame(self.mainFrame, borderwidth=5, relief="raised") #relief="sunken" or "groove" or "ridge" or "flat" (default)
		self.statusFrame.grid(column=2, row=0, sticky=(N, W, E, S))
		self.statusFrame.columnconfigure(0, weight=1)
		self.statusFrame.rowconfigure(0, weight=1)
		self.statusFrame.rowconfigure(1, weight=1)

		#Coord frame
		self.statusCoordFrame = ttk.Frame(self.statusFrame, borderwidth=5, relief="groove")
		self.statusCoordFrame.grid(column=0, row=0, sticky=(N, W, E, S))
		self.statusCoordFrame.columnconfigure(0, weight=1)
		self.statusCoordFrame.rowconfigure(0, weight=1)
		self.statusCoordFrame.rowconfigure(1, weight=1)
		self.statusCoordFrame.rowconfigure(2, weight=1)


		#Coord label
		self.statusCoordLabel = ttk.Frame(self.statusCoordFrame, borderwidth=5, relief="groove")
		self.statusCoordLabel.grid(column=0, row=0, sticky=(N, W, E, S))

		# X label
		self.statusCoordX = ttk.Frame(self.statusCoordFrame, borderwidth=5, relief="groove")
		self.statusCoordX.grid(column=0, row=1, sticky=(N, W, E, S))


		# Y label
		self.statusCoordY = ttk.Frame(self.statusCoordFrame, borderwidth=5, relief="groove")
		self.statusCoordY.grid(column=0, row=2, sticky=(N, W, E, S))			

		#Distance frame
		self.statusDistFrame = ttk.Frame(self.statusFrame, borderwidth=5, relief="groove")
		self.statusDistFrame.grid(column=0, row=1, sticky=(N, W, E, S))	
		self.statusDistFrame.columnconfigure(0, weight=1)
		self.statusDistFrame.rowconfigure(0, weight=1)
		self.statusDistFrame.rowconfigure(1, weight=1)	

		self.statusDistLabel = ttk.Frame(self.statusDistFrame, borderwidth=5, relief="groove")
		self.statusDistLabel.grid(column=0, row=0, sticky=(N, W, E, S))	

		self.statusDist= ttk.Frame(self.statusDistFrame, borderwidth=5, relief="groove")
		self.statusDist.grid(column=0, row=1, sticky=(N, W, E, S))			

	# Create Menu item
	def init_menu(self, new_command=0, open_command=0, save_command=0, saveas_command=0, connect_command=0, disconnect_command=0, start_command=0, pause_command=0, stop_command=0, stop_move=0):
		
		#Menubar object
		menubar = Menu(self.menuBarFrame)
		self.master.config(menu=menubar)

		filemenu = Menu(menubar, tearoff=0)
		# filemenu.add_command(label="New", command=new_command)
		# filemenu.add_command(label="Open", command=open_command)
		# filemenu.add_command(label="Save", command=save_command)
		# filemenu.add_command(label="Save As...", command=saveas_command)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.master.quit)
		menubar.add_cascade(label="File", menu=filemenu)

		projectmenu = Menu(menubar, tearoff=0)
		
		projectmenu.add_command(label="Connect HelloRobo", command=self.connect_command)
		projectmenu.add_command(label="Disconnect HelloRobo", command=self.disconnect_command)

		# projectmenu.add_separator()
		# projectmenu.add_command(label="Start", command=self.start_move)
		# projectmenu.add_command(label="Pause", command=pause_move)
		# projectmenu.add_command(label="Stop", command=stop_move)
		projectmenu.add_separator()
		projectmenu.add_command(label="Emergency Stop", command=self.stop_move)
		menubar.add_cascade(label="Project", menu=projectmenu)

	# Create Left frame Widgets
	def init_control_frame(self):

		#Status Frame
		ttk.Button(self.controlStatusConnect, text="Connect HelloRobo", command=self.connect_command).grid(column=0, row=0, sticky=(N, W, E, S))

		ttk.Label(self.controlStatusView, text="Status: ").grid(column=0, row=0, sticky=(W), padx=6)
		ttk.Label(self.controlStatusView, textvariable = self.status).grid(column=1, row=0,sticky=(W))
		ttk.Label(self.controlStatusView, text="Mode: ").grid(column=0, row=1, sticky=(W), padx=6)
		ttk.Label(self.controlStatusView, textvariable = self.mode).grid(column=1, row=1,sticky=(W))

		#Automate mode frame
		ttk.Radiobutton(self.controlModeAutomateLabel, text="Automate", variable=self.mode, value="automate", command=self.set_mode).grid(column=0, row=0)

		ttk.Label(self.controlModeAutomateControl, text="Control buttons").grid(column=0, row=1)
		ttk.Button(self.controlModeAutomateControl, text="Play", command=self.play_button).grid(column=1, row=1, sticky=(N, W, E, S))
		ttk.Button(self.controlModeAutomateControl, text="Pause", command=self.pause_button).grid(column=2, row=1, sticky=(N, W, E, S))
		ttk.Button(self.controlModeAutomateControl, text="Stop", command=self.stop_button).grid(column=3, row=1, sticky=(N, W, E, S))

		ttk.Button(self.controlModeAutomateFile, text="Load track", command=self.load_track).grid(column=0, row=0, sticky=(N, W, E, S))
		ttk.Button(self.controlModeAutomateFile, text="Save track", command=self.save_track).grid(column=0, row=1, sticky=(N, W, E, S))
		ttk.Button(self.controlModeAutomateFile, text="Recognition",command=self.recognition_track).grid(column=0, row=2, sticky=(N, W, E, S))
		
		points = [15, 10, 20, 12, 50, 18, 21, 20, 15, 15, 10, 20]
		self.controlModeAutomateCanvas.create_polygon(points, fill="#476042")

		
		#Manual mode frame
		ttk.Radiobutton(self.controlModeManualLabel, text="Manual", variable=self.mode, value="manual", command=self.set_mode).grid(column=0, row=0)

		ttk.Label(self.controlModeManualSpeed, text="Speed").grid(column=0, row=0)
		ttk.Radiobutton(self.controlModeManualSpeed, text="Slow", variable=self.speed, value="slow", command=self.set_speed).grid(column=1, row=0)
		ttk.Radiobutton(self.controlModeManualSpeed, text="Fast", variable=self.speed, value="fast", command=self.set_speed).grid(column=2, row=0)
		ttk.Label(self.controlModeManualControl, text="Manual move").grid(column=0, row=0)
		ttk.Button(self.controlModeManualControl, text="FW-LW", command=self.fw_lw_move).grid(column=0, row=1, sticky=(N, W, E, S))
		ttk.Button(self.controlModeManualControl, text="FW", command=self.fw_move).grid(column=1, row=1, sticky=(N, W, E, S))
		ttk.Button(self.controlModeManualControl, text="FW-RW", command=self.fw_rw_move).grid(column=2, row=1, sticky=(N, W, E, S))
		ttk.Button(self.controlModeManualControl, text="LW", command=self.lw_move).grid(column=0, row=2, sticky=(N, W, E, S))
		ttk.Button(self.controlModeManualControl, text="STOP", command=self.stop_move).grid(column=1, row=2, sticky=(N, W, E, S))
		ttk.Button(self.controlModeManualControl, text="RW",command=self.rw_move).grid(column=2, row=2, sticky=(N, W, E, S))
		ttk.Button(self.controlModeManualControl, text="BW-LW", command=self.bw_lw_move).grid(column=0, row=3, sticky=(N, W, E, S))
		ttk.Button(self.controlModeManualControl, text="BW", command=self.bw_move).grid(column=1, row=3, sticky=(N, W, E, S))
		ttk.Button(self.controlModeManualControl, text="BW-RW", command=self.bw_rw_move).grid(column=2, row=3, sticky=(N, W, E, S))
	

	def init_canvas_frame(self):
		ttk.Label(self.canvasLabel, text="Map View").grid(column=0, row=0)
		#Have to implement points coord
		points = [150, 100, 200, 120, 500, 180, 210, 200, 150, 150, 100, 200]
		self.canvasFrameCanvas.create_polygon(points, fill="#476042")


	def init_status_frame(self):


		ttk.Label(self.statusCoordLabel, text="Actual Coordinates").grid(column=0, row=0)
		ttk.Label(self.statusCoordX, textvariable = self.xcoord).grid(column=0, row=1)
		ttk.Label(self.statusCoordY, textvariable = self.ycoord).grid(column=0, row=2)

		#Have to implement distance to obj
		ttk.Label(self.statusDistLabel, text="Distance to Object").grid(column=0, row=0)
		ttk.Label(self.statusDist, textvariable = self.distance).grid(column=0, row=1)

	def styles(self):
		pass

	def connect_command(self):
		print("connected")
		self.status.set("Connected")
	def disconnect_command(self):
		print("disconnected")
		self.status.set("Disconnected")

	def set_mode(self):
		print(self.mode.get())


	def play_button(self):
		print("pressed play")
	def pause_button(self):
		print("pressed pause")
	def stop_button(self):
		print("pressed stop")
	def load_track(self):
		print("load track")
	def save_track(self):
		print("save track")
	def recognition_track(self):
		print("recognition track")

	def set_speed(self):
		print(self.speed.get())

	def fw_move(self):
		print("fw_move")
	def bw_move(self):
		print("bw_move")
	def rw_move(self):
		print("rw_move")
	def lw_move(self):
		print("lw_move")

	def fw_lw_move(self):
		print("fw_lw_move")
	def fw_rw_move(self):
		print("fw_rw_move")
	def bw_lw_move(self):
		print("bw_lw_move")
	def bw_rw_move(self):
		print("bw_rw_move")
	def stop_move(self):
		print("stop")


