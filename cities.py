import math

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
    usr_spr = 60
    usr_summ = 75
    usr_aut = 60
    usr_win = 40
    
    calc(usr_spr, usr_summ, usr_aut, usr_win)
    return

def printCities():
    for i in range (0,100):
        print str(i) + str(cities[i].name) + "spring: " + str(cities[i].spr) + "summer: " + str(cities[i].summ) + "autumn: " + str(cities[i].aut) + "winter: " + str(cities[i].win)
    return

def addEntireCity(city_id, cityObject):
    cities[city_id] = cityObject
    return

def calc(usr_spr, usr_summ, usr_aut, usr_win):
	for i in range(0, 100):
		spr = cities[i].spr
		summ = cities[i].summ
		aut = cities[i].aut
		win = cities[i].win

		dif1sq = math.pow(abs(usr_spr - float(spr)),2)
		dif2sq = math.pow(abs(usr_summ - float(summ)),2)
		dif3sq = math.pow(abs(usr_aut - float(aut)),2)
		dif4sq = math.pow(abs(usr_win - float(win)),2)
		
		total = dif1sq + dif2sq + dif3sq + dif4sq
		score = math.sqrt(total)
		print str(i) + "City name: " + str(cities[i].name) + "score: " + str(score)
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
