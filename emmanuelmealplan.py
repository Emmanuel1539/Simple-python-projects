print()
print('Welcome to our restaurant, please fill the folling questionaires')
child_meal_price = float(input("What's child's meal price?: $"))
adult_meal_price = float(input("what's adult's meal price?: $"))
no_of_children = int(input("What's number of children?: $"))
no_of_adults = int(input("What's number of adults?: $"))
sales_tax_rate = float(input("What's sales tax rate?: $"))
print()


children_meal_subtotal = child_meal_price * no_of_children
adult_meal_subtotal = adult_meal_price * no_of_adults


subtotal = children_meal_subtotal + adult_meal_subtotal
sale_tax = (subtotal * sales_tax_rate)/100

total_meal_price = subtotal + sale_tax


print(f'Your Subtotal is: ${subtotal:.2f}')
print(f'Your sales tax is: ${sale_tax:.2f}')
print(f'Your total price of the meal is: ${total_meal_price:.2f}')

payment_amount = float(input("What is the payment amount?: $"))
change = payment_amount - total_meal_price
print(f'Your change is: ${change:.2f}')
print()
print('Thanks for patronising us!')


