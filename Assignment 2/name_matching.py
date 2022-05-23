import os
# import re
import html

f = open("utils/authors.tsv", "r", encoding="utf-8")
author_names = []
while True:
    line = f.readline()
    author = line.split('\t')

f.close()
