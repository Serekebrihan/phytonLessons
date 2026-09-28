my_sets = {1, 2, 3, 4, 5}
my_sets_1 = {1,2,3,4}
print(my_sets)

my_sets.add(6)
my_sets.add(5)# note that if the set has already values in it will not be added
print(my_sets)

my_sets.remove(5)
#my_sets.remove(5)
my_sets.discard(5) # note that unlike remove this will not give error messeges
print(my_sets)
#my_sets.clear()
print(my_sets)

print(my_sets.issubset(my_sets_1))
my_sets.add(5)
print(my_sets.issuperset(my_sets_1))
print(my_sets.difference(my_sets_1))
print(my_sets.isdisjoint(my_sets_1))

my_sets_2 = my_sets | my_sets_1
print(my_sets_2)
my_sets_3 = my_sets_2 & my_sets_1
print(my_sets_3)
my_sets_4 = my_sets - my_sets_1
print(my_sets_4)
my_sets_4.add(5)
my_sets_4.add(6)
my_sets_4.add(7)
print(my_sets_4)
my_sets.remove(5)
print(5 in my_sets)
print(my_sets)
my_sets_5 = my_sets_4 ^ my_sets
print(my_sets_5)