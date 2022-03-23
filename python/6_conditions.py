x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#Python uses indentation to define code blocks, instead of brackets. 

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

x = [1,2,3]
y = [1,2,3]
z = x;
print(x == y) # Prints out True
print(x is y) # Prints out False
print(x is z)

print(not False) # Prints out True
print((not False) == (False)) # Prints out False

# change this code, first section, so that each if statement resolves as True.
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
