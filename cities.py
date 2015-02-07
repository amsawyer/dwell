cities = { }
def main():
	myfile = open('cities.txt', 'r')
	
	i = 0;
	counter = 0;
	
	print "hello"
	for line in myfile:
		print(i)
		print(line)
		if(i%5==0):
			name = line
			newCity = City(name)
		if((i-1)%5==0):
			newCity.addSpr(line)
		if((i-2)%5==0):
			newCity.addSumm(line)
		if((i-3)%5==0):
			newCity.addAut(line)
		if((i-3)%5==0):
			newCity.addWin(line)
		addEntireCity(counter, newCity)
		i = i+1
		counter = counter + 1
	
	printCities()
	return

def printCities():
	for i in range (0,100):
		print str(cities[i].name) + "spr: " + str(cities[i].spr) + "\n"
	return

def addEntireCity(city_id, cityObject):
	cities[city_id] = cityObject
	return

class City:
	""" Object for modelling a city """
	def __init__(self,name):
		self.name = name
		return	
	def addSpr(self,spr):
		self.spr = spr
		return
	def addSumm(self,summ):
		self.summ = summ
		return
	def addAut(self,aut):
		self.aut = aut
		return
	def addWin(self,win):
		self.win = win
		return
		
if __name__ == "__main__":
	main()

