"""
This file is both informative and used for the decoding.
In my cpu design I have 4 formats of assembling/disassembling.
r,i,s,u
In the next 4 lines each one of the will be explained by BITS in this format:
(range) (register/imm/opcode), (range) (register/imm/opcode), ect...
(imm is short for immediate)
R - 0-6 opcode, 7-12 rd, 13-18 rs1, 19-24 rs2,25-31 func
I - 0-6 opcode, 7-12 rd, 13-18 rs1, 19-31 imm
S - 0-6 opcode, 7-12 imm, 13-18 rs1, 19-24 rs2, 25-31 imm
U - 0-6 opcode, 7-12 rd, 13-31 imm
"""
from Modules.hardware.cpu.ControlUnit import ControlUnit
class isa:

    @staticmethod
    def Rtype_assemble(line: str)->int:
        final =0
        opcode, rest = line.split(" ",1)
        rd,rs1,rs2 = rest.split(",")
        opcode = ControlUnit.code_to_int[opcode]
        rd,rs1,rs2 = int(rd.strip()[1:]),int(rs1.strip()[1:]),int(rs2.strip()[1:])
        final = final<<7 #func

        final = (final<<6) | rs2

        final = (final << 6) | rs1

        final = (final << 6) | rd

        final = (final << 7) | opcode

        return final

    @staticmethod
    def Rtype_disassemble(bits_line: int):

        opcode = bits_line & 0x7F
        bits_line = bits_line >> 7

        rd = bits_line & 0x3F
        bits_line = bits_line >> 6

        rs1 = bits_line & 0x3F
        bits_line = bits_line >> 6

        rs2 = bits_line & 0x3F
        bits_line = bits_line >> 6

        function = bits_line & 0x7F

        return opcode,rd,rs1,rs2

    @staticmethod
    def Itype_assemble(line: str) -> int:
        final = 0
        opcode, rest = line.split(" ", 1)
        rd, rs1, imm = rest.split(",")
        opcode = ControlUnit.code_to_int[opcode]
        rd, rs1, imm = int(rd.strip()[1:]), int(rs1.strip()[1:]), int(imm)
        final = (final << 13) | imm

        final = (final << 6) | rs1

        final = (final << 6) | rd

        final = (final << 7) | opcode

        return final

    @staticmethod
    def Itype_disassemble(bits_line: int):
        opcode = bits_line & 0x7F
        bits_line = bits_line >> 7

        rd = bits_line & 0x3F
        bits_line = bits_line >> 6

        rs1 = bits_line & 0x3F
        bits_line = bits_line >> 6

        imm = bits_line & 0x1FFF

        return opcode, rd, rs1, imm

    @staticmethod
    def Stype_assemble(line: str) -> int: #skipping s-type for now
        pass

    @staticmethod
    def Stype_disassemble(bits_line: int): #skipping s-type for now
        pass

    @staticmethod
    def Utype_assemble(line: str) -> int:
        final = 0
        opcode, rest = line.split(" ", 1)
        rd, imm = rest.split(",")
        opcode = ControlUnit.code_to_int[opcode]
        rd, imm = int(rd.strip()[1:]), int(imm)
        final = (final << 19) | imm

        final = (final << 6) | rd

        final = (final << 7) | opcode

        return final

    @staticmethod
    def Utype_disassemble(bits_line: int):
        opcode = bits_line & 0x7F
        bits_line = bits_line >> 7

        rd = bits_line & 0x3F
        bits_line = bits_line >> 6

        imm = bits_line & 0x7FFFF

        return opcode, rd, imm
