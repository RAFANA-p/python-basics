#Global Variables

#Create a variable outside of a function, and
# use it inside the function & outside the function.

x = "awesome"

def myfunc():

  print("Python is " + x)


myfunc()
print(x)
