# # Dictionary 
myDict = {
    "fast" : "In a Quick Manner",
    "ahmad" : "A Software Engineer",
    "marks" : [1,2,3],
    "anotherdict": {'ahmad': 'racer'},
    1: 2
}

# # print(myDict['Fast'])
# # print(myDict['Ahmad'])
# # print(myDict['Marks'])
# print(myDict['anotherdict']['ahmad'])

# dictionary unoder hoty hai or changable b 

# dictionary method

# print(myDict.keys())
# print(list(myDict.keys()))
# print(myDict.value())

updateDict = { #this function use for update dictionary
    "Lovish": "Friend",
    "ahmad" : "A Python Developer"
}
myDict.update(updateDict)
print(myDict)

# sets in python 
# Set is non repititive element 
s = {1,2,3,4,1}
print(s) 

# how to creat an empty set 
a = {}
print(type(a)) #This is not an empty set this a dictionary

# Here is the way we can make an empty set 

b = set()
print(type(b)) #this is the valid empty set 
b.add(4)
b.add(5)       # how to add value in a empty set 
b.remove(5)  #we can use for remove value
# b.add([1,2,3,4]) #Not a valid santex we cannot add list in set 
b.add((1,2,3,4)) #yes we can add a tuple in the set
# we cannot add dictionary in the set 

print(b)


