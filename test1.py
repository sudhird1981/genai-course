print("hello world")
"""list:
ordered set of of numbers
Orderded list - follow indexing
can hold any value
"""
a = [1,2,3,4,5,6]
print(a[0]) #first index
print(a[-2]) #second last

#slicing start
c = a[1:3]
print(c)
c = a[1:]
print(c)
c = a[:3]
print(c)
c = a[:]
print(c)

prompt = ["what is AI","Waht is ML",567,34.5,True]
print(prompt)

#list within list
promt = [1,[3,4,5],6,"sudhir"]
print(type(promt[1]))
print(promt[1][0])

#add value to list
prompt.append(10)
print(prompt)

#remove value
prompt.remove(10)
print(prompt)

#tuple
#can not add delete values to tuple. its imutable. it used very less
#mainly the output of the fucntion return the tuple so that it can not be changed
t = (1,2,3,4)
print(t)

#set
#unit values no duplicate
a_set = {2,3,4,5,4,5}
print(a_set)

#dictionary
#key value pair, value will be fetched based on key
movies = {"title":"3 idiots","year":2006,"rating":4.5,"released":True}
print(movies["title"])
student = {"name":"Saurav","city":"pune"}
#add
student["course"] = "gen ai"
student["pin"] = "411017"
print (student)
#delete
del student["pin"]
print (student)

student.pop("city")
print(student)

messages = [
    {
        "role" : "user",
        "content" : "you are a user"
    },
    {
        "role" : "system",
        "content" : "you are a system"
        
    }
]
print(messages[0]["role"])

#if else
t = 0
if t > 1:
    print("greater")
elif t ==1:
    print("equal")
else:
    print("less")
    
#for loop
numbers = [3,5,7,8,4,2,1,2]
for i in numbers:
    print(i)
    

for i in prompt:
    print(i)
    
movies = {"title":"3 idiots","year":2006,"rating":4.5,"released":True}
messages = [
    {
        "role" : "user",
        "content" : "you are a user"
    },
    {
        "role" : "system",
        "content" : "you are a system"
        
    }
]
for message in messages:
    print(message)
    for i in message:
        print(i + ":" + message[i])
        
costs = {"got-4o":0.005,"got-4o-mini":0.000015}
for model, cost in costs.items():
    print(f"{model} -> {cost}")
    
#fprint
name = "sudhir"
print(f"Hello {name}")

#import - to import any package and library
import math
print(math.sqrt(4))

import json
print("json")

#exception handeling
try:
    number = 3 - 3
    
    print (f"result is : {3/number}")
except:
    print ("devide by 0")
    
#function
def format_message(role,text):
    message = {"role":role,"content":text}
    return message

print(format_message("user","what is AI"))
