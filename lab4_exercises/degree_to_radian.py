import math
def d_to_r(a):
    r = a * math.pi / 180
    return r
degree = int(input("Input degree:"))
radian = d_to_r(degree)
print(radian)