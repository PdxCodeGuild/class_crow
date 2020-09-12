def word_counter():  

    book = open('/home/jpchato/class_crow/Code/jesse_pena/labs/lab_21.txt', 'r')
    contents = book.read()
    contents = contents.lower()
    word_dict = {}
    


    # reference: https://stackoverflow.com/a/21853764

    # The setdefault() method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value

    for word in contents.replace('?', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('-', '').replace(',', '').replace('/', '').replace('\\', '').replace(':', '').replace('$', '').replace('%', '').replace('*', '').replace('"', '').replace('_', '').split():

        word_dict[word] = word_dict.setdefault(word, 0) + 1
       

    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

def pair_counter():
    book = open('/home/jpchato/class_crow/Code/jesse_pena/labs/lab_21.txt', 'r')
    contents = book.read()
    contents = contents.lower()
    pair_dict = {}
    clean_words = []
    
    


    # reference: https://stackoverflow.com/a/21853764

    # The setdefault() method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value

    for word in contents.replace('?', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('-', '').replace(',', '').replace('/', '').replace('\\', '').replace(':', '').replace('$', '').replace('%', '').replace('*', '').replace('"', '').replace('_', '').split():
        clean_words.append(word)
    
    for i in range(len(clean_words) - 1):
        # print(clean_words[i])
        # print(clean_words[i+1])
        word_pair = clean_words[i] + ' ' + clean_words[i + 1]
        pair_dict[word_pair] = pair_dict.setdefault(word_pair, 0) + 1
        
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(pair_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    

def user_input_tracker():
    book = open('/home/jpchato/class_crow/Code/jesse_pena/labs/lab_21.txt', 'r')
    contents = book.read()
    contents = contents.lower()
    clean_words = []
    user_dict = {}

    for word in contents.replace('?', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('-', '').replace(',', '').replace('/', '').replace('\\', '').replace(':', '').replace('$', '').replace('%', '').replace('*', '').replace('"', '').replace('_', '').split():
        clean_words.append(word)


    user_input = input('Pick a word that is in the book. Be patient for results: ').lower()
    # user_input = 'the'
    
    for i in range(len(clean_words) - 1):
        if user_input in clean_words:
            if user_input == clean_words[i]:
                
                user_pair = clean_words[i] + ' ' + clean_words[i + 1]
            
                user_dict[user_pair] = user_dict.setdefault(user_pair, 0) + 1
        elif user_input not in clean_words:
            print('The word is not in the book')
            user_input_tracker()


            

    # print(user_dict)
    
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(user_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    

if __name__ == "__main__":
    word_counter()
    pair_counter()
    user_input_tracker()