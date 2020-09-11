def peaks(dataset_ints):
    peaks = []
    last = 0
    sec_last = 0
    count = 0
    for item in dataset_ints:
        if count == 0:
            last = item
        elif count == 1:
            if item < last:
                peaks.append(last)
                sec_last = last
                last = item
            else:
                sec_last = last
                last = item
        elif item > last:
            sec_last = last
            last = item
        elif item < last and last < sec_last:
            sec_last = last
            last = item
        elif item < last and last > sec_last:
            peaks.append(last)
            sec_last = last
            last = item
        count += 1
    return peaks

def valleys(dataset_ints):
    valleys = []
    last = 0
    sec_last = 0
    count = 0
    for item in dataset_ints:
        if count == 0:
            last = item
        elif item < last:
            sec_last = last
            last = item
        elif item > last and last > sec_last:
            sec_last = last
            last = item
        elif item > last and last < sec_last:
            valleys.append(last)
            sec_last = last
            last = item
        count += 1
    return valleys
    
def peaks_and_valleys(dataset_ints):
    peaksandvalleys = []
    lastnum = 0
    sec_lastnum = 0
    count = 0
    for item in dataset_ints:
        if count == 0:
            lastnum = item
        elif count == 1:
            if item < lastnum:
                peaksandvalleys.append(lastnum)
                sec_lastnum = lastnum
                lastnum = item
            else:
                sec_lastnum = lastnum
                lastnum = item
        elif item > lastnum and lastnum < sec_lastnum:
            peaksandvalleys.append(lastnum)
            sec_lastnum = lastnum
            lastnum = item
        elif item > lastnum and lastnum > sec_lastnum:
            sec_lastnum = lastnum
            lastnum = item
        elif item < lastnum and lastnum > sec_lastnum:
            peaksandvalleys.append(lastnum)
            sec_lastnum = lastnum
            lastnum = item
        elif item < lastnum and lastnum < sec_lastnum:
            sec_lastnum = lastnum
            lastnum = item
        count += 1
    return peaksandvalleys

def print_data(dataset_ints):
    peaks_var = peaks(dataset_ints)
    biggestPeak = 0
    count = 0
    for item in peaks_var:
        if item > peaks_var[count]:
            biggestPeak = item
        count += 1
    total_count = len(dataset_ints) * biggestPeak
    print_count = 0
    count == biggestPeak
    while print_count <= total_count:
        for item in dataset_ints:
            if item < count:
                print('O')
            elif item >= count:
                print('X')
        print('\n')        
        print_count += 1

def main():
    userinput = input('What would you like to get from your data?\n1)Peaks\n2)Valleys\n3)Both\n4)Print Data: \n')
    dataset = input('Enter your data values separated by commas (,): ')
    dataset = dataset.split(',')
    dataset_ints = []
    for item in dataset:
        dataset_ints.append(int(item))
    print(dataset_ints)
    if userinput == '1':
        print(peaks(dataset_ints))
    elif userinput == '2':
        print(valleys(dataset_ints))
    elif userinput == '3':
        print(peaks_and_valleys(dataset_ints))
    elif userinput == '4':
        print_data(dataset_ints)
        
main()

