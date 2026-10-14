class ControlUnit:
    def __init__(self):
        instructions = {"ret":0,
                        "mov":1,
                        "add":2,
                        "sub":3,
                        "jmp":4,
                        "load":5,
                        "store":6,
                        "push":7,
                        "pop":8,
                        "addi":12,
                        "subi":13
                        }
