from distutils.command.register import register

from scapy.contrib.roce import opcode

from Modules.hardware.hardware_const import MEGABYTE
from Modules.hardware.registers import Registers
from Modules.hardware.ram import Ram
from Modules.Assembler.disassembler import disassembler
from Modules.alu.alu import alu
from Modules.hardware.cpu.cpu_consts import *
from Modules.hardware.flags import Flags
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
        opcode = Registers.get_decode()["opcode"]
        val1 = Registers.get_decode()["val1"]
        val2 = Registers.get_decode()["val2"]
        dest = Registers.get_decode()["dest"]
        dic = {}
        if opcode in need_execute:
            dic = {"opcode":opcode, "result":None, "dest": dest}
            result = 0
            match opcode:
                case "add":
                    val1 = Registers.getreg_value(val1)
                    val2 = Registers.getreg_value(val2)
                    result = alu.binary_add(val1,val2)
                case "sub":
                    val1 = Registers.getreg_value(val1)
                    val2 = Registers.getreg_value(val2)
                    result = alu.binary_sub(val1, val2)
                case "jmp":
                    result = val1
                    dic["dest"] = "pc"
                case "addi":
                    val1 = Registers.getreg_value(val1)
                    result = alu.binary_add(val1, val2)
                case "subi":
                    val1 = Registers.getreg_value(val1)
                    result = alu.binary_sub(val1, val2)
                case "beq": #a bit complex so an explanation:
                    #if the values are equal we are jumping to the dest stored in the dest register
                    #so we set the result to where we want to jump
                    #and the dest to the program counter (:
                    val1 = Registers.getreg_value(val1)
                    val2 = Registers.getreg_value(val2)
                    result = None
                    dest = Registers.getreg_value(dest)
                    if val1 == val2:
                        result = dest
                    dic["dest"] = "pc"
                #just the poc! other branching types will be added soon.
            dic["result"] = result

        else:
            dic = {"opcode":opcode, "result":Registers.getreg_value(val1), "dest": dest}
        Registers.set_execute(dic)


    @staticmethod
    def memory():
        opcode = Registers.get_alu()["opcode"]
        dest = Registers.get_alu()["dest"]
        result = Registers.get_alu()["result"]
        memory_buffer = MEGABYTE/2
        dic = Registers.get_alu()
        dic["mem_data"] = None
        if opcode in needs_memo:
            match opcode:
                case "store":
                    Ram.write_ram(memory_buffer + Registers.getreg_value(dest), Registers.getreg_value(result))
                case "load":
                    dic["mem_data"] = Ram.read_ram(memory_buffer + Registers.getreg_value(result))

        Registers.set_memory(dic)

    @staticmethod
    def writeback():
        opcode = Registers.get_memory()["opcode"]
        dest = Registers.get_memory()["dest"]
        result = Registers.get_memory()["result"]
        mem_data = Registers.get_memory()["mem_data"]
        memory_buffer = MEGABYTE / 2
        if mem_data:
            Ram.write_ram(memory_buffer + Registers.getreg_value(dest), mem_data)
        else:
            Registers.setreg_value(Registers.getreg_value(dest),result)