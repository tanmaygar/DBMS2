import time

start_time = time.time()
f = open("source.txt", "r", encoding="utf-8")
op = open("list_of_venue.txt", "w", encoding="utf-8")

list_venue = []
count = 0
while True:
    line = f.readline()
    count = count + 1
    if not line:
        break
    if line[0] == '#' and line[1] == 'c':
        x = line[2:]
        x = x.rstrip()
        list_venue.append(x)
set_venue = set(list_venue)
list_venue = list(set_venue)
list_venue.sort()
print(time.time()-start_time)
for venue in list_venue:
    op.write(venue + '\n')
