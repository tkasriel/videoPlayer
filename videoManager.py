import imageio.v3 as iio
class VideoManager:
	def __init__(self, file_name):
		self.file_name = file_name
		self.videoStream = iio.imiter(file_name, plugin="pyav")
		self.meta = iio.improps(file_name, plugin="pyav")
		# self.

	def nextFrame (self):
		# Output: [x][y] = [R,G,B]
		return next(self.videoStream)