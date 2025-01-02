with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("Hello, world!\nhey there")

# Reading from a file with UTF-8 encoding
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)      # prints
    my_data=[]
    for eachline in content.splitlines():
        my_data.append(eachline)
    print(my_data)  # Output: Hello, world!

# UTF-8 IS INHERENTLY SUPPORTTED BY PYTHON NO LIBRARY REQUIRED