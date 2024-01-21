print("------------- Arpit Srivastava ---------------")

#Step a:- creating a string and storing into myString variable      
print("\nStep a :- creating a string and storing into myString variable")
myString = "python is most use programming language in the world"

#Step b:- printing out the string
print("\nStep b :- printing String : ")
print(myString)

#Step c:- Convert the string to a list of words using the string split method.
splitString = myString.split()
print("\nStep c :- after spliting : ")
print(splitString)

#Step d:-Sort the list into reverse alphabetical order using some of the list methods (you might need to use dir(list) or help(list) to find appropriate methods).
splitString.sort(reverse=True)

#Step e:-Print out the sorted, reversed list of words.
print
print(splitString)
