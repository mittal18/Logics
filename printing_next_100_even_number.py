#printing next 100 even number
printing_number = 0
user_input = int(input("Enter any integer number: "))
if(user_input%2 != 0):
    starting_number = user_input + 1
else:
    starting_number = user_input + 2
for counter in range(0, 100):
    print(starting_number + printing_number)
    printing_number = printing_number + 2
    counter = counter + 1


