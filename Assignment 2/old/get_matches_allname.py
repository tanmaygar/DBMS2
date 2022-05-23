import html
import time
from thefuzz import process
from thefuzz import fuzz
from html.parser import HTMLParser
from html.entities import name2codepoint
from pylatexenc.latex2text import LatexNodes2Text
import sys


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)


def raw_string_c_(og_name):
    modified_name = og_name
    modified_name = modified_name.replace('\W', 'W')
    # modified_name = modified_name.replace("\''a", "\\\'a")
    modified_name = modified_name.replace("\a", "\\a")
    modified_name = modified_name.replace("\v", "\\v")
    modified_name = modified_name.replace("\b", "\\b")
    modified_name = modified_name.replace("\"", '\\"')
    modified_name = modified_name.replace("\''", '\\\'')
    return modified_name


parser = MyHTMLParser()


def name_corrector(og_name):
    name_modified1 = og_name
    name_modified2 = raw_string_c_(og_name)
    name_modified1 = name_modified1.lower()
    name_modified1 = html.unescape(name_modified1)
    name_modified2 = LatexNodes2Text().latex_to_text(name_modified2)
    if len(name_modified1) == len(name_modified2):
        final_name = og_name
    elif len(name_modified1) > len(name_modified2):
        final_name = name_modified2
    else:
        final_name = name_modified1
    return final_name


start_time = time.time()
f = open("source.txt", "r", encoding="utf-8")
op = open("names_all.txt", "w", encoding="utf-8")
# op2 = open("names_line.txt", "w", encoding="utf-8")
list_names = []
count = 0
while True:
    line = f.readline()
    count = count + 1
    if not line:
        break
    if line[0] == '#' and line[1] == '@':
        x = line[2:].split(',')
        for i in range(len(x)):
            new_name = x[i].rstrip()
            if len(new_name) >= 1:
                if new_name[0] == " ":
                    new_name = new_name[1:]
            # op2.write("{}: {}\n".format(count, new_name))
            # print("{}: {}\n".format(count, new_name))
            modi_name = name_corrector(new_name)
            list_names.append(modi_name)

print(len(list_names))
print(len(set(list_names)))

set_names = set(list_names)
list_names = list(set_names)
list_names.sort()
for i in range(len(list_names)):
    op.write((list_names[i] + '\n'))
op.close()
f.close()
print(time.time() - start_time)
list_names.pop(0)

# str_tmp = "&#x00c0;lex M&#x00e9;ndez-Feliu"
# h = HTMLParser()
# print(html.unescape(str_tmp))

# parser = MyHTMLParser()
# name = "marusi&cbreve;"
# # name = raw_string_c_(name)
# name = name_corrector(name)
# # name = name.replace("\''", '\\\'')
# # name = r"" + name
# print(LatexNodes2Text().latex_to_text(name))
# names_list = ["Csaba Szepesvari", "Csaba Szepesva\''ri", r"marusi&cbreve;"]
# print(type(names_list[0]))
# print(type(names_list[2]))
# print(LatexNodes2Text().latex_to_text(names_list[2]))
# string_tmp = LatexNodes2Text().latex_to_text(names_list[2])
# parser.feed(names_list[2])
#
#
# tmp_tmp = sys.stdout
# sys.stdout = open("tmp.txt", "w", encoding="utf-8")
# parser.feed(names_list[2])
# sys.stdout.close()
# sys.stdout = tmp_tmp
# print("hello")
# f = open("tmp.txt", "r", encoding="utf-8")
# new_name = f.readline()
# new_name = new_name[11:]
# print(new_name)
# parser.feed("&cbreve")
# for name1 in names_list:
#     for name2 in names_list:
#         print("{}, {} %: {}".format(name1, name2, fuzz.ratio(name1, name2)))

# print(html.unescape(names_list[2]).encode('latin1').decode('utf8'))
