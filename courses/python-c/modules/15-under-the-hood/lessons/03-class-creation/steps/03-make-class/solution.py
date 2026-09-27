def _norm(self):
    return (self.x * self.x + self.y * self.y) ** 0.5

Point = type("Point", (), {"x": 0, "y": 0, "norm": _norm})
