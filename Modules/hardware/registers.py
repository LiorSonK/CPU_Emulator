from Modules.hardware.hardware_const import REGISTER_COUNT


class Registers():
    registers = [0] * REGISTER_COUNT #R0 will always equal 0
    special_registers = {"pc":0,
                        "sp":0, # stack pointer + program counter
                        }
    latches = [{"instruction":0},
               {"opcode": "", "val1":0, "val2":0, "dest":None},
               {"opcode":"", "result":0, "dest": None},
               {"opcode":"","mem_data":0, "result":0, "dest": None}] #  0 - instruction fetch , 1 - instruction decode, 2 - execute, 3 - memory
    #latches are pipeline registers
    """each arr spot is related to their relative register
    for ex r0 = register[0] r1 = registers[1] ect..."""

    @staticmethod
    def setreg_value(num, value):
        if num == 0:
            return #register 0 will always be 0
        Registers.registers[num] = value

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
        Registers.latches[0] = dic

    @staticmethod
    def set_decode(opcode, val1, val2, dest):
        dic = {"opcode": opcode, "val1":val1, "val2":val2, "dest":dest}
        Registers.latches[1] = dic

    @staticmethod
    def set_execute(opcode, result, dest):
        dic = {"opcode": opcode, "result": result,"dest": dest}
        Registers.latches[2] = dic

    @staticmethod
    def set_memory(opcode, mem_data, result, dest):
        dic = {"opcode": opcode,"mem_data":mem_data, "result": result, "dest": dest}
        Registers.latches[2] = dic
