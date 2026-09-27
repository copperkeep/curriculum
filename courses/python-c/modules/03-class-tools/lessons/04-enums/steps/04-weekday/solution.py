from enum import Enum, auto

class Day(Enum):
    MON = auto()
    TUE = auto()
    WED = auto()
    THU = auto()
    FRI = auto()
    SAT = auto()
    SUN = auto()

    def is_weekend(self):
        return self in (Day.SAT, Day.SUN)
