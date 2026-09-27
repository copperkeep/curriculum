class Command:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Command.registry[cls.__name__.lower()] = cls

class Hello(Command):
    def run(self):
        return "hi"

class Bye(Command):
    def run(self):
        return "bye"
