class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        return f"{self.username} of type {self.get_class_name()} has level {self.level}"

    @classmethod
    def get_class_name(cls):
        return cls.__name__
