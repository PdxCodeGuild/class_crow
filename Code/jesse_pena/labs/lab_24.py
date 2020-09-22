import requests
from datetime import datetime
import csv
import math

def load_data(url):

    data = []
    response = requests.get(url)

    lines = response.text.split('\n')
    lines = lines[11:-1]

    for line in lines:
        columns = line.split()

        
        date = columns[0]
        daily_total = columns[1]

        if daily_total == '-':
            continue
        data_tuple = (date, int(daily_total))
        data.append(data_tuple)
            

    return data
        
def average(data_list):
    
    grand_total = 0
    for item in data_list:
        grand_total += item[1]
    mean = round(grand_total/len(data_list),2)

    print(f'The mean is {mean} for {grand_total} inches of rain divided by {len(data_list)} days')
    return mean

def rainiest_day(data_list):
    rainiest_day = ''
    rainiest_day_rainfall = 0
    for item in data_list:
        if item[1] > rainiest_day_rainfall:
            rainiest_day = item[0]
            rainiest_day_rainfall = item[1]

    the_rainiest = (rainiest_day, rainiest_day_rainfall)
    print(f'The rainiest day was {rainiest_day}, {rainiest_day_rainfall} inches fell that day')
    return the_rainiest

def rainiest_year(data_list):

    year_list = []
    dict_1 = {}

    for item in data_list:
        date = datetime.strptime(item[0],'%d-%b-%Y')
        date = date.year
        rainfall = item[1]
        year_list.append((date, rainfall))

    
    for i in year_list:
        dict_1.setdefault(i[0],[]).append(i[1])

    highest_year = ''
    highest_average_yearly_rainfall = 0
    for key in dict_1:
        if sum(dict_1[key])/12 > highest_average_yearly_rainfall:
            highest_year = key
            highest_average_yearly_rainfall = sum(dict_1[key])/12
    print(f'The year {highest_year} had the highest average yearly rainfall with {round(highest_average_yearly_rainfall, 2)} inches on average')

if __name__ == "__main__":
    load_data('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain')
    average(load_data('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain'))
    rainiest_day(load_data('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain'))
    rainiest_year(load_data('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain'))