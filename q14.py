user_input = input("Enter a string: ")
print("Characters at odd indices:")
for index in range(len(user_input)):
    if index % 2 == 1:  
        print(user_input[index])