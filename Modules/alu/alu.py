class alu:

    @staticmethod
    def binary_add(b1: int, b2: int)->int:
        pass

    @staticmethod
    def binary_sub(b1: int, b2: int)->int:
        pass

    @staticmethod
    def binary_xor(b1: int, b2: int)->int:
        num =0
        i=0

        while b1>0 or b2>0:
            if b1%2 != b2%2:
                num += 2**i

            i+=1
            b1 = b1 //2
            b2 = b2 //2

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
                num += 2**i

            i += 1
            b1 = b1 // 2

        return num
b1 = 54
b2 = 765
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
print("------------")