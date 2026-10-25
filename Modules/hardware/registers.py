from Modules.hardware.cpu.cpu_consts import fetch_latch, decode_latch, execute_latch, memory_latch
from Modules.hardware.hardware_const import REGISTER_COUNT


class Registers():
    registers = [0] * REGISTER_COUNT #R0 will always equal 0
    special_registers = {"pc":0,
                        "sp":0, # stack pointer + program counter
                        }
    latches = [{"instruction":None},
               {"opcode": None, "val1":None, "val2":None, "dest":None},
               {"opcode":None, "result":None, "dest": None},
               {"opcode":None,"mem_data":None, "result":None, "dest": None}] #  0 - instruction fetch , 1 - instruction decode, 2 - execute, 3 - memory
    #latches are pipeline registers
    """each arr spot is related to their relative register
    for ex r0 = register[0] r1 = registers[1] ect..."""

    @staticmethod
    def setreg_value(reg_num, value):
        if reg_num == 0:
            return #register 0 will always be 0
        Registers.registers[reg_num] = value

    @staticmethod
    def getreg_value(num):
        return Registers.registers[num]

    @staticmethod
    def set_specialreg_value(name: str, value):

        if name in Registers.special_registers:
            Registers.special_registers[name] = value

    @staticmethod
    def get_specialreg_value(name: str):

        if name in Registers.special_registers:
            return Registers.special_registers[name]

    @staticmethod
    def get_fetch():
        return Registers.latches[0]

    @staticmethod
    def get_decode():
        return Registers.latches[1]

    @staticmethod
    def get_alu():
        return Registers.latches[2]

    @staticmethod
    def get_memory():
        return Registers.latches[3]

    @staticmethod
    def set_fetch(instruction):
        dic = {"instruction": instruction}
        Registers.latches[fetch_latch] = dic

    @staticmethod
    def set_decode(dic):
        Registers.latches[decode_latch] = dic

    @staticmethod
    def set_alu(dic):
        Registers.latches[execute_latch] = dic

    @staticmethod
    def set_memory(dic):
        Registers.latches[memory_latch] = dic
