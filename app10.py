# reading files:
# open("employees.txt", "w")  w----> write

# open("employees.txt", "a")  a----> append - append info to end of the file

# open("employees.txt", "r+") r+---> read and write

# open("employees.txt", "r")  r----> read

Employees_file = open("Employees.txt", "r")
print(Employees_file.readlines())

Employees_file.close()