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
print('1.', my_dict['foo'])
print('2.', my_dict['foo']['b'])
my_list.append(44)
print('3.', my_list)