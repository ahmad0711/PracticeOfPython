# # Make a Dictionary 
# myDict = { "fan" : "phanks",
#         "brother" : "bhai"

# }
# print("Please chose a word ", myDict.keys())
# a = input("Enter The English Word\n")
# # If the word enter the user is not available in below then he craet error 
# # gfprint("The Meaning of your word is:", myDict[a])
# # Therefore we are use this peace of code 
# print("Meaning of your desir word is", myDict.get(a))

##write a program to use for make a set of 8 number enter by the use

# n1 = int(input("Please Enter the Number 1: ",))
# n2 = int(input("Please Enter the Number 2: ",))
# n3 = int(input("Please Enter the Number 3: ",))
# n4 = int(input("Please Enter the Number 4: ",))
# n5 = int(input("Please Enter the Number 5: ",))
# n6 = int(input("Please Enter the Number 6: ",))
# n7 = int(input("Please Enter the Number 7: ",))
# n8 = int(input("Please Enter the Number 8: ",))

# s = {n1, n2, n3, n4, n5, n6, n7, n8}
# print(s)

# s = {18, "18"}
# print(s)
favLang = {} 
a = input("Please enter your favorite language ahmad ")
b = input("Please enter your favorite language zawar ")
c = input("Please enter your favorite language zahid ")
d = input("Please enter your favorite language zeeshan ")
favLang['ahmad'] = a
favLang['zawar'] = b
favLang['zahid'] = c
favLang['zeeshan'] = d
print(favLang)
