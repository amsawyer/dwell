from flask import Flask, jsonify
import math
import operator
import requests

cities = { }
def average(usr_spr, usr_summ, usr_aut, usr_win):
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
    
    tup = calc(usr_spr, usr_summ, usr_aut, usr_win) # full 100
    sorted_tup = sort(tup) # sorted 100
    city_list = []
    for i in range (0, 3):
        one_tup = sorted_tup[i]
        city_only = one_tup[0]
        city_list.append(city_only[:-1]) # list of just cities, no scores

    #photos = get_photos(city_list)

    return city_list

def printCities():
    for i in range (0,100):
        print str(i) + str(cities[i].name) + "spring: " + str(cities[i].spr) + "summer: " + str(cities[i].summ) + "autumn: " + str(cities[i].aut) + "winter: " + str(cities[i].win)
    return

def addEntireCity(city_id, cityObject):
    cities[city_id] = cityObject
    return

def calc(usr_spr, usr_summ, usr_aut, usr_win):
    name_list = []
    score_list = []
    for i in range(0, 100):
        spr = cities[i].spr
        summ = cities[i].summ
        aut = cities[i].aut
        win = cities[i].win

        dif1sq = math.pow(abs(float(usr_spr) - float(spr)),2)
        dif2sq = math.pow(abs(float(usr_summ) - float(summ)),2)
        dif3sq = math.pow(abs(float(usr_aut) - float(aut)),2)
        dif4sq = math.pow(abs(float(usr_win) - float(win)),2)
        
        total = dif1sq + dif2sq + dif3sq + dif4sq
        score = math.sqrt(total)

        # Add to lists
        name_list.append(str(cities[i].name))
        score_list.append(score)
        # print str(i) + "City name: " + str(cities[i].name) + "score: " + str(score)

    # Create 2-tuple of names and scores
    tup = zip(name_list, score_list)
    return tup

def sort(tup):
    tup.sort(key=operator.itemgetter(1))
    return tup

'''
def get_photos(city_list):
    photo_urls = []
    for i in range (0, 3):
        url = "https://api.shutterstock.com/v2/images/search?per_page=1&query=" + city_list[i]
        # necessary URL formatting modifications
        url = url.replace(" ", "+")
        comma_idx = url.rfind(",")
        url = url[0:comma_idx]
        print url
        response = requests.get(url)
        response_dict = response.json()
        photo_url = (response_dict.get("large_thumb")).get("url")
        print photo_url
        photo_urls.append(photo_url)
       
    print photo_urls
    return photo_urls
'''

class City:
    ''' Object for modelling a city '''
    def __init__(self, name, spr, summ, aut, win):
        self.name = name
        self.spr = spr
        self.summ = summ
        self.aut = aut
        self.win = win
        return
        
if __name__ == "__main__":
    main()
