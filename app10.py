# Building a better calculator :

# 3 variables

num1 = int(input("Enter num1 : "))
op = input("Enter OP: ")
num2 = int(input("Enter num2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
