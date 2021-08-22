## spam didector method 01 
# text = input("Enter your Comment\n")

# if("make money fast" in text):
#     print("This is a spam")
# elif("click this link below" in text):
#     print("This is a spam")
# elif("Please subscribe this channel" in text):
#     print("This is a spam")
# else:
#     print("This is Not a spam")

## spam didector method 02
text = input("Enter your Comment\n")

if("make money fast" in text):
    spam = True
elif("click this link below" in text):
    spam = True
elif("Please subscribe this channel" in text):
    spam = True
else:
    spam = False
if(spam):
    print("This Text is a spam")
else:
    print("This Text is not a spam")

