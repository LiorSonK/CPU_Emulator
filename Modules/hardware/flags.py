class Flags:

    def __init__(self):
        self.zero = 0
        self.negative = 0

    def enable_zero(self):
        self.zero = 1

    def disable_zero(self):
        self.zero = 0

    def enable_negative(self):
        self.negative = 1

    def disable_negative(self):
        self.negative = 0