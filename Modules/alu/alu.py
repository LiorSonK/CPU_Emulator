class alu:

    @staticmethod
    def binary_add(b1: int, b2: int)->int:
        num = 0
        i = 0
        carry = 0

        while b1>0 or b2>0 or carry>0: #runs while both nums are bigger than 0 and there's no carry

            if b1 % 2 == b2 % 2:
                if b1 % 2 == 0: #if both are 0
                    if carry == 1:
                        num += 2 ** i
                        carry = 0
                else: #if both are 1
                    if carry == 1:
                        num += 2 ** i
                        carry = 1
                    else:
                        carry = 1
            else: #if one of the numbers is 1 and the other is o
                if carry == 1:
                    carry = 1
                else:
                    num += 2 ** i
                    carry = 0

            i += 1
            b1 = b1 // 2
            b2 = b2 // 2
        return num

    @staticmethod
    def binary_sub(b1: int, b2: int)->int: #currently using python TODO: change the algorithm
        return  b1-b2

    @staticmethod
    def binary_xor(b1: int, b2: int)->int:
        num =0
        i=0

        while b1 > 0 or b2 > 0:
            if b1 % 2 != b2 % 2:
                num += 2 ** i

            i+=1
            b1 = b1 // 2
            b2 = b2 // 2

        return num

    @staticmethod
    def binary_or(b1: int, b2: int)->int:
        num = 0
        i = 0

        while b1 > 0 or b2 > 0:
            if b1 % 2 == 1 or b2 % 2 == 1:
                num += 2 ** i

            i += 1
            b1 = b1 // 2
            b2 = b2 // 2

        return num

    @staticmethod
    def binary_and(b1: int, b2: int)->int:
        num = 0
        i = 0

        while b1 > 0 or b2 > 0:
            if b1 % 2 == 1 and b2 % 2 == 1:
                num += 2 ** i

            i += 1
            b1 = b1 // 2
            b2 = b2 // 2

        return num

    @staticmethod
    def binary_not(b1: int)->int:
        num = 0
        i = 0

        while b1 > 0:
            if b1 % 2 == 0:
                num += 2 ** i

            i += 1
            b1 = b1 // 2

        return num
b1 = 54
b2 = 765
print("------------")
print("python xor : ", b1^b2)
print("my xor: ", alu.binary_xor(b1,b2))
print("------------")
print("python and : ", b1&b2)
print("my and: ", alu.binary_and(b1,b2))
print("------------")
print("python or : ", b1|b2)
print("my or: ", alu.binary_or(b1,b2))
print("------------")
print("python not : ", ~b1)
print("my not: ", alu.binary_not(b1))
print("my not is fine cuz python is weird\nor is it me...")
print("------------")
print("python add : ", b1+b2)
print("my and: ", alu.binary_add(b1,b2))
print("------------")