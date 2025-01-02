my_list = ["flower","flow","flight"]

min_word = min(my_list) #to get the minimum word form the list of words 
print(len(min_word)) #apply a len fucntion on the word to get the length
# output is 4 

#####################################################################################################
my_list = [5,3,6,7,2,8,1,9,9,9,4,0,2]
my_newlist = list(set(my_list)) #remove duplicates of the list by converting into a set and back into a list
my_newlist.sort(reverse=True) #either use reverse=True or use directly in ascending order and print(my_list[-2])
print(my_newlist)
print(my_newlist[1])
# gives the second highest element of the array or list (first sort it and then give the second last)
#output is 
# my_list = [5,3,6,7,2,8,1,9,4,0,2]
# 8

###########################################################################################################


def isValid(s: str) -> bool:
    if s == "":
        return True
    if len(s) < 2:
        return False
    r = 0
    s_new = ""
    for i in s:
        if i == "(" or i == "{" or i == "[":
            s_new += i            
        elif i == ")":
            if s_new[-(r+1)] == "(":
                r+=1
            else:
                return False
        elif i == "}":
            if s_new[-(r+1)] == "{":
                r+=1
            else:
                return False
        elif i == "]":
            if s_new[-(r+1)] == "[":
                r+=1
            else:
                return False
    return True   

s = "("
print(isValid(s))