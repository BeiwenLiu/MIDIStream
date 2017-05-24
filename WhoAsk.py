import MyEvent

import pygame
import time

TARGET_FPS = 60

accumulator = 0

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



#------------------------------------------------------------------------------
def start(beat):
    beat = 1000*float(1/float(beat/60))
    clock = pygame.time.Clock()

    while True:
        timeChange = clock.tick(TARGET_FPS) #time change between each frame. TARGET_FPS is 60 so on average there should be 50-60 miliseconds per frame
        Tick(timeChange,beat)

class WhoAsk( object ):
    """
    First class which ask who is listening to it
    """
    def __init__(self, event_dispatcher):
        # Save a reference to the event dispatch
        self.event_dispatcher = event_dispatcher

        # Listen for the RESPOND event type
        self.event_dispatcher.add_event_listener(
            MyEvent.MyEvent.RESPOND, self.on_answer_event
        )

    def Tick(self,timeChange,beat):
        global accumulator

        accumulator += timeChange
        if accumulator > beat:
            accumulator = accumulator - beat
            Numeral.beat()
            self.event_dispatcher.dispatch_event(
                MyEvent.MyEvent( MyEvent.MyEvent.ASK, self ) #sends out signal. MyEvent.MyEvent.ASK is just an agreed upon constant to look for when receiving
            )

    def ask(self):
        """
        Dispatch the ask event
        """
        print ">>> I'm instance {0}. Who are listening to me ?".format( self )

        beat = 1000
        clock = pygame.time.Clock()

        while True:
            timeChange = clock.tick(TARGET_FPS) #time change between each frame. TARGET_FPS is 60 so on average there should be 50-60 miliseconds per frame
            self.Tick(timeChange,beat)

    def on_answer_event(self, event):
        """
        Event handler for the RESPOND event type
        """
        print "<<< Thank you instance {0}".format( event.data )