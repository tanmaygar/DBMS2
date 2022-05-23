import time
from thefuzz import process
from thefuzz import fuzz

start_time = time.time()
f = open("source.txt", "r", encoding="utf-8")
op = open("names_all.txt", "w", encoding="utf-8")
op2 = open("names_line.txt", "w", encoding="utf-8")
list_names = []
count = 0
while True:
    line = f.readline()
    count = count + 1
    if not line:
        break
    if line[0] == '#' and line[1] == '@':
        x = line[2:].split(',')
        # new_x = []
        # for ind in range(len(x)):
        #     new_x.extend(x[ind].split(','))
        # # x = re.split(r',|,\s|', line[2:])
        # x = new_x
        for i in range(len(x)):
            new_name = x[i].rstrip()
            if len(new_name) >= 1:
                if new_name[0] == " ":
                    new_name = new_name[1:]
            op2.write("{}: {}\n".format(count, new_name))
            list_names.append(new_name)

# print(list_names)
print(len(list_names))
print(len(set(list_names)))
set_names = set(list_names)
list_names = list(set_names)
list_names.sort()
for i in range(len(list_names)):
    # if len(list_names[i]) <= 4:
    #     print(list_names[i])
    op.write((list_names[i] + '\n'))
op.close()
f.close()

list_names.pop(0)
for i in range(len(list_names)):
    if list_names[i][0] == ' ':
        print(list_names[i])
# op = open("short_long_form.txt", "w", encoding="utf-8")
# print("{}: {}".format(list_names[140], process.extract(list_names[140], list_names)))
# for name1 in list_names:
#     op.write("{}: {}".format(name1, process.extract(name1, list_names)))
