import EventDispatcher
import Metronome
import WhoRespond
# Create and instance of event dispatcher
dispatcher = EventDispatcher.EventDispatcher()

# Create an instance of WhoAsk class and two instance of WhoRespond class
metronome = Metronome.Metronome( dispatcher )

who_responde1 = WhoRespond.WhoRespond( dispatcher )
who_responde2 = WhoRespond.WhoRespond( dispatcher )

# WhoAsk ask :-)
metronome.startTick()