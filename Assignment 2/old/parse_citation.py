import time

start_time = time.time()
f = open("source.txt", "r", encoding="utf-8")

paper_index = 0
main_list_cit = []
tmp_list_cit = []
while True:
    line = f.readline()
    if not line:
        break
    if line[0] == '#' and line[1] == 'i':
        # dum = [int(word) for word in line.split() if word.isdigit()]
        paper_ind = [int(word) for word in line[6:].split() if word.isdigit()]
        paper_index = paper_ind[0]
        main_list_cit.append(tmp_list_cit)
        tmp_list_cit = []
    if line[0] == '#' and line[1] == '%':
        citation_lst = [int(word) for word in line[2:].split() if word.isdigit()]
        citation_id = citation_lst[0]
        tmp_list_cit.append(citation_id)




