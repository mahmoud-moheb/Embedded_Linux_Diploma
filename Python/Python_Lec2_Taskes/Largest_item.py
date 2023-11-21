#!/usr/bin/python3
#C style code to find the maximum number in a list
#the list
ls=[1200,1200,29,1300,4,11,20,3]
print("This is your original list {}".format(ls))
#sorting
for i in range(0,len(ls)-1):
    for j in range(0,len(ls)-i-1):
        if ls[j] > ls[(j+1)]:
            temp=ls[(j+1)]
            ls[(j+1)]=ls[j]
            ls[j]=temp
        else:
            pass
print("This is your  list after sorting {}".format(ls))
#printing the maximum number in the list

print("And the maximum number in your list is: {}".format(ls[-1]))