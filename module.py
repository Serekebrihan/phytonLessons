print('The module has been imported.....')

year = 2007
year2 = 2008
year3 = 2009
year4 = 2010
year5 = 2011

def car_check(cars, brand):
    for car in cars:
        if brand == car:
            return True
    return False