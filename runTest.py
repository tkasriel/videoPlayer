import videoManager as vm
import window as ww
import tkinter as tk
import time

fileName = "test.mp4"

print (f"Testing with {fileName}")
# Test videoManager
video = vm.VideoManager(fileName)

lastTime = time.time()
for i in range(1000):
	out = video.nextFrame()
	print (f"Loaded frame in {time.time()-lastTime}s")
	lastTime = time.time()

# print (video.meta)

# Test windowManager
# root = tk.Tk()
# window = ww.Window(root)
# window.drawVideoFrame(out)