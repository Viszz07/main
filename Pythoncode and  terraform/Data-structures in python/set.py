# Its Unordered, mutable, only unique elements, no indexing.

my_set = {1,2,3,4,5,6,7,7,8,9,0,9}
print(my_set)

#output is {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

###################################################################################

my_set = {1,2,3,4,5,6,7,7,8,9,0,9}
my_set.add(55)
print(my_set)

# output is {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 55}

###############################################################################

my_set = {1,2,3,4,5,6,7,7,8,9,0,9}
my_set.remove(3)
print(my_set)

# output is {0, 1, 2, 4, 5, 6, 7, 8, 9}

##############################################################################

my_set = {1, 2}
my_list = [3, 4]
my_tuple = (5, 6)

# Adding elements from both the list and tuple to the set
my_set.update(my_list, my_tuple)

print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
#####################################################################################
my_set = {"a", "b"}
my_string = "bcdef"

# Adding characters from the string to the set
my_set.update(my_string)

print(my_set)  # Output: {'a', 'b', 'c', 'd', 'e', 'f'}

#############################################################################

my_set = {1, 2, 3}
my_list = [3, 4, 5]

# Adding elements from the list to the set
my_set.update(my_list)

print(my_set)  # Output: {1, 2, 3, 4, 5}

###############################################################################

my_set = {1,2,3,4,5,6,7,7,8,9,0,9}
length = len(my_set)
print(length)

# output is 10

###############################################################################

my_set = {1,2,3,4,5,6,7,7,8,9,0,9}
my_set.discard(5)  # same as remove
print(my_set)

# output is {0, 1, 2, 3, 4, 6, 7, 8, 9}

#######################################################################################

my_set = {1,2,3,4,5,6,7,8}
my_newset = {1,2,3,4,5,6,7,8,9,5,6,56}
value = my_set.issubset(my_newset)
print(value)


# output is True

############################################################################################
# Union: Combines elements from multiple sets.  (union)
# Intersection: Finds common elements between sets. (intersection)
# Difference: Finds elements in one set that are not in another. (difference)
# Symmetric Difference: Finds elements that are in either set but not in both. (symmetric_difference)
# Subset/Superset: Checks for subset or superset relationships. (issubset , issuperset)
# Disjoint: Checks if two sets have no elements in common. (isdisjoint)
# Add/Remove/Discard: Modify the set by adding or removing elements. (add , remove , discard )
# Pop/Clear: Remove elements or clear the set. (pop , clear )