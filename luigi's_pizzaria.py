"""
Name: Shivam Patel
Problem: The purpose of this program is to ask the customer for their pizza order and provide them with a receipt
based on their choices.
Date: 09/2/2024
"""


"""
Note all while loops used in the program are made with a validation of some sort so the user has to insert a specific
input otherwise will be re-prompted the question
"""

# Function created to run the program
def pizza_order():

    print("Welcome to Luigi's Pizzaria")
    while True:
        try: # Try and except block used to check user input and make sure it is valid
            a = int(input("How many pizzas would you like? ")) # used to multiply bill at end for final_bill
            break
        except ValueError:
            print("That was not a valid integer please try again!")

    while True: # While loop used to ask for size of pizza
            b = input("What size pizza(s) would you like (Small, Medium, Large)? ").upper()
            if b != 'SMALL' and b != 'MEDIUM' and b != 'LARGE':
                print("Your input is invalid. Please try again!")
            else:
                break # breaks loop



    bill = 0 # Variable starts at 0 to have more added to it
    # Boolean used to
    if b == 'SMALL':
        bill += 12 # Adds $12 to bill
    elif b == 'MEDIUM':
        bill += 15 # Adds $15 to bill
    else:
        bill += 18 # Adds $18 to bill

    # While loop that prompts user to a topping choice
    while True:
        c = int(input("Would you like pepperoni (1 for yes, 0 for no)? "))
        if c != 1 and c != 0:
            print("Your input is invalid. Please try again!")
        else:
            break #breaks the loop

    if c == 1:
        bill += 1 # Adds $1 to bill
    else:
        bill += 0 # Nothing added to bill

    # While loop that prompts user to a topping choice
    while True:
        d = int(input("Would you like sausage (1 for yes, 0 for no)? "))
        if d != 1 and d != 0:
            print("Your input is invalid. Please try again!")
        else:
            break # breaks the loop for next prompt

    if d == 1:
        bill += 1 # Adds $1 to bill
    else:
        bill += 0 # Nothing added to bill

    # While loop that prompts user to a topping choice
    while True:
        e = int(input("Would you like olives (1 for yes, 0 for no)? "))
        if e != 1 and e != 0:
            print("Your input is invalid. Please try again!")
        else:
            break # breaks the loop

    if e == 1:
        bill += 1 # Adds $1 to bill
    else:
        bill += 0 # Nothing added to bill


    # Boolean used to check for toppings or no toppings to add to receipt
    if bill == 12 or bill == 15 or bill == 18:
        extra = "with no toppings"
    else:
        extra = "with toppings"


    final_bill = bill * a # Used to calculate the final bill

    # Receipt for the order
    receipt = (f"Thank you for your order! \n"
               f"Quantity: {a} Item(s): {b} cheese pizza(s) {extra} - ${final_bill}.00")
    # Printed receipt with final bill added to it
    print(receipt)


# Function is being called here
if __name__ == "__main__":
    pizza_order() # Used function