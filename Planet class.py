class Planet:
    def __init__(self, name, planet_type, star):
        try:
            if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
                raise TypeError('name, planet type, and star must be strings')
            if name == '' or planet_type == '' or star == '':
                raise ValueError('name, planet_type, and star must be non-empty strings')
            self.name = name
            self.planet_type = planet_type
            self.star = star
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


planet_1 = Planet("earth", "round", "")
planet_2 = Planet("mars", "round", "earth")
planet_3 = Planet("jupiter", "round", "earth")

print(planet_1)
print(planet_2)
print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())


###
#### The above solution will also has the same output but Freecodecamp wont accept it
####
####
class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        if name == '' or planet_type == '' or star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


planet_1 = Planet("earth", "round", "sun")
planet_2 = Planet("mars", "round", "earth")
planet_3 = Planet("jupiter", "round", "earth")

print(planet_1)
print(planet_2)
print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())