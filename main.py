import videoManager as vm
import window as ww
import tkinter as tk

import time
class Main:
	def __init__(self):
		self.root = tk.Tk()
		self.window = ww.Window(self.root)
		file = self.window.requestFile()
		if file:
			self.currVideo = vm.VideoManager(file)
		else:
			sys.exit(0)

	def runVideo(self):
		fps = self.currVideo.meta["fps"]
		prevTime = time.time()
		# Admire this in its full 4 fps beauty
		while True:
			frame = self.currVideo.nextFrame()
			self.window.drawVideoFrame(frame)
			remainingTickTime = max(1/fps - (time.time() - prevTime), 0)
			time.sleep(remainingTickTime)
			prevTime = time.time()


main = Main()
main.runVideo()