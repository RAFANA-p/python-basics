#Return "orange" instead of "banana" ?



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

list = [0,1,2,3,4]
newlist1 = [x**2 for x in list]
print(newlist1)