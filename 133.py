#Join a Set and a Tuple

#The union() method allows you to join a set with other data types,
# like lists or tuples.


x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)