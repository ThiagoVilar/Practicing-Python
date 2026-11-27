# Activity 06: Understanding the use of break
# Goes through a list of books and shows a message as soon as
# "The Hobbit" is found, stopping the search right after.

books = ['1984', 'Dom Casmurro', 'The Little Prince', 'The Hobbit', 'Pride and Prejudice']

for book in books:
    if book == 'The Hobbit':
        print(f'Book found: {book}')
        break