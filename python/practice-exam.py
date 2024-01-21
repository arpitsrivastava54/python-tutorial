# ..................  basic syntax ......................
print("hello world")

# single line command 
'''
  multi line command
'''
# .................. string values .........................

my_string = "hello world generating new string using python"

# string methods  upper () lower() replace () ==> it return new string which we need to save it

uppercase_string = my_string.upper()
print(uppercase_string)

replace_string = my_string.replace("world","india")
print(replace_string)

# formating string while printing

name = "arpit"
age = 20
print("hello my name is : {} and my age is {}".format(name,age))
print(f"my name is {name} and my age is {age}")

# string operators

'''
  concatenate ==> (+) ==> full_name  = first_name + last_name
  repetion  ==> (*) ==> print(full_name*3)
'''

# .................. numeric data type .....................
# int , float

# .................. conversion functions .......................
# int () , float () , str ()

my_str = "20"
print("before checking " , type(my_str))
temp_str = int(my_str)
print("after checking " , type(temp_str))


# ................. if statement ...............................
x = 10 
if (x > 5):
  print("greater hai")

# ..................... relational and logical operators .......................
# relational operator ==> < , > <= , >= , == , !=
# logical operator ==> and, or , not

age = 20
if age>=18 and age <= 30:
  print("your are eligible")


# ..................... bitwise operator .....................
# & , | , ~
a = 5 # 0101
b = 2 # 0010
print(a&b) # 0000

# ....................... while loop .................. 
i = 1
while(i<=2):
  print(i)
  i += 1

# .................... break and continue ..............................
# break ==> break the loop permanently
# continue ==> skips the iteration at that time

j=1
while(j<=3):
  if(j==2):
    break
  print(j)
  j += 1

# continue example 
k = 1
while (k<=3):
  if(k==2):
    k += 1
    continue
  print("continue ==> ",k)
  k += 1

# .............................. for loop ....................  
  for x in range(1,4):
    print("for loop ",x)

# ..................... collections ...........................
# python has many built in data types list , tuples , set , dictionaries
'''
list ==> [2,3,5,"apple",True] ==> ordered, changable , allow duplicate
tuples ==> (2,3,5,"apple",True) ==> ordered, immutable , allow duplicated
sets ==> {"apple","mango",1,3,True} ==> unordered , unchangable , do not allow duplicate
dictionaries ==> {
  "name":"arpit",
  "age":20,
} ==> unordered , changable , do not allow duplicate

'''
# ............... copy collections ........................
import copy
my_list = ["apple","mango",[1,3]]
copy_list = copy.deepcopy(my_list)
copy_list[2][0] = "banana"
print("mylist : ",my_list)
print("copylist : ",copy_list)


# ................ def functions .....................



def find_sum(*args):
  temp_sum = 0
  for x in args:
    temp_sum += x
  print("sum ==> ", temp_sum)
  return temp_sum

def greet_fun(name,func):
  print(name)
  func(2,3,5)

greet_fun("arpit",find_sum)

# .................... map functions ......................
# my_list = [1,2,3,4]
# sqrt_list = map(lambda x:x+1,my_list)
# print(set(sqrt_list))

mylist = [1,2,3,4]
filter_list = filter(lambda x : x==2 ,mylist)
print(set(filter_list))

# .................. store functions in dictionaries ..................

my_dict = {
  "hello":lambda name:print(f"hello {name}"),
}
my_dict["hello"]("harshit")

# ................... clouser ......................

def sum (x):
  def sum_with(y):
    return x+y
  return sum_with

sum_with = sum(5)
print("sum ==> : ",sum_with(55))

# ....................... modules ...................
# sys module 
import sys
print("python version : ",sys.version)
print("python version info : ",sys.version_info)

# math module
import math 
# sqrt(25) , pow(2,3) ==> 8 , pi(), e(),log(10) ,factorial(5)
square_root = math.sqrt(25)
print("square root : ", square_root)
power = math.pow(2,3)
print("power : ",power)
fabi = math.fabs(5)
print(fabi)

module_name = dir (math)
print(module_name)

# ........................ exeception handling ..............................

# TypeError, ValueError, ZeroDivisonError etc.

try :
  # x = 5/0
  y = [1,2]
  print(y[2])
# except ZeroDivisionErrofr:
#   print("not divisible by zero")
except Exception as e :
  print(e)


# raise 
# x = int (input ("Enter number for dividng with 10 :"))
# if x <= 0:
#   raise Exception("not allow")
# print("dividing ==> ",10/x)

# assert 

x = int (input ("Enter number : "))
assert x > 0 , "valuse should be greater than zero"
print(10/x)

# ....................... file handling ...........................

# with open("my.txt","w") as file :
#   file.write("hello world")

try :
  with open ("my.txt","r") as file:
    content = file.read()
    print("file content : ",content)
except IOError as e :
  print(e)

# with open ("my.txt","a") as file :
#   # file.write(" hello world 2")
#   print("cursor position : ",file.tell())


# .................. classes ....................

# class Animal :
#   def __init__ (self,name,nature):
#     self.name = name
#     self.nature = nature
  
#   def voice (self):
#     print("animal voice : ",self.nature)

# dog = Animal("lion","roar")
# print("animal name : ",dog.name)
# dog.voice()

# inheritance 

class Animal :
  def __init__(self,name,nature):
    self.name = name
    self.nature = nature
  def live(self):
    print("live in forest")

class Dog(Animal):
  def __init__ (self,name,nature):
    super().__init__(name,nature)
  
  def habbit (self):
    print ("lives in home ...")


d = Dog("tommy","bark")
print("dog name : ",d.name)
print("dog nature : ",d.nature)
d.live()
d.habbit()









































