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
        # print(item[1])
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
            # print(rainiest_day)
            # print(rainiest_day_rainfall)

    the_rainiest = (rainiest_day, rainiest_day_rainfall)
    print(f'The rainiest day was {rainiest_day}, {rainiest_day_rainfall} inches fell that day')
    return the_rainiest

def rainiest_year(data_list):
    average_yearly = 0
    year = ''
    year_list = []

    for item in data_list:
        date = datetime.strptime(item[0],'%d-%b-%Y')
        # print(date.year)
        date = date.year
        rainfall = item[1]
        year_list.append((date, rainfall))
        
    for pair in year_list:
        print(pair)
    
    for i in range(len(year_list)):
        if year_list[i] == year_list[i-1]:
             

    #     counter = 0
    #     sum = 0
    
    #     if date == date:
    #         # print('whatup')
    #         counter += 1
    #         sum += item[1]
    #         if sum/counter > average_yearly:
    #             average_yearly = sum/counter
    #             year = date
    #             print(average_yearly)
    #             print(year)
    # print(average_yearly)
    # print(year)


    

    



if __name__ == "__main__":
    load_data('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain')
    # average(load_data('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain'))
    # rainiest_day(load_data('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain'))
    rainiest_year(load_data('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain'))