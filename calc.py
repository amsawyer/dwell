from cities import cities

def main():
	usr_spr = 10
	usr_summ = 20
	usr_aut = 30
	usr_win = 40

	calc(usr_spr, usr_summ, usr_aut, usr_win)

	return

def calc(usr_spr, usr_summ, usr_aut, usr_win):
	print str(cities[5].name)

	# for i in range(0, 100):
	for i in range(0,2):
		spr = cities[i].spr
		dif1 = abs(usr_spr - spr)
		print "diff spring = " + str(dif1)
	return


if __name__=="__main__":
	main()
