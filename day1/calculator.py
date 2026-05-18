num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

# choose operation
print("select operation:")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

# perform calculation
if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 !=0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by Zero is not allowed")

else:
    print("invalid input")
