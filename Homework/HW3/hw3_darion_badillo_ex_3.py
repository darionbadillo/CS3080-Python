"""
Homework 3 - Exercise 3
Name: Darion Badillo
Date: 02/23/2023
Description of your program: This program uses Python Dictionaries to Update, Delete, and Print an existing
inventory
"""


# Takes inventory dictionary and prints a neatly formatted inventory
def print_inventory(current_inventory):
    print("Current Inventory: ")
    print("____________________________________")
    for k, v in current_inventory.items():
        print(f'{k:20s} {v}')


# Adds an item to inventory
def add_item(current_inventory, item):

    # Searches inventory to check if item already exists
    if item.lower() in str(inventory.keys()).lower():
        # Takes current value and increment it by 1
        count = current_inventory.get(item, 0)
        current_inventory[item] = int(count) + 1

    # If item doesn't exist, this adds the singular item to the inventory
    else:
        current_inventory[item] = 1

    # Returns new dictionary
    return current_inventory


# Deletes an item from the inventory
def delete_item(current_inventory, item):

    # Searches inventory to check if item exists
    if item in current_inventory.keys():
        count = current_inventory.get(item, 0)
        # Decrements the value of the item being deleted by 1
        if int(count) != 0:
            current_inventory[item] = int(count) - 1
        # If item is already at 0, the item cannot be decremented any further
        else:
            print(f"Error: {item} cannot be deleted any further")

    # Error statement saying item does not exist
    else:
        print(f"{item} does not exist and cannot be deleted")
    return current_inventory


# main

# inventory dictionary
inventory = {"Item": "Number of Item", "Hand Sanitizer": "10", "Soap": "6", "Kleenex": "22",
             "Lotion": "16", "Razors": "12"}

# Prints formatted inventory
print_inventory(inventory)
sentinel_value = False

# Loops until a sentinel value of -1 is given and will exit loop
while not sentinel_value:

    # Asks user for to make a choice of adding an item, deleting an item, or printing current inventory
    user_choice = int(input("\nPlease select an option:\n1 to add an item\n2 to delete an item\n3 to print inventory"
                            "\n-1 to quit\n"))

    # Displays error message if the user's input does not match any existing choice
    if user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != -1:
        print("\nInvalid choice")

    # Allows user to add an item to the existing inventory if user entered 1 and reprints inventory
    elif user_choice == 1:
        item_to_add = input("\nIf item being added exists in inventory, please ensure item matches case.\n"
                            "Please enter an item to add: ")
        inventory = add_item(inventory, item_to_add)
        print_inventory(inventory)

    # Allows user to delete an item from the existing inventory if user entered 2 and reprints inventory
    elif user_choice == 2:
        del_item = input("\nPlease enter an item to delete: ")
        inventory = delete_item(inventory, del_item)
        print_inventory(inventory)

    # Allows user to reprint inventory
    elif user_choice == 3:
        print("\nPrinting current inventory")
        print_inventory(inventory)

    # Sets bool value to true to exit loop
    elif user_choice == -1:
        sentinel_value = True

print("\nHave a good day!")
