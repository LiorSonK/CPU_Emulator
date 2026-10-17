from Modules.file_handler.file_handle import file_handle
from Modules.hardware.cpu.ControlUnit import ControlUnit
from isa import isa
from Modules.hardware.ram import Ram

class addembler:

    @staticmethod
    def assemble_into_ram():
        ranges = []
        starting_spot = 0
        i = 0
        for file in file_handle.handle_files():

            for line in file:
                line = addembler.pseudo_commands(line)
                cmd = line.split(" ")[0]
                try:
                    print(line)
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
            rd = args.split(",")[0]
            try:
                num = int(args.split(",")[1].strip())
                return f"addi {rd}, r0, {num}"
            except ValueError:
                r1 = args.split(",")[1].strip()
                return f"add {rd}, {r1}, r0"
        return line


print(addembler.assemble_into_ram())
print(Ram.ram[0:100])