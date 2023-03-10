'''Given a matrix M write a function Transpose which accepts a matrix M and return the transpose of M.
   Transpose of a matrix is a matrix in which each row is changed to a column or vice versa.'''

def Transpose(M):
    # Initializing all elements of transpose matrix with 0 
    transpose = [[0 for i in range(len(M))]for i in range(len(M))]    
   	
    for i in range(len(M)):
        for j in range(len(M)):
            transpose[i][j] =M[j][i] #copying elements from M to transpose matrix
    return transpose

n = int(input())
M = [] 

#Taking a matrix as input from the user 
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)
print(Transpose(M))


# resolved a merge conflict - dummy comment


# added a second dummy comment