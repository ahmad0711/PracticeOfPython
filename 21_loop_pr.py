# #print a table using for loop
# n = int(input("Enter the Number:"))
# for i in range(1, 11):
#     ##Below Code of Line is Write without F string
#     # print(str(n) + " X " + str(i) + "=" + str(n*i))
#     ##But if we are use F sring. Its make coder life easy 
#     print(f"{n}X{i}={n*i}")

# #practice no.02

# f1 = ["Ahmad", "Zahid", "Zawar", "Ali"]

# for name in f1:
#     if name.startswith("A"):
#         print("Chaudhry " + name)
    
# #practice no.03 this problem is no.1 but solved with while loop

# n = int(input("Enter the Number:"))
# i = 0
# while i<11: 
#     print(f"{n}X{i}={n*i}")
#     i = i + 1

# #practice no.04

# n = int(input("Enter a Number: "))
# prime = True

# for i in range(2, n):
#     if(n%1 == 0):
#         prime = False
#         break
# if prime:
#     print("This Number is Prime")
# else:
#     print("This Number is not Prime")

# #practice no.06

# n = int(input("Enter a number:\n"))
# factorial = 1 
# for i in range(1, n+1):
#     factorial = factorial*i
# print(f"the factorial of {n} is {factorial}")

# #practice no.08

## but this is wronge way to sol this problem
## print("     *       ")
## print("    ***      ")
## print("   *****     ")

# n = 4

# for i in range(4):
#     print("*" * (i+1))

# #practice no.07


a = [105, 106, 107]

print(type(a))