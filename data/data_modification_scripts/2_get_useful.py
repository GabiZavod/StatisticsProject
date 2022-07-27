def time_add(time1,time2):
    """returns the sum of two times in HH:MM:SS format"""
    t1=time1.split(":")
    t2=time2.split(":")

    sec1=int(t1[2])
    min1=int(t1[1])
    h1=int(t1[0])

    sec2=int(t2[2])
    min2=int(t2[1])
    h2=int(t2[0])

    sec=sec1+sec2
    s = sec % 60
    if s <= 9: 
        seconds = "0" + str(s)
    else:
        seconds = str(s)
    s_carry = sec // 60

    min = s_carry+min1+min2
    m = min % 60
    if m <= 9:
        minutes = "0" + str(m)
    else:
        minutes = str(m)
    m_carry = min // 60

    h = h1+h2+m_carry
    if h <= 9:
        hours = "0" + str(h)
    else:
        hours = str(h)

    return hours + ":" + minutes + ":" + seconds

def convert_time(t):
    """converts time from HH:MM:SS format to hours rounded to 4 decimals"""
    time = t.split(":")
    hours = float(time[0]) + float(time[1])/60 + float(time[2])/3600
    return str(round(hours,4))

# Musim tam pridavat nazvy suborov manualne, nechce sa mi to vymýšľať aby to šlo automaticky
input="../Student4"
i=open(input, "r")

output="../Student4_2"
o=open(output, "a")

i.readline()
line = i.readline()
current_date = line.split(",")[1].split()[0]
current_time = line.split(",")[2]

while True:
    line=i.readline()

    if not line:
        break

    line_strip=line.split(",")
    # zapamatám si deň
    date = line_strip[1].split()[0]
    # zapamätám si čas
    time = line_strip[2]
    
    # Pokiaľ je dátum ten istý, llen pričítam k času strávenom na Netflixe v ten deň
    if date == current_date:
        current_time = time_add(current_time,time)
    
    # ak sú dátumy rôzne, prepočítam čas do hodín a zapíšem do výstupného súboru
    else:
        t = convert_time(current_time)
        o.write(current_date + "," + t + "\n")
        current_date = date
        current_time = time

o.close()
i.close()