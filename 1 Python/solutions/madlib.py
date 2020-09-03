from functools import reduce

MadLib = 'Hello, Im {name}, I am a {adj} person, and I like to {verb} and {verb}'

def writesMadLib():
    wordList = []
    repetitions = MadLib.count('{')
    end = 0
    for i in range(repetitions):
        start = MadLib.find('{', end) + 1
        end = MadLib.find('}', start)
        key = MadLib[start: end]
        wordList.append(key)
    # return list of types of words from the madli
    # ex:  return: ['[name]', '[adj]', '[verb]']
    # print(wordList)
    return wordList

def display(wordDict, MadLib):
    # functional soluction: had to import reducers
    completeLib = reduce(lambda a, kv: a.replace(*kv), wordDict.items(), MadLib)
    #     for item in wordDitct:
    #       MadLib.replace(key, wordDict[key]) 
    print(completeLib)

def playMadLib(madlib):
    wordPicks = {}

    for word in madlib:
        choice = input(f"give me a {word}: ")
        wordPicks.update({word : choice})
    print(wordPicks)

    display(wordPicks, MadLib)


playMadLib(writesMadLib())

writesMadLib()