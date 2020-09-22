def combine():
    
    fruits = ['apple', 'banana', 'pear']
    prices = [1.2, 3.3, 2.1]
  
    fruit_dict = {fruits[i]: prices[i] for i in range(len(fruits))}
    print(fruit_dict)

if __name__ == "__main__":
    combine()