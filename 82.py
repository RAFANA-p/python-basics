#Customize Sort Function
#You can also customize your own function by
# using the keyword argument key = function.

#The function will return
# a number that will be used to sort the list (the lowest number first)

#Sort the list based on how close the number is to 50?

def myfunc(n):
  print(n,"value from list", "after subtraction n - 50",abs(n-50))

  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


