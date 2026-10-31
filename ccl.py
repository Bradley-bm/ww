def add(R, B):
    return R + B
def subtract(R, B):
    return R - B
def multiply(R, B):
    return R * B
def divide(R, B):
    return R / B
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = input("Enter choice(a/b/c/d): ")
num_1 = int(input("Please enter first number: "))
num_2 = int(input("Please enter second number: "))
if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("This is an invalid input!")