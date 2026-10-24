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
                    val1 = Ram.ram[val1]
                    val2 = Ram.ram[val2]
                    result = alu.binary_add(val1,val2)
                case "sub":
                    val1 = Ram.ram[val1]
                    val2 = Ram.ram[val2]
                    result = alu.binary_sub(val1, val2)
                case "jmp":
                    result = val1
                    dic["dest"] = "pc"
                case "addi":
                    val1 = Ram.ram[val1]
                    result = alu.binary_add(val1, val2)
                case "subi":
                    val1 = Ram.ram[val1]
                    result = alu.binary_sub(val1, val2)
                case "beq": #a bit complex so an explanation:
                    #if the values are equal we are jumping to the dest stored in the dest register
                    #so we set the result to where we want to jump
                    #and the dest to the program counter (:
                    val1 = Ram.ram[val1]
                    val2 = Ram.ram[val2]
                    result = None
                    dest = Ram.ram[dest]
                    if val1 == val2:
                        result = dest
                    dic["dest"] = "pc"
                #just the poc! other branching types will be added soon.
            dic["result"] = result

        else:
            dic = {"opcode":opcode, "result":val1, "dest": dest}
        Registers.set_execute(dic)


    @staticmethod
    def memory():
        opcode = Registers.get_alu()["opcode"]
        dest = Registers.get_alu()["dest"]
        val1 = Registers.get_alu()["val1"]
        memory_buffer = MEGABYTE/2
        dic = Registers.get_alu()
        dic["mem_data"] = None
        if opcode in needs_memo:
            match opcode:
                case "store":
                    Ram.write_ram(memory_buffer + dest, val1)
                case "load":
                    dic["mem_data"] = Ram.read_ram(memory_buffer + dest)

        Registers.set_memory(dic)

    @staticmethod
    def writeback():
        pass