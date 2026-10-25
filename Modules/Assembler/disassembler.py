from Modules.hardware.cpu.ControlUnit import ControlUnit
from isa import isa
from Modules.hardware.registers import Registers

class disassembler:

    @staticmethod
    def find_opcode(bits_line):
        bits = bits_line & 0x7F
        opcode = ControlUnit.int_to_code[bits]
        return opcode

    @staticmethod
    def disassemble_to_regs():
        fetch_dic = Registers.get_fetch()
        instruction = fetch_dic["instruction"]
        if instruction:
            opcode = disassembler.find_opcode(instruction)
            cmd_type = ControlUnit.code_to_type[opcode]
            dic = disassembler.disassemble_to_dic(cmd_type,instruction)
            Registers.set_decode(dic) #sets the

    @staticmethod
    def disassemble_to_dic(type, instruction):
        dic = {"opcode": None, "val1":None, "val2":None, "dest":None}
        match type:
            case "R":
                components = isa.Rtype_disassemble(instruction)
                dic["opcode"] = components[0]
                dic["dest"] = components[1]
                dic["val1"] = components[2]
                dic["val2"] = components[3]
            case "I":
                components = isa.Itype_disassemble(instruction)
                dic["opcode"] = components[0]
                dic["dest"] = components[1]
                dic["val1"] = components[2]
                dic["val2"] = components[3]
            case "S":
                components = isa.Stype_disassemble(instruction)
                #doesnt work yet!
            case "U":
                components = isa.Utype_disassemble(instruction)
                dic["opcode"] = components[0]
                dic["dest"] = components[1]
                dic["val1"] = components[2]
        return dic
