firends = ['abresh', 'abela', 'yoni', 'hena']
print(firends[0])
print(firends[1])
print(firends[2])
print(firends[3])

print(list(firends[0]))
del firends[3]

for i in range(len(firends)):
    print(firends[i])
print(list(firends))
firends += [['henok', 'hana', 'nardos']]
print(firends)
del firends[3][2]
print(firends)

abresh = ['student', 'taxi', 'open to work']
status, *current_work= abresh
print(status)
print(current_work)
print(firends[1:])

numbers = [1,2,3,4,5,6]
numbers.append(7)
numbers_2 = [8,9,10]
numbers_3 = [11,12,13]

numbers += numbers_2
print(numbers)
numbers.append(numbers_3)
print(numbers)
numbers.extend(numbers_2)
print(numbers)
for i in range(6,len(numbers)-4):
    numbers.insert(i,8)
print(numbers)
numbers.remove(8)
print(numbers)
numbers.reverse()
print(numbers)

print(numbers.index(8))

#Tuples are a data type that can not be alterd later

my_tuople = ('my name is ', 'serekebirhan', 'kahsay', 26, 'yearsold')
print(my_tuople[0])
print(my_tuople)
spelling_abresh = tuple(firends[0])
print(spelling_abresh)

my_list = [1,2,3,4,5,6]
print(my_list)
for i in range(1,len(my_list),2):
    my_list[i] = 2
print(my_list)

students = ('sereke', 'mahider', 'enanu', 'berihu', 'feven', 'aster')


#### Always use a diffrent name for the loop than the variable so that it will not be overwritten when running it example below
####
####       for i, students in enumerate(students):
####            print(students, i)
####
####
####
for i, student in enumerate(students):
    print(student, i)
for student, my_list in zip(students, my_list):
    print(student, my_list)
print(students)

##### Lambda functions

my_numbers = [1,2,3,4,5,6]

my_numbers_squared = list(map(lambda my_number: my_number ** 2, my_numbers))
print(my_numbers_squared )
