data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks():
    peaks = []
    for i in range(len(data)-1):
        if data[i] > data[i + 1] and data[i] > data[i - 1]:
            peaks.append(i)
    return peaks

def valleys():
    valleys = []
    for i in range(len(data)-1):
        if i == 0:
            continue
        if data[i] < data[i + 1] and data[i] < data[i - 1]:
            valleys.append(i)
    return valleys
 
def valleys_and_peaks():
    valleys_and_peaks = peaks() + valleys()
    return valleys_and_peaks

print(valleys_and_peaks())