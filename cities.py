cities = { }
def main():
    myfile = open('cities.txt', 'r')
    
    i = 0
    counter = 0
    
    while (i < 500):
        name = myfile.readline()
        spr = myfile.readline()
        summ = myfile.readline()
        aut = myfile.readline()
        win = myfile.readline()
        newCity = City(name, spr, summ, aut, win)
        addEntireCity(counter, newCity)
        i += 5
        counter += 1
    
    printCities()
    return

def printCities():
    for i in range (0,100):
        print str(cities[i].name) + "spring: " + str(cities[i].spr) + "summer: " + str(cities[i].summ) + "autumn: " + str(cities[i].aut) + "winter: " + str(cities[i].win)
    return

def addEntireCity(city_id, cityObject):
    cities[city_id] = cityObject
    return

class City:
    """ Object for modelling a city """
    def __init__(self, name, spr, summ, aut, win):
        self.name = name
        self.spr = spr
        self.summ = summ
        self.aut = aut
        self.win = win
        return
        
if __name__ == "__main__":
    main()
