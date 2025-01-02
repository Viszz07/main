
'''
lines=["Hi", "there", "How are you?", "The weather is nice"]

Expected Output:
1 Hi
2 there
3 How are you?
4 The weather is nice
'''
lines=["Hi", "there", "How are you?", "The weather is nice"]
i= 1
for item in lines:
    print(i,item)
    i+=1

print()


'''
names=["John Doe", "Jane Doe", "Alex Smith", "Ryan Doe", "Mike Hanks", "Jay Smith"]

Expected output:
Doe 3
Hanks 1
Smith 2
'''
names=["John Doe", "Jane Doe", "Alex Smith", "Ryan Doe", "Mike Hanks", "Jay Smith"]
new_dict={}
for item in names:
    sur_name = item.split(" ")[-1]
    if sur_name in new_dict:
        new_dict[sur_name] += 1
    else:
        new_dict[sur_name] = 1
for key, value in new_dict.items():
    print(f"{key} {value}")



