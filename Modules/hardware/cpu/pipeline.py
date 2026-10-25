from Modules.hardware.cpu.cpu import cpu
from startup import startup
from Modules.hardware.registers import Registers
class pipeline:
    @staticmethod
    def clock_cycle():
        if startup.debug == True:
            print(f"writing {Registers.get_memory()} to regs")
        cpu.writeback()
        cpu.memory()
        if startup.debug == True:
            print(f"memory: {Registers.get_memory()}")
        cpu.execute()
        if startup.debug == True:
            print(f"alu: {Registers.get_alu()}")
        cpu.decode()
        if startup.debug == True:
            print(f"decode: {Registers.get_decode()}")
        cpu.fetch()
        if startup.debug == True:
            print(f"fetched: {Registers.get_fetch()}")