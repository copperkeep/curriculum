class Settings:
    def __init__(self):
        self.theme = "light"
        self.size = 12

# Write apply(settings, changes) that sets each attribute named in the dict
# changes, ignoring names Settings does not already have. Return the list of
# names that were ignored.
