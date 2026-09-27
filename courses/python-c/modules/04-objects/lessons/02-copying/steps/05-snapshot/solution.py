import copy

class Editor:
    def __init__(self):
        self.state = {"lines": []}
        self.history = []

    def snapshot(self):
        self.history.append(copy.deepcopy(self.state))

    def undo(self):
        self.state = self.history.pop()
