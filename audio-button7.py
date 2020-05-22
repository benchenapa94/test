# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import logging
import os
import board
import digitalio
logging.basicConfig(level=logging.INFO)
VIDEO_1_PATH = "bp.mp3"
VIDEO_2_PATH = "bd.mp3"
VIDEO_3_PATH = "bomb.mp3"
player_log = logging.getLogger("Player 1")
player = OMXPlayer(VIDEO_1_PATH,
dbus_name='org.mpris.MediaPlayer2.omxplayer1')
player2 = OMXPlayer(VIDEO_2_PATH,
dbus_name='org.mpris.MediaPlayer2.omxplayer1')
player3 = OMXPlayer(VIDEO_3_PATH,
dbus_name='org.mpris.MediaPlayer2.omxplayer1')
player0 = OMXPlayer('VIDEO_1_PATH', args=['--no-osd'], dbus_name='org.mpris.MediaPlayer2.omxplayer' + str(0))
player0.pause()
player0.hide_video()

player1 = OMXPlayer('VIDEO_2_PATH', args=['--no-osd'], dbus_name='org.mpris.MediaPlayer2.omxplayer' + str(0))
player1.pause()
player1.hide_video()

player2 = OMXPlayer('VIDEO_3_PATH', args=['--no-osd'], dbus_name='org.mpris.MediaPlayer2.omxplayer' + str(0))
player2.pause()
player2.hide_video()
print("press a button!")

button1 = digitalio.DigitalInOut(board.D23)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D24)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

while True:
    # omxplayer -o local <file>
    # omxplayer -o hdmi <file>
    # omxplayer -o both <file>
    if not button1.value:
player0.play()
Player2.play()
  
    if not button2.value:
player2.stop()
Player1.play()
