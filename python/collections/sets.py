# sets are use to store multiple values in a single variable
# sets are unordered, unchangeable (but we can add or remove items) 
# **** do not allow duplicate values

myset = {"apple",5,True,("banana",3),False}
print(myset) # output of this will be unordered ==> {False, True, 'apple', 5, ('banana', 3)}
print("length of myset : ",len(myset)) # length of myset :  5

# ............ access set items ..............
# we can not access set items using index or range but can access using for loop

for x in myset :
  print(x) # output of this will be unordered ==> False, True, 'apple', 5, ('banana', 3)

# ............ methods set items ..............

# add
myset.add("cherry")
print("after adding item : ",myset) # output of this will be unordered ==> {False, True, 'apple', 5, ('banana', 3), 'cherry'}

# update
myset.update({"john","rock"}) # it will items after destructing this set
print("after updating : ",myset) # {('banana', 3), True, False, 'cherry', 'john', 5, 'rock', 'apple'}

# remove
myset.remove("john") # it will raise error if item is not present
print(myset) # {('banana', 3), True, False, 'cherry', 5, 'rock', 'apple'}

# discard
myset.discard(5) # it will not raise error if item is not present
print(myset) # {('banana', 3), True, False, 'cherry', 'rock', 'apple'}

# pop ==> it will remove last item
# clear ==> it will remove all items from set and set will be empty --> {}

# del ==> it will remove set and it will be deleted 
del myset
print(myset) # NameError: name 'myset' is not defined