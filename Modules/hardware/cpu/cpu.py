from Modules.hardware.registers import Registers
from Modules.hardware.ram import Ram
class cpu:

    @staticmethod
    def fetch(register: Registers)->int:

        slot = register.get_specialreg_value("pc")
        value = Ram.read_ram(slot)
        register.set_specialreg_value("pc", slot+1)
        return value

    @staticmethod
    def decode():
        pass

    @staticmethod
    def execute():
        pass

    @staticmethod
    def memory():
        pass

    @staticmethod
    def writeback():
        pass