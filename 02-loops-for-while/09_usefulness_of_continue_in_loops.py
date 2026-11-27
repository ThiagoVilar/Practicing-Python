# Activity 09: Usefulness of continue in loops
# Goes through a list of books and shows only the ones in stock.
# Books with no stock are skipped using continue.

books = [
    {'name': '1984', 'stock': 5},
    {'name': 'Dom Casmurro', 'stock': 0},
    {'name': 'The Little Prince', 'stock': 3},
    {'name': 'The Hobbit', 'stock': 0},
    {'name': 'Pride and Prejudice', 'stock': 2},
]

for book in books:
    if book['stock'] == 0:
        continue
    print(f"Book available: {book['name']}")