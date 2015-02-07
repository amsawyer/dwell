cities = { }
def main():
<<<<<<< HEAD
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

=======
	myfile = open('cities.txt', 'r')
	
	i = 5;
	counter = 0;
	for line in myfile:
		if(i%5==0):
			name = line
			newCity = City(name)
		elif((i-1)%5==0):
			newCity.addSpr(line)
		elif((i-2)%5==0):
			newCity.addSumm(line)
		elif((i-3)%5==0):
			newCity.addAut(line)
		elif((i-3)%5==0):
			newCity.addWin(line)

		if(i%5==0):
			addEntireCity(counter, newCity)
			counter = counter + 1
		i = i + 1
	
	printCities()
	return

def printCities():
	for i in range (0,100):
		print str(i) + " " + str(cities[i].name) + "spr: " + str(cities[i].spr) + "summ" + str(cities[i].summ) + "aut: " + str(cities[i].aut) + "win: " + str(cities[i].win)+"\n"
	return
    
>>>>>>> master
def addEntireCity(city_id, cityObject):
    cities[city_id] = cityObject
    return

class City:
<<<<<<< HEAD
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
=======
	""" Object for modelling a city """
	def __init__(self,name):
		self.name = name
	def addSpr(self,spr):
		self.spr = spr
	def addSumm(self,summ):
		self.summ = summ
	def addAut(self,aut):
		self.aut = aut
	def addWin(self,win):
		self.win = win
		
if __name__ == "__main__":
	main()
>>>>>>> master
