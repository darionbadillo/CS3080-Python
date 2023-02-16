"""
Homework 2 - Exercise 3
Name: Darion Badillo
Date: 02/14/2023
Description of your program: This program was created to practice using lists. The program creates, sorts, appends,
removes, inserts, and reverse items in a list. The function strList iterates through the function and turns the items
in the list into a formatted string.
"""


# Takes current list and turns values into a formatted string
def strList(str_list):

    fancy_str = ''

    # Iterates through str_list, adds items to a string separated by a comma
    for item in range(0, len(str_list)):

        if item == len(str_list) - 1:
            fancy_str += 'and ' + str_list[item]
        else:
            fancy_str += str_list[item] + ', '

    return fancy_str


# main

# Create a list with strings 'Wallet', 'Phone', and 'Keys'. Print the list using a single line of
# code
string_list = ['Wallet', 'Phone', 'Keys']
print(*string_list)

# Sort the list using the sort() function, then print the list again
string_list.sort()
print(*string_list)

# Print the first item in the list
print(*string_list[:1])

# Print everything except the first item in the list as a list using slicing
print(*string_list[1:3])

# Print the last item in the list using negative index
print(*string_list[-1:])

# Print the index of keys using index
index = string_list.index('Keys')
print(f'Keys index: {index}')

# Append tablet to the list, then print the list
string_list.append('Tablet')
print(*string_list)

# Insert mask to the list as the second item and print
string_list.insert(1,'Mask')
print(*string_list)

# Remove phone from the list and print
string_list.remove('Phone')
print(*string_list)

# Reverse the list and print
string_list.reverse()
print(*string_list)

# Print formatted string of list
print(strList(string_list))
