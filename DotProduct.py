def dotproduct(list1, list2):
  sum = 0
  for(i,j) in zip(list1, list2):
    sum = sum + (i*j)
  return sum

l1 = []
l2 = []
 

list1 = (input("Enter the list1"))
for i in list1.split():
    num = int(i)
    l1.append(num) 
list2 = (input("Enter the list2"))
for i in list2.split():
    num = int(i)
    l2.append(num)

if len(l1) == len(l2):
	result = dotproduct(l1, l2)
	print(result, end="")

else:
  print("Length of lists are different")

  
