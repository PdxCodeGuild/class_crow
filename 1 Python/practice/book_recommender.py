import requests
import random 
from bs4 import BeautifulSoup

#get response from website
response = requests.get('https://www.goodreads.com/genres/science-fiction')

#turn it into html string that python can use
html = BeautifulSoup(response.text, 'html.parser')

#find all relevant divs on the page
divs = html.find_all('div')

books = []
# Loop over them
for div in divs:
  classes = div.get('class')
  # If they have a class called 'coverWrapper'...
  if classes and 'coverWrapper' in classes:
    # Find the link and title of the book
    title = div.find('img')['alt']
    link = div.find('a')['href']
    # Add to our books list
    book = (title, link)
    books.append(book)

book_suggestions = []
books_found = 0
while books_found < 10:
    suggested_book = random.choice(books)
    if suggested_book not in book_suggestions:
        #add to the list
        book_suggestions.append(suggested_book)
        books_found += 1

print("We suggest these books:")
print("-----------------------\n")
for suggested_book in book_suggestions: 
    # tuple unpack our title and link
    title, link = (suggested_book)
    print(title)
    print(f"https://www.goodreads.com{link}\n")
    # print(suggested_book)
