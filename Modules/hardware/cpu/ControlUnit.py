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
                    "beq":20, #branch equal
                    "bne":21, #branch not equal
                    "blt":22, #branch less than
                    "bge": 23, #branch greater equal
                    "bgt": 24, #branch greater then
                    "ble": 25, #branch less equal

                    }
    int_to_code = dict([(v,k) for k,v in code_to_int.items()]) #flips keys and values

    code_to_type = {
         "mov": "I", #mov is I for now but its S
         "add": "R",
         "sub": "R",
         "jmp": "U",
         "load": "U",
         "store": "U",
         "push": "U",
         "pop": "U",
         "addi": "I",
         "subi": "I",
         "beq": "R",
         "bne": "R",
         "blt": "R",
         "bge": "R",
         "bgt": "R",
         "ble": "R",
        # "ret": "?",
         }
