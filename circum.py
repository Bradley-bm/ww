def circumference(radius):
    pi = 3.142
    return 2 * pi * radius
radius = float(input("Enter the radius of the circle: "))
result = circumference(radius)
print("The circumference of the circle is:", round(result, 2))
