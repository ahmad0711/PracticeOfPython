# # Practice set
# I = input("Please Enter Name: ")
# N = ["ahmad", "zawar", "zahid", "zeshan", "ali"]
# if(I in N):
#     print("Yes name available here")
# else:
#     print("No Name is Not Available")

# marks = int(input("Please Enter your total marks:\n"))

# if(marks>100):
#     print("Sorry you are enter invalid Number")
# elif(marks>=90):
#     print("Awesome your grade is A")
# elif(marks>80):
#     print("Exelent your grade is B")
# elif(marks>70):
#     print("Nice your grade is C")
# elif(marks>60):
#     print("Your grade is D")
# else:
#     print("Sorry your grade is poor")

##second way to sol upper problem
marks = int(input("Please Enter your total marks:\n"))

if(marks>100):
    grade = "Invalid"
elif(marks>=90):
    grade = "A"
elif(marks>80):
    grade = "B"
elif(marks>70):
    grade = "C"
elif(marks>60):
    grade = "D"
else:
    grade = "F"

print("Your garde is " + grade)
