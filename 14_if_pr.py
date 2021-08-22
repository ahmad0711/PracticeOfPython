n1 = int(input("Plase Enter The Score Team 1: "))
n2 = int(input("Plase Enter The Score Team 2: "))
n3 = int(input("Plase Enter The Score Team 3: "))
n4 = int(input("Plase Enter The Score Team 4: "))
if(n1>n4):
    f1 = n1
else:
    f1 = n4

if(n2>n4):
    f2 = n2
else:
    f2 = n3

if(f1>f2):
    print(str(f1) + " is Greater ")
else:
    print(str(f2) + " is Greater ")
    

