class Robot:
    count = 0

    def __init__(self, name):
        Robot.count += 1
        self.name = name
        self.serial = Robot.count
