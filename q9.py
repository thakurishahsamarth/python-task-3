num = input("Enter an integer: ") 
reversed_num = ""

for digit in num[::-1]:
    reversed_num += digit

print("Reversed number:", reversed_num)