text = input("Enter find text\n")

if("AHMAD" in text):
    spam = True
elif("Ahmad" in text):
    spam = True
elif("ahmad" or "aHmad" or "ahMad" in text):
    spam = True
else:
    spam = False
if(spam):
    print("Yes you are talking about Ahmad")
else:
    print("No you are not talking about Ahmad")

