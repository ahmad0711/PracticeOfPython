# Code writing by Muhammad Ahmad 
# Question no.1 problem sloved with help of google and youtube
# Declaring a function name as MaxActivities
def MaxActivities(start, end):
    # usnig length funtion 
    n = len(end)
    # printing a statement for show activities 
    print("Here is the following activities are selected")
    s = 0
    # usnig for loop For solving the problem 
    for e in range(n):
        if start[e] >= end[s]:
            print(e)
            s = e
# Here is the values are given in the question 01 example 02
start = [1,3,2,5]
end = [2,4,3,6]
MaxActivities(start , end)
