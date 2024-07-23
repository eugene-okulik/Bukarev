symbol = '='
symbol *= 40

my_dict = {'tuple': (1, 5, 6, 8, 10), 'list': ['test', 1, 2, 'hello', 100],
           'dict': {'test1': 1, 'test2': 6, 'test3': 22, 'test4': 'TEST', 'test5': 77}, 'set': {1, 5, 'Privet', 7, 99}}

print(symbol)
print(my_dict['tuple'][-1])

my_dict['list'].append(46)
print(my_dict)
print(symbol)

poped = my_dict['list'].pop(1)
print(my_dict['list'])
print(poped)
print(symbol)

my_dict['dict']['i am a tuple'] = 'test_add_new_value'
print(my_dict['dict'])

poped2 = my_dict['dict'].pop('test2')
print(poped2)
print(my_dict['dict'])
print(symbol)

my_dict['set'].add(100)
print(my_dict['set'])

poped3 = my_dict['set'].remove(5)
print(poped3)
print(my_dict['set'])
print(symbol)

print(my_dict)
