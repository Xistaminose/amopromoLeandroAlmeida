names = {1: 'Alice',
         2: 'Bob',
         3: 'Carl',
         4: 'Ann',
         5: 'Liz'}

# def filter_dict(d, f):
#     newDict = dict()
#     for key, value in d.items():
#         if f(key, value):
#             newDict[key] = value
#     return newDict

# print(filter_dict(names, lambda k,v: k%2==1))
# print(filter_dict(names, lambda k,v: v.startswith('A')))


#print(dict(filter(lambda v: v[0]%2 == 0, names.items())))

x = ({k:v for (k,v) in names.items() if k%2 == 0})
print(x)
