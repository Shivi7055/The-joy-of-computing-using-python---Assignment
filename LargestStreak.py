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
    	
    
