communication_queue = []

class EventHandler:
    def __init__(self):
        self.events_map = {}

    def register_handler(self, event_name, handler_function):
        if event_name not in self.events_map:
            self.events_map[event_name] = []
        self.events_map[event_name].append(handler_function)

    def emit(self, event_name, event):
        if event_name in self.events_map:
            for handler in self.events_map[event_name]:
                handler(event)
