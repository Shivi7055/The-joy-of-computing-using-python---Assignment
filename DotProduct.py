'''Write a Python program that calculates the dot product of two lists containing the same number of elements. 
The program should take two lists of integers as input from the user, and then call a function named dot_product to find the dot product of the two lists. 
The dot_product function should take two lists a and b as input, and should return the dot product of those two lists.

Your program should first prompt the user to enter the two lists of integers, which should be entered as strings separated by spaces.
 Your program should then convert the input strings into lists of integers. Your program should then call the dot_product function with the two lists as arguments, and store the resulting dot product in a variable named result. 
 Finally, your program should print out the dot product of the two lists as the output.'''


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

  
