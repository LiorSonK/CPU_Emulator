from Modules.file_handler.file_handle import file_handle
from Modules.hardware.cpu.ControlUnit import ControlUnit
from isa import isa
from Modules.hardware.ram import Ram
from startup import startup
class assembler:

    @staticmethod
    def assemble_into_ram():
        ranges = []
        starting_spot = 0
        i = 0
        for file in file_handle.handle_files():

            for line in file:
                if startup.debug:
                    print(line)
                line = assembler.pseudo_commands(line)
                cmd = line.split(" ")[0]
                try:
                    type = ControlUnit.code_to_type[cmd]
                    assembled_line = 0
                    match type:
                        case "R":
                            assembled_line = isa.Rtype_assemble(line)
                        case "I":
                            assembled_line = isa.Itype_assemble(line)
                        case "S":
                            assembled_line = isa.Stype_assemble(line)
                        case "U":
                            assembled_line = isa.Utype_assemble(line)

                    Ram.write_ram(starting_spot + i,assembled_line)
                    i+=1
                except:
                    print(f"invalid command: {cmd}")
                    print(f"code may break!")
            ranges.append(range(starting_spot,starting_spot+i))
            starting_spot= i
            i=0
        return ranges

    @staticmethod
    def pseudo_commands(line): #some commands like mov doesn't have a format so they get replaced.
        cmd,args = line.split(" ", 1)
        if cmd == "mov":
            return line + ", 0"
        return line

