phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

for name,number in phonebook.items():
    print("Phone Number of %s is %d" % (name,number))

del phonebook["John"] 
phonebook.pop("Jill")

print(phonebook)


phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
# your code goes here
phonebook["Jake"] = 938273443
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
