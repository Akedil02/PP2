def trapezoid_area(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

height = float(input("Enter the height of the trapezoid: "))
base1 = float(input("Enter the first base of the trapezoid: "))
base2 = float(input("Enter the second base of the trapezoid: "))

area = trapezoid_area(height, base1, base2)
print("The area of the trapezoid is:", area)
