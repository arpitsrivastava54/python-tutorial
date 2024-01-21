
# .................. shallow copy of collections ....................

# it will copy only reference of nested collections

# mainlist = ["apple","grapes",3,True,["childList","childList2"]]
# copylist = mainlist.copy()

# copylist[1] = "cherry"
# copylist[4][0] = "updateChildlist"
# print("main list : ",mainlist) # ['apple', 'grapes', 3, True, ['childList', 'childList2']]
# print("copy list : ",copylist) # ['apple', 'grapes', 3, True, ['childList', 'childList2']]


# ...................... deep copy of collections .................

import copy

mainlist = ["apple","grapes",3,True,["childList","childList2"]]
copylist = copy.deepcopy(mainlist)

copylist[1] = "cherry"
copylist[4][0] = "updateChildlist"
print("main list : ",mainlist) # ['apple', 'cherry', 3, True, ['updateChildlist', 'childList2']]
print("copy list : ",copylist) # ['apple', 'cherry', 3, True, ['updateChildlist', 'childList2']]
