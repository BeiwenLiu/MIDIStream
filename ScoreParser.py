import MyEvent
from music21 import *

class ScoreParser( object ):
    """
    Second class who respond to ASK events
    """

    def __init__(self, event_dispatcher, sheetFile):
        # Save event dispatcher reference
        self.measureCounter = 0
        self.event_dispatcher = event_dispatcher
        self.sheetFile = sheetFile
        self.c = self.initializeSheets()

        # Listen for ASK event type
        self.event_dispatcher.add_event_listener(
            MyEvent.MyEvent.ASK, self.on_ask_event
        )

    def on_ask_event(self, event):
        """
        Event handler for ASK event type
        """
        self.measureCounter += 1
        self.analyze(self.measureCounter)


    def initializeSheets(self):
        return converter.parse(self.sheetFile)

    def analyze(self, measureCounter):
        m = self.c.parts[0].measure(measureCounter)

        print "measure : ", measureCounter
        for notes in m.flat:
            if type(notes) is note.Note or type(notes) is chord.Chord:
                print notes
                print notes.offset


