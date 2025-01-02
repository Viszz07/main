# Immutable 

my_tuple = (1,2,3,4,5,4,6,7)
count = my_tuple.count(4)
print(count)

# output 2

###############################################################################

my_tuple = (1,2,3,4,5,4,6,7)
print(my_tuple.index(4))

# output will return the index of the value

#######################################################################################

my_tuple = (1,2,3,4,5,6,7,8)
print(my_tuple.__contains__(5))

# output will be true ( return a boolean)

##########################################################################################

my_tuple = (1,2,3,4,5,6,7,8)
length = len(my_tuple)
print(length)

# output will be length as 8 

##########################################################################################

my_tuple = (1,2,3,4,5,6,7,8)
my_tuple[4]=6
print( my_tuple)

# output is that tuple cannot be assigned a value as its immutable after its first assignment
