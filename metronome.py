import pygame
import time

TARGET_FPS = 60

accumulator = 0

last_press = None
last_deltas = None

#------------------------------------------------------------------------------
class Numeral:
    beat_index = 0
    beats = ['1', '2', '3', '4']
        
    @classmethod
    def beat(cls):
        cls.beat_index += 1
        cls.beat_index %= len(cls.beats)
        print cls.beat_index



#------------------------------------------------------------------------------
def Tick(timeChange,beat):
    global accumulator

    accumulator += timeChange
    if accumulator > beat:
        accumulator = accumulator - beat
        Numeral.beat()

#------------------------------------------------------------------------------
def start(beat):
    beat = 1000*float(1/float(beat/60))
    pygame.init()
    clock = pygame.time.Clock()

    while True:
        timeChange = clock.tick(TARGET_FPS) #time change between each frame. TARGET_FPS is 60 so on average there should be 50-60 miliseconds per frame

        remainingEvents = pygame.event.get()

        Tick(timeChange,beat)


