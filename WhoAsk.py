import MyEvent

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

    def ask(self):
        """
        Dispatch the ask event
        """
        print ">>> I'm instance {0}. Who are listening to me ?".format( self )

        self.event_dispatcher.dispatch_event(
            MyEvent.MyEvent( MyEvent.MyEvent.ASK, self )
        )

    def on_answer_event(self, event):
        """
        Event handler for the RESPOND event type
        """
        print "<<< Thank you instance {0}".format( event.data )