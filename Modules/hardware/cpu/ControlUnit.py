class ControlUnit:
    code_to_int = {#"ret":0, i dont have labels yet
                    "mov":1,
                    "add":2,
                    "sub":3,
                    "jmp":4,
                    "load":5,
                    "store":6,
                    "push":7,
                    "pop":8,
                    "addi":12,
                    "subi":13,
                    "BEQ":20, #branch equal
                    "BNE":21, #branch not equal
                    "BLT":22, #branch less ten
                    "BGE": 23, #branch greater equal
                    "BGT": 24, #branch greater then
                    "BLE": 25, #branch less equal

                    }
    int_to_code = dict([(v,k) for k,v in code_to_int.items()]) #flips keys and values

    code_to_type = {
         #"ret": "?",
         "mov": "R",
         "add": "R",
         "sub": "R",
         "jmp": "U",
         "load": "u",
         "store": "U",
         "push": "U",
         "pop": "U",
         "addi": "I",
         "subi": "I",
         "BEQ": "I",
         "BNE": "I",
         "BLT": "I",
         "BGE": "I",
         "BGT": "I",
         "BLE": "I",
         }
