import pygame
from gpiozero import Button

pygame.init()

drum = pygame.mixer.Sound("/home/pi/bomb.mp3")
cymbal = pygame.mixer.Sound("/home/pi/bd.mp3")
snare = pygame.mixer.Sound("/home/pi/bp.mp3")

btn_drum = Button(23)
btn_cymbal = Button(24)
btn_snare= Button(27)

btn_drum.when_pressed = drum.play
btn_cymbal.when_pressed = drum.stop, cymbal.play
btn_snare.when_pressed = snare.play
