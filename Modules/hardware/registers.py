from Modules.hardware.hardware_const import REGISTER_COUNT


class Registers():
    def __init__(self):
        self.registers = [0] * REGISTER_COUNT #R0 will always equal 0
        self.special_registers = {"pc":0,
                                  "sp":0} # stack pointer + program counter
        """each arr spot is related to their relative register
        for ex r0 = register[0] r1 = registers[1] ect..."""