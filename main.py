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
    else:
        print(Registers.latches)
        break