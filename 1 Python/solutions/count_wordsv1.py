import string, os

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn', 'one', 'gutenbergtm', 'gutenberg']

with open('dracula.txt', encoding='utf-8') as file:
    contents = file.read()

# takes list of works, returns dictionary containing words & counts
def count_words(words):
    word_dict = {}
    pair_dict = {}
    for i in range(len(words)):
        word = words[i]
        if word not in stop_words:
            word_dict[word] = word_dict.get(word, 0) + 1
        if i < len(words) - 1:
            if (words[i] not in stop_words) and (words[i+1] not in stop_words):
                pair = (words[i], words[i+1])
                pair_dict[pair] = pair_dict.get(pair, 0) + 1
    return (word_dict, pair_dict)

# takes entire text, returns list of words
def split_words(text):
    translator  = str.maketrans('', '', string.punctuation)
    no_punct = text.translate(translator)
    return no_punct.lower().split()

def most_frequent(counter, num=10):
    counter = list(counter.items())
    counter.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(num, len(counter))):  # print the top 20 words, or all of them, whichever is smaller
        print(counter[i])  

# print(count_words(split_words(contents)))

def main():
    single_count, pair_count = count_words(split_words(contents))
    print('-'*48)
    most_frequent(single_count, 5)
    print('-'*48)
    most_frequent(pair_count, 5)


main()