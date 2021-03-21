# creating a dictionary
d = {'a':'value',
    'b': 2,
    'c': 'a to jest wartosc',
    'd': ['d1', 'd2', 'd3']}

# print('d["a to jest wartosc"] = ', d["a to jest wartosc"])
# print('d[1] = ', d[1])
# print('d["key"] = ', d["key"])
# print('to jest wartosc["d"] = ', d['d'])

my_dict = {1:'apple', 2:'ball'}

# using dict()
my_dict = dict({3:'apple', 4:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball'), (3,'dupa'), (4,'dupa4'), (5,'dupa5')])

# fromkeys(seq[, v]) - create new dictionary based on the sequence and can assign default values to the keys
print ("\n# fromkeys(seq[, v]) - create new dictionary based on the sequence and can assign default values to the keys")
dupaseq = ['j', 'Number 5', 't', 'Number 8']
print("dupaseq = ['j', 'Number 5', 't', 'Number 8']")
testfromkeys = my_dict.fromkeys(dupaseq, 'default value test')
print("testfromkeys = my_dict.fromkeys(dupaseq, 'default value test')")
print("testfromkeys:" ,testfromkeys)

# getting list of keys from dictionary
print("\n# getting list of keys from dictionary")
print("my_dict.keys() = ", my_dict.keys())

# getting list of values from dictionary
print("\n# getting list of values from dictionary")
print("my_dict.values() = ", my_dict.values())

# Removing item from dictionary
print("\n# Removing item from dictionary")
my_dict = dict([(1,'apple'), (2,'ball'), (3,'dupa'), (4,'dupa4'), (5,'dupa5')])
del my_dict[2]
print("del my_dict[2] \nmy_dict = ", my_dict)

# pop() - Popping the item from dictionary - removes the item from dictionary, the value can be assigned to variable
print("\n# pop() - Popping the item from dictionary - removes the item from dictionary, the value can be assigned to variable")
my_dict = dict([(1,'apple'), ('dwa','ball'), (3,'dupa'), (4,'dupa4'), (5,'dupa5')])
popDwa = my_dict.pop('dwa')
print("my_dict.pop('dwa') = ", popDwa)

# popitem() - Pops the item from dictionary as a tupple (Key & Value)
print("\n# popitem() - Pops the item from dictionary as a tupple (Key & Value)")
popitem2 = my_dict.popitem()
print("my_dict.popitem() = ", popitem2)
print("type(popitem2) = ", type(popitem2))
print("len(popitem2) = ", len(popitem2))
print("popitem2[1] = ", popitem2[1])

# For loop through dictionary
for i in range(10):
    if i not in my_dict.keys():
        my_dict[i] = 'Number ' + str(i)

print("\nmy_dict = ", my_dict)
items = my_dict.items()
print("type(my_dict): ", type(my_dict))

print("\nitems = my_dict.items(): ", items )
print("type(my_dict.items()): ", type(items))


new_dict = {x: x*2 for x in range(5)}
print("\nnew_dict = {x: x*2 for x in range(5)}")
print("new_dict = ", new_dict)


