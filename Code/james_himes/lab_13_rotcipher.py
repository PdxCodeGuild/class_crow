alpha = 'abcdefghijklmnopqrstuvwxyz'
rotated = 'nopqrstuvwxyzabcdefghijklm'
message = 'message'
stuff = []

for char in message:
    index = alpha.find(char)
    message = rotated[index]
    #print(message)
    stuff.append(message)
print(''.join(stuff))