# Activity 07: Inventory control
# Simulates the sales of a book with an initial stock of 5 copies.
# Shows a message after each sale and, when the stock runs out,
# shows that it is sold out.

stock = 5

while stock > 0:
    stock -= 1
    print(f'Sale completed! Remaining stock: {stock}')

print('Out of stock')