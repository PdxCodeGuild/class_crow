
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    # if value of left and right are less than current point, it is the peak
    peaks_list = []
    for i in range(0, (len(data)-1)):
        if data[i-1] < data[i] > data[i+1]:
            print(data[i-1])
            print(data[i])
            print(data[i+1])
            peaks_list.append(i)
    print(peaks_list)
    return peaks_list
    

def valleys(data):
        # if value of left and right are less than current point, it is the peak
    valleys_list = []
    for i in range(1, (len(data)-1)):
        if data[i-1] > data[i] < data[i+1]:
            print(data[i-1])
            print(data[i])
            print(data[i+1])
            valleys_list.append(i)
    print(valleys_list)
    return valleys_list

def peaks_and_valleys(data):
    combo_list = []
    for i in range(1, (len(data)-1)):
        if data[i-1] > data[i] < data[i+1]:
            print(data[i-1])
            print(data[i])
            print(data[i+1])
            combo_list.append(i)
        elif data[i-1] < data[i] > data[i+1]:
            print(data[i-1])
            print(data[i])
            print(data[i+1])
            combo_list.append(i)

    print(combo_list)
    return combo_list

if __name__ == "__main__":
    peaks(data)
    valleys(data)
    peaks_and_valleys(data)