def int2bin(x: int):
    arr = []
    i=0
    while(x>0):
        print(x)
        arr.append(x%2)
        x = x//2
        i+=1
    arr = arr[::-1]
    return arr
print(int2bin(13))