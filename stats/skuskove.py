def column_to_array(doc_name, col_num):
    col_array = []
    inp = open(doc_name, "r")
    for line in inp.readlines():
        col_array.append(line.split(",")[col_num])
    
    inp.close()
    return col_array

def is_start(date):
    # zaciatok skuskoveho: 05-20 (letne) alebo 01-08 (zimne)
    if date[5:] == "05-20" or date[5:] == "01-08":
        return True
    return False

def is_end(date):
    if date[5:] == "06-30" or date[5:] == "02-14":
        return True
    return False

def select_skuskove(dates):
    # prechadzam zoznam, narazim na koniec skuskoveho, poznacim si index ako zaciatok, 
    # narazim na koniec skuskoveho, oznacim si index ako koniec
    # ulozim ako dvojicu (zaciatok, koniec) do zoznamu
    intervals = []
    for i in range(len(dates)):
        if is_start(dates[i]):
            intervals.append((end, i))
        if is_end(dates[i]):
            end = i
    
    return intervals

def get_skuskove(intervals, times):
    skuskove = []
    for interval in intervals:
        for i in range(interval[0], interval[1]+1):
            skuskove.append(times[i])
    
    return skuskove

def get_mimo(intervals, times):
    mimo = []
    start = 0
    for interval in intervals:
        end = interval[0]
        for i in range(start, end):
            mimo.append(times[i])
        start = interval[1] + 1
    end = len(times)
    for i in range(start, end):
        mimo.append(times[i])
    
    return mimo