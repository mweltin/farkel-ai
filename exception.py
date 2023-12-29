class InvalidNumberOfDice(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "Number of dice must be between 1-6, {0} ".format(self.message)
        else:
            return "Number of dice must be between 1-6"

class InvalidDieValue(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "All values must be positive integers between 1-6, {0} ".format(self.message)
        else:
            return "All values must be positive integers between 1-6"