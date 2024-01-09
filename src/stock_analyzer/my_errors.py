class InputError(Exception):
    def __init__(self, name, value):
        super(InputError, self).__init__()
        self.name = name
        self.value = value

    def __str__(self):
        return "Invalid input {}: {}".format(self.name, self.value)
