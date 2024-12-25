user_input = input("Enter a string: ")
print("Characters at even indices:")
for index in range(len(user_input)):
    if index % 2 == 0: 
        print(user_input[index])