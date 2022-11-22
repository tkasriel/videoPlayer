import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import numpy as np
from PIL import Image, ImageTk


class Window (object):
	FRAMEHEIGHT=720
	FRAMEWIDTH=1280
	SUPPORTED = [("Video", ".mp4 .mov")]
	def __init__(self, master):
		super().__init__()
		# Set up window
		master.geometry(f"{Window.FRAMEWIDTH}x{Window.FRAMEHEIGHT}")
		self.videoCanvas = tk.Canvas(master, bg="black",width=Window.FRAMEWIDTH,height=Window.FRAMEHEIGHT)
		self.videoCanvas.pack(side=tk.TOP)
		self.frameImage = None
		self.currFrame = self.videoCanvas.create_image(10, 10, image=self.frameImage)

	def drawVideoFrame(self, image):
		if type (image) != np.ndarray:
			raise ValueError(f"Frame of type {type(image)}, should be np.ndarray")
		if len(image) == 0 or len(image[0]) == 0:
			raise ValueError(f"Image cannot be blank")

		# Convert image to pillow Image
		frame = Image.fromarray(image)
		frame = frame.resize((Window.FRAMEWIDTH, Window.FRAMEHEIGHT))
		self.frameImage = ImageTk.PhotoImage(frame)
		
		# Render image
		self.videoCanvas.delete("all")
		self.currFrame = self.videoCanvas.create_image(Window.FRAMEWIDTH//2, Window.FRAMEHEIGHT//2, image=self.frameImage)
		self.videoCanvas.config(width=frame.size[0], height=frame.size[1])

		self.videoCanvas.update()

	def requestFile (self):
		filename = fd.askopenfilename(title="Please choose the video", filetypes=Window.SUPPORTED)
		return filename
