# dictionaries used to store data in key:value pairs
# it is ordered , changable or mutable , and don't allow duplicate values

# ............... example ............. 
mydict = {
  "name":"john",
  "college":"Aktu"
}
print(mydict) # {'name': 'john', 'college': 'Aktu'}

# ................. access dictionaries  ..............

print(mydict["name"]) # john

# ................. methods dictionaries  ...............

print(mydict.get("college")) # Aktu
print(mydict.items())# dict_items([('name', 'john'), ('college', 'Aktu')])
print(mydict.keys()) # dict_keys(['name', 'college'])
print(mydict.values()) # dict_values(['john', 'Aktu'])

mydict.pop("college") # remove specific item from dictionary
print(mydict) # {'name': 'john'}


mydict.update({"college":"AKTU","age":21}) # update dictionary
print(mydict)

# .................... sort dictionaries ..................

sortedDict = dict(sorted(mydict.items())) # sort dictionary
print("sorted dict ==> ",sortedDict)