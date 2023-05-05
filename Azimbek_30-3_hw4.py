data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple :
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

del numbers [0]
numbers.insert(2,2)
numbers.sort()
letters.reverse()
letters[0]= 'G'
letters[6]= 'c'
letters.insert(0,numbers[0])
del numbers [0]
numbers = [i*i for i in numbers]

letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)

print(letters_tuple)
print(numbers_tuple)


