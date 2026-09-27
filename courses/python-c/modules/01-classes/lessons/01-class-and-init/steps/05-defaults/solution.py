class Rect:
    def __init__(self, width, height=None):
        self.width = width
        self.height = width if height is None else height
        self.area = self.width * self.height
