class SingleLL:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):         # Optional part if you just want to check the print function of the class
        return str(self.val)
    

########################################################### Assignment ####################

Head = SingleLL(1)
A = SingleLL(5)
B = SingleLL(10)
C = SingleLL(15)

Head.next = A
A.next = B
B.next = C
#################################    Display O(n) ###########################################

print(Head)   #---> When print is called it calls the __str__ method inside the class to display in an understandable way
def displayLL(Head):
    mylist = []
    curr = Head
    while curr:
        mylist.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(mylist)) # ----> Always takes a string of iterable make sure you do it already or expplicitly typecast here

displayLL(Head)
 
############################################### search for a val in LL O(n) ######################

def Searchval(Head, val):
    curr = Head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False

print(Searchval(Head, 15))

############################################## Insert at start O(1) ########################

def InsertAtStart(Head, val):
    newNode = SingleLL(val , next = Head)
    return newNode

Head = InsertAtStart(Head , -5)
displayLL(Head)

############################################## Insert at last O(n) ###########################

def Atend(Head , val):
    newnode = SingleLL(val, next=None)
    curr = Head
    while curr.next:
        curr = curr.next
    curr.next = newnode
    return Head
Head = Atend(Head , 20)
displayLL(Head)

############################################## insert in between O(n) 2nd and 3rd Element  ###########################

def Inbetween(Head, val, position):
    newNode = SingleLL(val)
    curr = Head
    counter = 0
    while curr:
        if counter == position:
            newNode.next = curr.next
            curr.next = newNode   
        counter += 1
        curr = curr.next
    return Head 

Head = Inbetween(Head , 12 , 2)
displayLL(Head)

 ################################################# Deleting a Node  O(n) #########################

def deletenode(Head , value):
    prev = Head
    curr = Head.next
    if value == Head.val:    # edge case to delete first node
        Head = Head.next
        return
    while prev:
        if prev.val == value or curr.val == value:
            prev.next = curr.next
        curr = curr.next
        prev = prev.next
    return
deletenode(Head , 1)
displayLL(Head)

#############################################################################################################

