countries = {
    'Ethiopia': 'Addis Ababa',
    'Germany': 'Berlin',
    'USA': 'Washington',
    'Poland': 'Warsaw'
}

#for countries in countries.items():
#    print(countries)

#To get the values of each key
print('The capital of Ethiopia is ' + countries.get('Ethiopia'))

#to give a key or add a key
countries.update({'Japan': 'Tokyo'})
print(countries)

#to print all the keys in the dictionary use .key method
key = countries.keys()
print(key)

#to print all the values in the dictionary use .values method

values = countries.values()
for value in countries.values():
    print(value)

#to print  an items list of 2D tuples use .items method

items = countries.items()
for key, value in items:
    print(f"{key} : {value}")

#To remove a key use pop

countries.pop('USA')
print(countries)

#to remove the last item that was added use popitem and it will remove the last added item

countries.popitem()
print(countries)

#to clear all items use clear method
countries.clear()
print(countries)