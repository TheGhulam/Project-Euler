def NumberSpiralDiagonals(n):
    layers = (n+1)//2
    return(LayerSum(layers))

def LayerSum(l):
    s, last = 1, 1
    for i in range(2, l+1):
        s += last*4 + 20*(i-1)
        last += 8*(i-1)
    return s

# print(LayerSum(3))
# print("3", NumberSpiralDiagonals(3))
# print("5", NumberSpiralDiagonals(5))
# print("7", NumberSpiralDiagonals(7))
print("1001", NumberSpiralDiagonals(1001))


