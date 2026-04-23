from attrs import define


@define(kw_only=True)
class EventQueue:
    events: list = []

    def pop(self):
        if self.events:
            return self.events.pop(0)
        return None

    def push(self, event):
        self.events.append(event)

    def is_empty(self):
        return len(self.events) == 0

    def size(self):
        return len(self.events)
