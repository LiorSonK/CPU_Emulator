from Modules.hardware.hardware_const import MEGABYTE

class Ram:
    def __init__(self):
        ram = [0]*MEGABYTE
        #first half of the ram is for the commands and the second is for storing ect, the stack is a kilobyte from the end of the ram, ram[-1025:-1]