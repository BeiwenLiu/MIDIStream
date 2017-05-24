import Event

class MyEvent( Event.Event ):
    """
    When subclassing Event class the only thing you must do is to define
    a list of class level constants which defines the event types and the
    string associated to them
    """

    ASK     = "askMyEvent"
    RESPOND = "respondMyEvent"