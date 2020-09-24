def combine():
    
    fruits = ['apple', 'banana', 'pear']
    prices = [1.2, 3.3, 2.1]
  
    fruit_dict = {fruits[i]: prices[i] for i in range(len(fruits))}
    print(fruit_dict)
    return fruit_dict



def average(_dict):
    '''
    Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.
    combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
    average(combined) -> 2.2
    '''
    total = sum(_dict.values())
    average = round(total/len(_dict),2)
    # print(len(_dict))
    print (average)
    return round(average, 2)

def unify():
    '''
    Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.

    d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
    unify(d) -> {'a':3, 'b':4, 'c':5}
    '''
    d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
    unify_dict = {}

    
    for key in d:
        # print (key)
        start_letter = key[0]
        amount = d[key]
        unify_dict[start_letter] = unify_dict.setdefault(start_letter, amount) + amount
        print (unify_dict)
        # print(amount)
        # unify_dict[start_letter] = unify_dict.setdefault(start_letter, 0) 
        # word_dict[word] = word_dict.setdefault(word, 0) + 1
    # print (unify_dict)
    

        


    # fruit_dict = {fruits[i]: prices[i] for i in range(len(fruits))}



    

if __name__ == "__main__":
    # combine()
    # average(combine())
    unify()