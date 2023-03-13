'''Write a Python function that takes a string s as input and returns the length of the largest streak of 0s in the string. 
   For example, if the input string is "10001000110000000001", the function should return 6.'''

curr_len = 0
max_len = 0 
count = 0 
m = 0

s = (input())
for i in s:
    print(i,end=" ")
    if int(i)==0:
  
        count = count+1 
        curr_len = count
        
        if(curr_len>max_len): 
            max_len = curr_len 
    else: 
        count = 0
print(max_len)
    	
    
