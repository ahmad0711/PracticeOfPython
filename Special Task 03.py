# Question no.03
# The longest substring
def lcs(X, n):
 
    if n == 0:
    	return 0;
    elif X[n-1]:
    	return 1 + lcs(X, n-1);
    else:
    	return max(lcs(X, n-1), lcs(X, n-1));
 
X = "geeksforgeeks"
print ("Length of LCS is ", lcs(X ,len(X),))

