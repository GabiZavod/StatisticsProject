def next_date(dt):
    """returns following date"""
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    months_4 = [31,29,31,30,31,30,31,31,30,31,30,31]
    mnts = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

    date = dt.split("-")
    y = int(date[0])
    m = int(date[1])
    d = int(date[2])

    if y%4 == 0:
        if d+1 <= months_4[m-1]:
            if d+1<=9:
                day = "0" + str(d+1)
            else: 
                day = str(d+1)
            return str(y) + "-" + mnts[m-1] + "-" + day
        elif d == months_4[m-1]:
            if m == 12:
                return str(y+1) + "-01-01"
            else:
                return str(y) + "-" + mnts[m] + "-01"
    
    else:
        if d+1 <= months[m-1]:
            if d+1<=9:
                day = "0" + str(d+1)
            else: 
                day = str(d+1)
            return str(y) + "-" + mnts[m-1] + "-" + day
        elif d == months[m-1]:
            if m == 12:
                return str(y+1) + "-01-01"
            else:
                return str(y) + "-" + mnts[m] + "-01"

def follows(d1,d2):
    """True if d1 is immediately followed by d2"""
    if d2 == next_date(d1):
        return True
    return False

def add_dates(dates, times):
    """fill up array of dates with missing dates and array of times with zeroes"""
    i = 0
    last = dates[-1]
    while True:
        if dates[i] == last:
            break

        if not(follows(dates[i], dates[i+1])):
            dates.insert(i+1, next_date(dates[i]))
            times.insert(i+1, "0\n")
        i+=1

inp = open("../Student4_2", "r")
o = open("../final_data/Student4", "a")

inp.readline()
lt_line = inp.readline()
last_line = lt_line.split(",")
last_date = last_line[0]
last_time = last_line[1]

while True:
    line = inp.readline()
    if not line:
        break
    
    l = line.split(",")
    date = l[0]
    time = l[1]

    if not(follows(date,last_date)):
        dt = [date,last_date]
        tm = [time,last_time]
        add_dates(dt, tm)
        dt.reverse()
        tm.reverse()

        for i in range(len(dt)-1):
            o.write(dt[i] + "," + tm[i])
        
    else:
        o.write(last_date + "," + last_time)

    last_date = date
    last_time = time

inp.close()
o.close()