
l1 = ['A', 'B', 'O', 'T', 'F', 'C']
l2 = ['T', 'J', 'Y', 'P', 'O', 'L'] 
count = 0

if len(l1) == len(l2):
    for i in l1:
        for j in l2: 
            if i == j:
               print("Common elements are:",i +" and "+j) 
               count = count+1
    if count>1:
        print("More than one elements are common")
    else:
        print("No elements are common")