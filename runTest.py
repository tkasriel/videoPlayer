import videoManager as vm
import window as ww
import tkinter as tk

fileName = "test.mp4"

print (f"Testing with {fileName}")
# Test videoManager
video = vm.VideoManager(fileName)
out = video.nextFrame()
print (video.meta)

# Test windowManager
root = tk.Tk()
window = ww.Window(root)
window.drawVideoFrame(out)