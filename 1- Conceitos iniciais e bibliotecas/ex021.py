import winsound
winsound.init()
winsound.mixer.music.load('ex021.mp3')
winsound.mixer.music.play()
winsound.event.wait()
