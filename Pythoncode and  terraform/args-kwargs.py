# args is a tuple internally(multiple arguments at a time : the * is very imp the rest can be any variable name ex: *abc)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5))

# output is 15

#########################################################################################################
# default arguments

def add(a,b=5,c=0):
    return(a+b+c)

print(add(2,3,4)) # output is 9
print(add(2))    # output is 7 as b and c took default argument values

###########################################################################################################

#kwargs keyword arguments is a dictionary internally . used a s **kwargs or any other name as **abc

def address(**kwargs):
    for key in kwargs.keys():
        print(key , end=" ")

address(street= "123-avenue-street", apartment= "#123", zipcode="564")
# output is street apartment zipcode

print()

def address(**kwargs):
    for value in kwargs.values():
        print(value , end=" ")

address(street= "123-avenue-street", apartment= "#123", zipcode="564")
# output is 123-avenue-street #123 564

print()

def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value} ", end=" ")

address(street= "123-avenue-street", apartment= "#123", zipcode="564")

# output is street:123-avenue-street  apartment:#123  zipcode:564
