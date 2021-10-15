# Building a better calculator :

# 3 variables

num_1 = int(input("Enter num1 : "))
op = input("Enter OP: ")
num_2 = int(input("Enter num2: "))

if op == "+":
    print(num_1 + num_2)
elif op == "-":
    print(num_1-num_2)
elif op == "/":
    print(num_1/num_2)
elif op == "*":
    print(num_1 * num_2)
else:
    print("Invalid operator")
