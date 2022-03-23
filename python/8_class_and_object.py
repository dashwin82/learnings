class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()

print(myobjectx.variable)
myobjectx.function()


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle("Fer", "red", 60000.00)
car2 = Vehicle("Jump", "blue", 10000.00)

# test code
print(car1.description())
print(car2.description())


# Python program to
# demonstrate private methods

# Creating a Base class
class Base:

	# Declaring public method
	def fun(self):
		print("Public method")

	# Declaring private method
	def __fun(self):
		print("Private method")

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)

	def call_public(self):

		# Calling public method of base class
		print("\nInside derived class")
		self.fun()

	def call_private(self):

		# Calling private method of base class
		self.__fun()

# Driver code
obj1 = Base()

# Calling public method
obj1.fun()

obj2 = Derived()
obj2.call_public()

# Uncommenting obj1.__fun() will
# raise an AttributeError

# Uncommenting obj2.call_private()
# will also raise an AttributeError

