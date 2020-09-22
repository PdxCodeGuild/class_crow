import datetime

def open_files():
    data_points = []
    # opening file, could use requests & url if available
    with open('raindata.txt', 'r') as f:
        rows = f.readlines()
        # offset is incrementing to count how many rows 
        # until we reach the line of dashes
        offset = 0
    for row in rows:
        offset += 1
        row = row.strip()
        if set(row) == set('-'):
            break
    # access the data after the "offset", after the dashes
    # [offset:] is everything after offset
    for row in rows[offset:]:
        row_list = row.split()
        if row_list[1] != '-':
            data_point = {'date':datetime.datetime.strptime(row_list[0], '%d-%b-%Y'),
                            'total_rain':int(row_list[1])}
            data_points.append(data_point)
    return data_points

def max_min(data_points):
    annual_rain = {}

    # find rainiest day using anonymous lambda function
    rainiest_day = max(data_points, key=lambda day: day['total_rain'])

    for data_point in data_points:
        year = data_point['date'].year
        if year in annual_rain.keys():
            annual_rain[year] += data_point['total_rain']
        else:
            annual_rain[year] = data_point['total_rain']
    print(annual_rain)

    max_year = max(annual_rain.items(), key=lambda x: x[1])
    print(max_year)
    min_year = min(annual_rain.items(), key=lambda y: y[1])
    print(min_year)
# open_files()
max_min(open_files())