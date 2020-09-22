import requests
import csv
import threading

def load():

    with open('hayden_island.rain.txt', 'r') as f:
        f = f.read().splitlines()

        count = 0
        filelist = []
        for line in f:
            if count >= 12:
                filelist.append(line.split())
            count += 1
        
        return filelist
            
def highest_rain_date(filelist):

        raincount = 0
        for line in filelist:
            if line[1] != '-':
                if int(line[1]) > raincount:
                    raincount=int(line[1])
                    highraindate = line[0]


        return highraindate, raincount

def main():

    thread = threading.Thread()
    thread.start()

    filelist = load()

    thread.join()

    print(highest_rain_date(filelist))

main()