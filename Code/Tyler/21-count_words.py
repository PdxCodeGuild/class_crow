
import string

def main():

    punctuation = string.punctuation
    words = {}
    book = open('book.txt', 'r').read()
    # book.close()
    with open('book.txt', 'r') as f:
        for thing in punctuation:
            book = book.replace(thing, '')

    book = book.lower()

    book = book.replace(' ', '')
    
    book.split()

    dictionary = {}
    for item in book:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary.update({item:1})
        
    words = list(dictionary.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

    # print(book)
    #     for thing in punctuation:
    #         print(thing)
    #         book = str(f.read()).replace(thing, '')
    #         # book = f.read()
    #     print(str(f.read()))
        



main()