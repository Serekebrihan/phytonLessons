
def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        pattern = ''
        for i in range(n):
            if i == n - 1:
                pattern += str(i+1)
            else:
                pattern +=  str(i + 1) + " "
        return pattern
print(number_pattern(5))

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3))

