# Two types of Loops in python 
# while loop and for loop 
# Use of while Loop 
# a = 0
# while a<10:
#     print("Ahmad")
#     a = a + 1
##Quick Quiz  print 1 to 50 counting
# a = 0
# while a<=50:
#     print(a)
#     a = a + 1
##quick Quiz 2 
# fruits = ["Mango", "Apple", "Banana", "Guava"]
# f = 0
# while f<len(fruits):
#     print(fruits[f])
#     f = f+1

##For Loop

# fruits = ["Mango", "Apple", "Banana", "Guava"]
# for item in fruits:
#     print(item)

##Range Function in For loop

# for i in range(1,9):
#     print(i)

##Range function with step size

# for i in range(1,9,2): #step size is use for skip value
#     print(i)            #not mostally used function 

## conditional operator use in loop

# for i in range (8):
#     print(i)
# else:
#     print("This is end")

##Break function in loop
for i in range (8):
    print(i)
    if i == 5:
        break
