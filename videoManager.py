import imageio.v3 as iio
class VideoManager:
	def __init__(self, file_name):
		self.file_name = file_name
		self.currFrame = 0
		self.meta = iio.immeta(file_name, plugin="pyav")

	def nextFrame (self):
		# Output: [x][y] = [R,G,B]
		image = iio.imread(
    		self.file_name,
    		index=self.currFrame,
    		plugin="pyav",
		)
		self.currFrame += 1
		return image

	def changeFrame(self, frame):
		self.currFrame = frame