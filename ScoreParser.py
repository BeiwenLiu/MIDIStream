import MyEvent

class ScoreParser( object ):
    """
    Second class who respond to ASK events
    """
    def __init__(self, event_dispatcher):
        # Save event dispatcher reference
        self.event_dispatcher = event_dispatcher

        # Listen for ASK event type
        self.event_dispatcher.add_event_listener(
            MyEvent.MyEvent.ASK, self.on_ask_event
        )

    def on_ask_event(self, event):
        """
        Event handler for ASK event type
        """
        