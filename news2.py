my_list = [42, 43]
my_dict = {
    'foo': {'a':12,
            'b': (1, 2, 3, 4, my_list)
            },
    'bar':{'c':12,
           'd':{5, 6, 7, 8}
           },
    'moo':{'e':12,
           'f':{'Lol':['L', 'o', 'l']}}}
print('4.', my_dict['foo']['b'])
print('5.', my_dict['bar']['d'])
my_dict['bar']['d'].add(9)
print('6.', my_dict['bar']['d'])