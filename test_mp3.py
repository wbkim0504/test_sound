
import pygame
import time
import datetime

print datetime.datetime.now()

pygame.mixer.init()
pygame.mixer.music.load('siren.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

print 'playing ... '

#time.sleep(2.0)

for i in range(0,10):
	print 'is busy ? ', pygame.mixer.music.get_busy()
	time.sleep(0.2)
	if i == 8:
		print datetime.datetime.now()
		pygame.mixer.music.stop()
		





