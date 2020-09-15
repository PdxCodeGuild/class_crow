import requests
import random
from bs4 import BeautifulSoup

#get response from website
response = requests.get('https://www.goodreads.com/genres/science-fiction')

# turn it into html string that python can use
html = BeautifulSoup(response.text, 'html.parser')

# find all relevant divs on the page
divs = html.find_all('div')

books = []
# loop over divs
for div in divs:
    classes = div.get('class')
    # check for the class we want
    if classes and 'coverWrapper' in classes:
        # find link and title
        title = div.find('img')['alt']
        link = div.find('a')['href']
        book = (title, link)
        books.append(book)


book_suggestions = []
books_found = 0
while books_found < 10:
    suggested_book = random.choice(books)
    if suggested_book not in book_suggestions:
        book_suggestions.append(suggested_book)
        books_found += 1

print('We suggest these books')
print('----------------------\n')
for suggested_book in book_suggestions:
    # tuple unpack our title and link
    title, link = (suggested_book)
    print(title)
    print(f'https://www.goodreads.com{link}\n')
