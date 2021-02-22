print(".................!!!!!!Welcome to my Beginner Calculator!!!!!!................\n\n")
num1=int(input("Enter a number: "))
num2=int(input("Enter a second number: "))
#addition
print("......Choose the calculation you need to perform.......\n")
operators =int(input("\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Modulus\n  "))
if operators == 1:
    print("......Addition calculation......\n")
    sum = num1 + num2
    print(f"Your sum = {sum}")
elif operators == 2:
    print("......Subtraction calculation......\n")
    Subtraction = num1 - num2
    print(f"Your difference is = {Subtraction}")
elif operators == 3:
    print("......Multiplication calculation......\n")
    multply = num1 * num2
    print(f"Your Multiplication is = {multply}")
elif operators == 4:
    print("......Division calculation......\n")
    divide = num1/num2
    print(f"Your division is = {divide}")
elif operators == 5:
    print("......Modulus calculation......\n")
    mod = num1 % num2
    print(f"Your modulus is = {mod}")
else:
    print("Kindly select a valid option")

