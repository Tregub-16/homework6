my_dict = {'Vova': 1987,'Lena' :1988,'Oleg' : 1985}
print(my_dict)
print(my_dict['Vova'])
print(my_dict.get('Larisa'))
my_dict.update({'Valera' : 1995, 'Roma' : 2000})
my_dict.pop('Oleg')
print(my_dict)

my_set_={1,1,1,5,5,5,'Vova',10.5,10.5}
print(my_set_)
my_set_.add(2)
my_set_.add(7)
my_set_.discard(5)
print(my_set_)
