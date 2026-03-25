# Create an empty list for the shopping cart
shopping_cart = []

# 1. Add items to the cart
shopping_cart.append("Apples")
shopping_cart.append("Bread")
shopping_cart.append("Milk")
shopping_cart.append("Coffee")

print("Cart after adding items:", shopping_cart)

# 2. Remove one item from the cart
shopping_cart.remove("Milk")

print("Cart after removing 'Milk':", shopping_cart)

# 3. Print total items
total_items = len(shopping_cart)

print("Total items in the cart:", total_items)