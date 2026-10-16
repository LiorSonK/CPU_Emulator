from isa import isa
str = "add r1, r2, r3"
str2 = "addi r1, r2, 6"
str3 = "store r1, 5498"
x = isa.Rtype_assemble(str)
y = isa.Itype_assemble(str2)
z = isa.Utype_assemble(str3)
print(x)
print(isa.Rtype_disassemble(x))
print("-----")
print(y)
print(isa.Itype_disassemble(y))
print("-----")
print(z)
print(isa.Utype_disassemble(z))