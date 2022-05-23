# import hmni
# matcher = hmni.Matcher(model='latin')
#
# matcher.similarity("Ankur Bhargava", "A. Bhargava")

from thefuzz import process
from thefuzz import fuzz

print(fuzz.ratio("Ankur Bhargava", "Aryan Bhargava"))
op = open("names_2.txt", "r", encoding="utf-8")
names_list = []
while True:
    line = op.readline()
    if not line:
        break
    line = line.rstrip()
    names_list.append(line)
print(names_list)
for name1 in names_list:
    for name2 in names_list:
        print("{}, {} %: {}".format(name1, name2, fuzz.ratio(name1, name2)))
