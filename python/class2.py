#cooment place here
dict = {'key1': 'geeks', 'key2': 'for'}
print("Current Dict is:" , dict)
 
# adding key3
dict.update({'key3': 'geeks'})
print("Updated Dict is:", dict)
 
# adding dict1 (key4 and key5) to dict
dict1 = {'key4': 'is', 'key5': 'fabulous'}
dict.update(dict1)
print("After adding dict1 is:" , dict)
 
# by assigning
dict.update(newkey1='portal')
print("After asssigning new key:" , dict)