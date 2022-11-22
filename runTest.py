import videoManager as vm
import window as ww

fileName = "test.mp4"

print (f"Testing with {fileName}")
# Test videoManager
video = vm.VideoManager(fileName)
out = video.nextFrame()

# Test windowManager
window = ww.Window()
window.drawVideoFrame(out)