sub1 = int(input("Please Enter Sibject No 1 Marks "))
sub2 = int(input("Please Enter Sibject No 2 Marks "))
sub3 = int(input("Please Enter Sibject No 3 Marks "))

if(sub1<33 or sub2<33 or sub3<33):
    print("Sorry you are fail becasue less the 33% Marks")

if(sub1+sub2+sub3)/3 <40:
    print("Sorry you are fail due to less then 40% Marks")
else:
    print("Congratulation you are PASS ")
