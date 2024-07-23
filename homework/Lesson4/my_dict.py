my_dict = {'tuple': (1, 5, 6, 8, 10), 'list': ['test', 1, 2, 'hello', 100],
           'dict': {'test1': 1, 'test2': 6, 'test3': 22, 'test4': 'TEST', 'test5': 77}, 'set': {1, 5, 'Privet', 7, 99}}

print(my_dict['tuple'][-1])

my_dict['list'].append(46)
print(my_dict)