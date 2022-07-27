input="../ViewingActivity.csv"
i=open(input, "r")

first_line = i.readline()
name="Gabi"
count = 1

out=open("../Student1", "a")
out.write(first_line)

writing = True

while True:
    line = i.readline()
    if not line:
        break

    new_name = line.split(",")[0]
    if name != new_name:
        if new_name == "Kids":
            writing = False
        else:
            writing = True
            count += 1
            out.close()
            name=new_name
            out = open("../Student"+str(count), "a")
            out.write(first_line)
    
    if writing:
        out.write(line)

i.close()