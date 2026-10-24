from Modules.hardware.registers import Registers
from Modules.hardware.ram import Ram
from  Modules.Assembler.disassembler import disassembler
class cpu:

    @staticmethod
    def fetch(register: Registers):
        slot = register.get_specialreg_value("pc")
        value = Ram.read_ram(slot)
        register.set_fetch(value)

    @staticmethod
    def decode():
        disassembler.disassemble_to_regs()

    @staticmethod
    def execute():
        pass

    @staticmethod
    def memory():
        pass

    @staticmethod
    def writeback():
        pass