my_list = [1,2,3,4,5]
my_list.insert(4,3)
print(my_list)

# output will be [1, 2, 3, 4, 3, 5]

###################################################################################

my_list = [1,2,3,4,5,6,7]
my_list.remove(3)
print(my_list)
my_list.pop(4) # provide an index default is last index
print(my_list)

# output will be [1, 2, 4, 5, 6, 7]
# output will be [1, 2, 4, 5, 7]
##################################################################################

my_list = [1,2,3,4,5,5,7,8,5,5,6,5]
count= my_list.count(5)
print(count)

# output will be 5

###################################################################################

my_list = [1,2,3,4,5,67,8,89]
my_list.append(55)
print(my_list)

#output is [1, 2, 3, 4, 5, 67, 8, 89, 55]

##################################################################################

my_list=[1,8,5,0,2,567,123,45]
my_list.sort()
print(my_list)

# output is [0, 1, 2, 5, 8, 45, 123, 567]

#################################################################################

my_list=[1,2,3,4,5,6,7]
my_new_list=['Vishal','Shivaji','Thorat']
my_list.extend(my_new_list)
print(my_list)

#if we use append instead of extends

my_list=[1,2,3,4,5,6,7]
my_list.append(my_new_list)
print(my_list)

# output is [1, 2, 3, 4, 5, 6, 7, 'Vishal', 'Shivaji', 'Thorat']
# output is [1, 2, 3, 4, 5, 6, 7, ['Vishal', 'Shivaji', 'Thorat']]
######################################################################################

my_list=[1,2,3,4,5,6,7]
my_new_list = my_list.copy()
print(my_new_list)
my_new_list.append(88)
print(my_new_list)

# output will be [1, 2, 3, 4, 5, 6, 7]
# output will be[1, 2, 3, 4, 5, 6, 7, 88]

#########################################################################################

my_list=[1,2,3,4,5,6,7]
print(my_list.index(5))

# output will be 4

######################################################################################

my_list= [1,2,3,4,5,6,7]
my_list.reverse()
print(my_list)

# output will be [7, 6, 5, 4, 3, 2, 1]
##################################################################################

my_list = [1,2,3,4,5,6,7]
my_list.clear()
print(my_list)

#output will be []
######################################################################################


my_list = [1,2,3,4,5,6,7]
length = len(my_list)
print(length)

# output is 7 

############################################################################################

print(my_list.pop()) 

# by default will pop the last element output is 7

