
import OpenGL
# OpenGL.ERROR_CHECKING = False
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Window ():

	def __init__(self, width, height, initFrame=None):
		'''
		Handles the window element.
		Inputs:
		- width (int)
		- height (int)
		- initFrame (bytearray)

		TODO: Use glfw instead of GLUT so that I can have main.py as the main function
		'''
		self.displayMode = GLUT_RGBA
		self.width = width
		self.height = height
		self.currFrame = initFrame

		glutInit()
		glutInitDisplayMode(self.displayMode)
		glutInitWindowSize(width, height)
		glutInitWindowPosition(0,0)
		self.window = glutCreateWindow("VideoPlayer")
		glutDisplayFunc(self.renderScreen)

		glutPostRedisplay()
		glutMainLoop()

	def createTexture(self):

		# I have no clue what I'm doing help
		texture_id = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, texture_id)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glPixelStorei(GL_PACK_ALIGNMENT, 1)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.currFrame)
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
		'''Define border to projection'''
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(0, 500, 0, 500)
		glMatrixMode(GL_TEXTURE)
		glLoadIdentity()
		gluOrtho2D(0, 500, 0, 500)
		glMatrixMode (GL_MODELVIEW)
		glLoadIdentity()

	def renderScreen(self):
		if (not self.currFrame):
			raise ValueError("Frame is empty")
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		self.setFrame()
		self.createFrame()
		glutSwapBuffers()

if __name__ == "__main__":
	# Testing
	import random
	frame = bytearray(600*500*4)
	for i in range(600*500*4):
		frame[i] = random.randint(0, 255)
	win = Window(600, 500, frame)
