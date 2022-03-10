print("This line will be printed.")

x = 1
if x == 1:
    # indented four spaces
    print("X is",x,".")

#int
myint = 7
print(myint)

#float
myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

#string
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

#Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print(three)

hello,world = "hello", "world"
helloworld = hello + " " + world
print(helloworld)

if mystring == "hello":
    print("String: %s" % mystring)

if isinstance(myfloat, float) and myfloat == 7.0:
    print("Float: %f" % myfloat)

if isinstance(myint, int) and myint == 7:
    print("Integer %d" % myint)
