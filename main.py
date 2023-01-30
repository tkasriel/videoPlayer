import videoManager as vm
import window as ww
import tkinter as tk
import io
import sys
import glfw

import time
class Main:
	def __init__(self):
		fileName = ""
		if len(sys.argv) < 2:
			fileName = "test.mp4"
			# raise Exception ("Please enter the ")
		else:
			fileName = sys.argv[1]

		if fileName:
			self.currVideo = vm.VideoManager(fileName)
		else:
			sys.exit(0)

		initFrame = self.currVideo.nextFrame()
		print(initFrame.shape)

		self.window = ww.Window(initFrame.shape[1], initFrame.shape[0], )

	def runVideo(self):
		fps = self.currVideo.meta["fps"]
		prevTime = time.time()

		# Admire this in its full 4 fps beauty
		while not glfw.window_should_close(self.window.window):
			currFrame = self.currVideo.nextFrame()[::-1]
			img_byte_arr = currFrame.tobytes()
			# currFrame.save(img_byte_arr, format='PNG')
			# img_byte_arr = img_byte_arr.getvalue()

			self.window.currFrame = img_byte_arr
			self.window.renderScreen()
			glfw.poll_events()

			# Time-related stuff
			print (f"FPS: {1/(time.time()-prevTime)}; targe: {fps}")
			remainingTickTime = max(1/fps - (time.time() - prevTime), 0)
			time.sleep(remainingTickTime)
			prevTime = time.time()
		glfw.terminate()			
			


main = Main()
main.runVideo()