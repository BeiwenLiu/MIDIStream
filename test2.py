import EventDispatcher
import Metronome
import ScoreParser

sheetFile = 'page1.xml'
# Create and instance of event dispatcher
dispatcher = EventDispatcher.EventDispatcher()

# Create an instance of WhoAsk class and two instance of WhoRespond class
metronome = Metronome.Metronome( dispatcher )

scoreParser = ScoreParser.ScoreParser(dispatcher,sheetFile)

# WhoAsk ask :-)
metronome.startTick()