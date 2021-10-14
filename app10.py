# Lists functions:

luck_number = [4,8,15,16,23,42]
#          0      1       2       3     4       5
friends = ["Ali","Ali","Ahmed","Walid","Tom","Sarah"]

friends1 = friends.copy()

print(friends1)
lucky_numbers = [4,8,15,16,23,42]

friends = ["Ali",""Ali",Ahmed","Walid","Yosef","Mosa"]

friends.extend(lucky_number) This will append 2 lists together

friends.append("Sarah") append new element to the list

friends.insert(1,"Salah") insert element in index 1

friends.remove("Mosa")

friends.clear() getred of every single elements inside the list

friends.pop() getred the last element of the list

print(friends.index("Walid"))

print(friends.index("Rovan")) not exist

print(friends.count("Ali")) how many times element is exist.

friends.sort() sort the list in ascending order alphapetical order

lucky_numbers.sort()

print(lucky_numbers)

lucky_numbers.reverse() reverse the order

print(lucky_numbers)

friends2=friends.copy()

print(fiends2)