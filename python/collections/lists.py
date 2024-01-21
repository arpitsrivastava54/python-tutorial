#........... list ..............

# list are used to store multiple values in a single variable
# list items are ordered, changeable, and allow duplicate values.
# Into the list we use indexes (positive and negative) both start from 0 and -1

#........... example ..............


mylist = ["apple","grapes","banana",1,2,3,True,False]
print (mylist) # ['apple', 'grapes', 'banana', 1, 2, 3]

#............ acces list ..............

# by using indexes
print ("acces list using index : ",mylist[2] ) # acces list using index :  banana
# by using range
print(mylist[2:5]) # ['banana', 1, 2]

#............ change list items ..............

mylist[1] = "cherry"
print(mylist) # ['apple', 'cherry', 'banana', 1, 2, 3]

# ............ methods list (all methods can update original list) ...............

# append
mylist.append("orange")
print(mylist) # ['apple', 'cherry', 'banana', 1, 2, 3, True, False, 'orange']

# copy
newlist = mylist.copy()
print("new list : ", newlist) # new list :  ['apple', 'cherry', 'banana', 1, 2, 3, True, False, 'orange']

# count
count = mylist.count("orange")
print ("count : ", count) # count :  1

# pop 
mylist.pop() # remove last item from list
print(mylist) # ['apple', 'cherry', 'banana', 1, 2, 3, True, False]

# remove 
mylist.remove("cherry") # remove specific item which we mention
print ("after removing : ",mylist) # after removing :  ['apple', 'banana', 1, 2, 3, True, False]


