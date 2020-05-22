
import pygame.mixer #calling for pygame mixer to play audio files
import time         #calling for time to provide delays in program
import RPi.GPIO as IO  #calling for header file which helps in using GPIO’s of PI

IO.setwarnings(False)  #do not show any warnings
IO.setmode(IO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN29 as'GPIO5')

IO.setup(21, IO.IN)  #initialize GPIO21 as an input
IO.setup(20, IO.IN)  #initialize GPIO20 as an input
IO.setup(16, IO.IN)  #initialize GPIO16 as an input
IO.setup(12, IO.IN)  #initialize GPIO12 as an input
IO.setup(25, IO.IN)  #initialize GPIO25 as an input
IO.setup(23, IO.IN)  #initialize GPIO23 as an input

pygame.mixer.init(48000, -16, 1, 1024)  #initializing audio mixer

audio1 = pygame.mixer.Sound("bomb.mp3")      #calling for audio file
audio2 = pygame.mixer.Sound("bp.mp3")  #calling for audio file
audio3 = pygame.mixer.Sound("bd.mp3")      #calling for audio file
audio4 = pygame.mixer.Sound("ahem_x.wav")      #calling for audio file
audio5 = pygame.mixer.Sound("clap.wav")
audio6 = pygame.mixer.Sound("baseball_hit.wav")

channel1 = pygame.mixer.Channel(1)   #using channel one for first button
channel2 = pygame.mixer.Channel(2)   #using channel two for second button
channel3 = pygame.mixer.Channel(3)    #using channel three for second button
channel4 = pygame.mixer.Channel(4)   #using channel four for second button
channel5 = pygame.mixer.Channel(5)   #using channel five for second button
channel6 = pygame.mixer.Channel(6)   #using channel six for second button

while 1:  #execute loop forever
    if (IO.input(21) == 0):
        channel1.play(audio1)          #if button one is pressed(grounded) play audio file one

    if (IO.input(20) == 0):
        channel2.play(audio2)          #if button two is pressed(grounded) play second audio file

    if (IO.input(16) == 0):
        channel3.play(audio3)          #if button three is pressed(grounded) play third audio file

    if (IO.input(12) == 0):
        channel4.play(audio4)

    if (IO.input(25) == 0):
        channel5.play(audio5)

    if (IO.input(23) == 0):
        channel6.play(audio6)

    time.sleep(.01)  #sleep for 100ms
