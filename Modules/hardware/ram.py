from Modules.hardware.hardware_const import MEGABYTE

class Ram:
    ram = [0]*MEGABYTE
    #first half of the ram is for the commands and the second is for storing ect, the stack is a kilobyte from the end of the ram, ram[-1025:-1]

    @staticmethod
    def write_ram(spot: int, value: int):
        Ram.ram[spot] = value

    @staticmethod
    def read_ram(spot: int):
        return  Ram.ram[spot]