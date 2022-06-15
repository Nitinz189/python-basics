from ast import Delete
from os import lseek


# ls =[ "honey", "ansu" , " nitin"]
        #   0        1           2
        #   -3         *2             -1
# print (ls[0])
# print(ls[-2])

# ls = ["name",["kamal", True], 'jjhj']
# print(ls[2], ls[0])

# to chnage list 
# ls[2]= nitinn
# print(ls)


# to sort list
# ls.sort()

# to append list
# ls.append()
# print(ls)


# to insert in list
# ls.insert(2  , "lion")  here 2 is index no.

# to Delete
# del(ls[2])

# slicing list
# print(ls[2:7]) work on n+1 method
# print(ls[1:]) print 1 to end of list
# print(ls[:5])print list to 4th index


ls = [ 1,112,43,47,50,64,70,812,95,180,11,12]


# for i in range (len(ls)):
#     # print(i)
#     # print(ls[i])

maximum = 0
for i in ls:
   if maximum < i:
     maximum = i
print(maximum)    