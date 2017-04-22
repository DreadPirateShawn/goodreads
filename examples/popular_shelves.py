from goodreads import client
import json

#authetification
gc = client.GoodreadsClient('fCUHaHylHEkSW3jJcZJTQ', 'dOKwd2Kewa5sIpoAynUEVl44s5wscrwWoAiGwBuijTI')

#get all books by query
books = gc.search_books('Ali Vali', search_field='author')

for book in books:
    print(book.popular_shelves)
