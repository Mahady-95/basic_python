#Rectangle
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)

#Circle
import math

radius = float(input("Enter radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Area of the circle:", area)
print("Circumference of the circle:", circumference)

#Triangle
base = float(input("Enter base length of the triangle: "))
height = float(input("Enter height of the triangle: "))
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))

area = 0.5 * base * height
perimeter = base + side1 + side2

print("Area of the triangle:", area)
print("Perimeter of the triangle:", perimeter)

