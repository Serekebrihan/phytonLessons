class Planet:
    def __init__(self, name, planet_type, star):
        try:
            if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
                raise TypeError
            if name == '' or planet_type == '' or star == '':
                raise ValueError
            self.name = name
            self.planet_type = planet_type
            self.star = star
        except TypeError:
            print('name, planet type, and star must be strings')
        except ValueError:
            print('name, planet_type, and star must be non-empty strings')
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet("earth", "round", "SUN")
planet_2 = Planet("mars", "round", "earth")
planet_3 = Planet("jupiter", "round", "earth")

str(planet_1)
str(planet_2)
str(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())