import re

# Your code goes here
find_members = []
for member in dir(re):
    print(member)
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
