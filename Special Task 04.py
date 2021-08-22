# Question no .04
# function maxMeetings
def MaxMeeting(s, f):
    n = len(f)
    i = 0
    for j in range(n):
 
        if s[j] >= f[i]:
            print(j)
            i = j
            
s = [75250, 50074, 43659, 8931,11273,27545, 50879, 77924]
f = [112960, 114515, 81825, 93424,54316,35533, 73383, 160252]
print("The following is Max Meeting ")
MaxMeeting(s, f)