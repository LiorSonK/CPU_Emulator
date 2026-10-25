from startup import startup
from Modules.Assembler.assembler import assembler
from Modules.hardware.cpu.pipeline import pipeline
from Modules.hardware.registers import Registers
startup.start_menu()
ranges = assembler.assemble_into_ram()
if startup.debug_mode:
    print(ranges)
cur_range = 0
while True:
    if Registers.get_specialreg_value("pc") in ranges[cur_range]:
        if startup.debug:
            input("press enter to continue...")
        pipeline.clock_cycle()
        print(Registers.registers)
    else:
        Registers.set_fetch(None)
        pipeline.clock_cycle_no_fetch()
        if startup.debug:
            input("press enter to continue...")
        if Registers.get_memory()["opcode"] == None:
            break