def peaks(data):
    # if value of left and right are less than current point, it is the peak
    for i in range(len(data)):
        left = data[i]
        if data[i-1] > data[i] < data[i+1]:
            
            print(data[i])
    

def valleys(data):
    pass

def peaks_and_valleys(peaks, valleys):
    pass


if __name__ == "__main__":
    peaks([2,2,3,2,2])