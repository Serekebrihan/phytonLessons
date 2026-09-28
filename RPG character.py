full_dot = '●'
empty_dot = '○'

def create_character(char_name, stats1, stats2, stats3):
    if not isinstance(char_name, str):
        return 'The character name should be a string'
    elif not char_name:
        return 'The character should have a name'
    elif len(char_name) > 10:
        return 'The character name is too long'
    elif ' ' in char_name:
        return 'The character name should not contain spaces'
    elif not isinstance(stats1, int) or not isinstance(stats2, int) or not isinstance(stats3, int):
        return 'All stats should be integers'
    elif stats1 < 1 or stats2 < 1 or stats3 < 1:
        return 'All stats should be no less than 1'
    elif stats1 >4 or stats2 >4 or stats3 >4:
        return 'All stats should be no more than 4'
    elif stats1 + stats2 + stats3 != 7:
        return 'The character should start with 7 points'
    else:
        return f"{char_name}\nSTR {full_dot * stats1}{empty_dot * (10 - stats1)}\nINT {full_dot * stats2}{empty_dot * (10 - stats2)}\nCHA {full_dot * stats3}{empty_dot * (10 - stats3)}"


print(create_character('ren', 4, 2, 1))
message = 'Python is fun!!'

print(message[0:6])  # Python
print(message[7:])  # is fun!
print(message[::2])  # Pto sfn
trimmed_str = message.strip()
print(len(trimmed_str))
print(trimmed_str)

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')

developer = 'Naomi'

result = developer.endswith('N') # ?
print(result)


def greet():
    pass


print(greet())  # ?
defewwrewrwerewrweererwerwer = 1
print(defewwrewrwerewrweererwerwer)
example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(joined_str)  # ?