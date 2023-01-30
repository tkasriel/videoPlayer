
import OpenGL
# OpenGL.ERROR_CHECKING = False
from OpenGL.GL import *
import glfw
from OpenGL.GLU import *


class Window ():

	def __init__(self, width, height, initFrame=None):
		'''
		Handles the window element.
		Inputs:
		- width (int)
		- height (int)
		- initFrame (bytearray)

		
		'''
		self.displayMode = GL_RGB
		self.width = width
		self.height = height
		self.currFrame = initFrame

		if not glfw.init():
			raise Exception("GLFW could not be instantiated")

		self.window = glfw.create_window(self.width, self.height, "Video Player", None, None)

		if not self.window:
			glfw.terminate()
			raise Exception ("Window could not be created")

		glfw.make_context_current(self.window)

	def createTexture(self):

		# I have no clue what I'm doing help
		texture_id = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, texture_id)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glPixelStorei(GL_PACK_ALIGNMENT, 1)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		glTexImage2D(GL_TEXTURE_2D, 0, self.displayMode, self.width, self.height, 0, self.displayMode, GL_UNSIGNED_BYTE, self.currFrame)
		return texture_id

	def createFrame(self):
		'''Bind texture to quad'''
		glEnable(GL_TEXTURE_2D)
		texture_id = self.createTexture()
		glBindTexture(GL_TEXTURE_2D, texture_id)
		glBegin(GL_QUADS)

		glTexCoord2f(0,0)
		glVertex2f(0,0)

		glTexCoord2f(0, 500)
		glVertex2f(0, 500)

		glTexCoord2f(500, 500)
		glVertex2f(500, 500)

		glTexCoord2f(500, 0)
		glVertex2f(500,0)

		glEnd()
		glDisable(GL_TEXTURE_2D)


	def setFrame(self):
		'''Define border for textures'''
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(0, 500, 0, 500)
		glMatrixMode(GL_TEXTURE)
		glLoadIdentity()
		gluOrtho2D(0, 1000, 0, 1000)
		glMatrixMode (GL_MODELVIEW)
		glLoadIdentity()

	def renderScreen(self):
		if (not self.currFrame):
			raise ValueError("Frame is empty")
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		self.setFrame()
		self.createFrame()
		glfw.swap_buffers(self.window)

if __name__ == "__main__":
	# Testing
	import colorsys
	import random
	import time
	offset = 0

	def createFrame():
		frame = bytearray(600*500*3)
		for i in range(0, 600*500*3, 3):

			col = (i//3) % 600 + offset
			row = (i//3) // 600
			r,g,b = colorsys.hsv_to_rgb(col/600, (row/500) % 1, 1)
			# print (g * 255)
			frame[i] = int(r*255)
			frame[i+1] = int(g*255)
			frame[i+2] = int(b*255)
		return frame

	
	win = Window(600, 500)
	frame = createFrame()
	offset += 10
	frame2 = createFrame()
	lastFrameTime = time.time()
	while not glfw.window_should_close(win.window):
		win.currFrame = createFrame()
		win.renderScreen()
		glfw.poll_events()
		offset += 10
		print ("Frame time: " + str(time.time() - lastFrameTime))
		lastFrameTime = time.time()
	glfw.terminate()


