# use for store multiple values with different data types
# ordered and unchangeable(not update items or it's values) and allow duplicate values
# into the tuple we use indexes (positive and negative) both start from 0 and -1

mytupple = ("apple","grapes","banana",1,2,3,True,False)
print(mytupple) # ('apple', 'grapes', 'banana', 1, 2, 3, True, False)

#............ acces tupple ..............
print(mytupple[2]) # banana
print(mytupple[-2]) # True
print(mytupple[2:5]) # ('banana', 1, 2) ==> from 2 to 5 not include 5

#............ change tupple items ..............

# we can not change direcetly tupple values because it is immutable so we can try this ==>

templist = list(mytupple)
templist[1] = "cherry"
mytupple = tuple(templist)
print("change tupple items : ",mytupple) # ('apple', 'cherry', 'banana', 1, 2, 3, True, False)

#............ methods tupple ..............

# count
count = mytupple.count("cherry")
print ("count : ", count) # count :  1

# index
position = mytupple.index("banana")
print(position) # 2


