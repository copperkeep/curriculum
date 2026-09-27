class LoggedList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.log = []

    def append(self, x):
        self.log.append(x)
        super().append(x)
