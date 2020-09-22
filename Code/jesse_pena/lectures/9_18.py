import requests

def load_data(url):
    data = []

    response = requests.get(url)

    lines = response.text.split('\n')

    # print(lines)
    return lines

if __name__ == "__main__":
    load_data('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain')

from datetime import datetime
date = '30-AUG-1998'
formatted_date = datetime.strptime(date, '%d-%b-%Y')
print(formatted_date)
print(formatted_date.year)