"""
Author: EKENEDO NZUBE EMMANUEL  

PURPOSE: The purpose of this project is to help a customer with her shopping. 
        The customer can decide either Add, Remove, Check cart, and also get the total price of the items.
        When she is done with shopping, she can decide to quit shopping. 
"""


items = [] # create an empty list of items
prices = [] #create an empty list of price

action = '' #set action to nothing
while action != '5': # check if action is equal to 5 
    action = str(input('Please select an action:\n1 Add item \n2 View cart \n3 Remove item \n4 Compute total price \n5 Quit \n'))
    
    if action == '1':
        item = input('What item would you like to add? ')
        price = input(f"What is the price of '{item}'? ")
        price = float(price)
        items.append(item)
        prices.append(price)
    
    elif action == '2':# to view the cart
        if len(items) == 0:# check if the cart is empty
            print("Your cart is empty.") 
        else:
            print(f'The contents of the shopping cart are:')
            for item, price in zip(items, prices): # to make the item and price to be in one index, 
                                                    # then looping through the list of item to get the items and prices
                format_price = f'${price:.2f}'
                print(f'{item} - {format_price}')
    
    elif action == '3':# to remove the index of the selected items
        if len(items) == 0:
            print("Your cart is empty.")
        else:
            index = int(input('What index of the item would you like to remove? (1 to remove the first item) '))
            if 0 <= index < len(items):
                removed_item = items.pop(index - 1)
                removed_price = prices.pop(index - 1)
                print(f'You have removed {removed_item}: ${removed_price:.2f}')
            else:
                print('Invalid index, please enter a valid number.')
    
    elif action == '4': # to print the total price
        total_price = sum(prices)
        format_price = f'${total_price:.2f}'
        print(f'The total price of the items in the cart is: {format_price}')
    
    elif action == '5': #to quit
        print('Thank you for shopping with us. Goodbye.')
    
    else:
        print('Invalid choice, please enter a valid number.')
        

