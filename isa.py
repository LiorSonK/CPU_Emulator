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
class isa:

    @staticmethod
    def Rtype_assemble(line: str)->int:
        pass

    @staticmethod
    def Rtype_disassemble(bits_line: int)-> str:
        pass

    @staticmethod
    def Itype_assemble(line: str) -> int:
        pass

    @staticmethod
    def Itype_disassemble(bits_line: int) -> str:
        pass

    @staticmethod
    def Stype_assemble(line: str) -> int:
        pass

    @staticmethod
    def Stype_disassemble(bits_line: int) -> str:
        pass

    @staticmethod
    def Utype_assemble(line: str) -> int:
        pass

    @staticmethod
    def Utype_disassemble(bits_line: int) -> str:
        pass
