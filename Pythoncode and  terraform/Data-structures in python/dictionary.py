# Dictionary is a key value pair

my_dict = {"name": "Vishal","Age": 26,"Experience": 3}

# Iterating over keys
for key in my_dict.keys():   # we can use without .keys() also to iterate ex: (for key in my_dict:)
    print(key, end=" ")
print()
# Iterating over values
for value in my_dict.values():
    print(value, end=" ")
print()
# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f'{key}: {value}', end=" ")
print()
# output is 
#  name Age Experience 
#  Vishal 26 3
#  name: Vishal Age: 26 Experience: 3

######################################################################################################

my_dict = {"name": "Vishal","Age": 26,"Experience": 3}
print(my_dict.get('Experience'))
print(my_dict["Experience"])

# output is 3

######################################################################################################

my_dict = {"name": "Vishal","Age": 26,"Experience": 3}
my_new_dict = {"name": "Shivaji","Age": 56 ,"Experience": 30}
my_dict.update(my_new_dict)
print(my_dict)

# output will be  {'name': 'Shivaji', 'Age': 56, 'Experience': 30}

########################################################################################################

my_dict = {"Name": "Vishal","Age": 26,"Experience": 3}
my_dict.pop("Age")
print(my_dict)

# OUTPUT IS {'name': 'Vishal', 'Experience': 3}

########################################################################################################

my_dict = {"Name": "Vishal","Age": 26,"Experience": 3}
MY_NEW_DICT = my_dict.copy()
print(MY_NEW_DICT)

# OUTPUT IS {'Name': 'Vishal', 'Age': 26, 'Experience': 3}

##############################################################################################################

my_dict = [{"Name": "Vishal","Age": 26,"Experience": 3},
           {"Name": "Shivaji","Age": 55,"Experience": 30},
           {"Name": "Thorat","Age": 40,"Experience": 24}]

for name in my_dict:
    print(name["Name"] , end=" ")
print()

# output  Vishal Shivaji Thorat
for i,item in enumerate(my_dict):
    print(i,item)
#output is 
# 0 {'Name': 'Vishal', 'Age': 26, 'Experience': 3}
# 1 {'Name': 'Shivaji', 'Age': 55, 'Experience': 30}
# 2 {'Name': 'Thorat', 'Age': 40, 'Experience': 24}

print()
for name in my_dict:
    for eachelement in name.values():
        print(eachelement , end =" ")
    print()

# Vishal 26 3
# Shivaji 55 30
# Thorat 40 24

for name in my_dict:
    for key , value in name.items():
        print(f"{key}:{value}" , end =" ")
    print()

# Name:Vishal Age:26 Experience:3
# Name:Shivaji Age:55 Experience:30
# Name:Thorat Age:40 Experience:24

##########################################################################################################