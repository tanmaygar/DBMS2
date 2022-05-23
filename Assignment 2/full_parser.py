import time

start_time = time.time()

paper_id = 0
paper_citation_ids = []
authors_list = []
paper_abstract = ""
paper_title = ""
paper_date = ""
paper_venue = ""
sql_file = open("insert_statements.sql", "w", encoding="utf-8")
source_file = open("source_clean - Copy.txt", "r", encoding="utf-8")

while True:
    line = source_file.readline()
    if not line:
        break
    if line.startswith("#*"):
        paper_title = line[2:].strip()
        paper_citation_ids.clear()
        authors_list.clear()
    if line.startswith("#t"):
        paper_date = line[2:].strip()
    if line.startswith("#c"):
        paper_venue = line[2:].strip()
    if line.startswith("#index"):
        paper_id = int(line[6:].strip())
    if line.startswith("#%"):
        paper_citation_id = int(line[2:].strip())
        paper_citation_ids.append(paper_citation_id)
    if line.startswith("#@"):
        authors_string = line[2:].strip()
        # authors_list = authors_string.split(",")
        authors_list = [int(author_id) for author_id in authors_string.split(",") if author_id.strip().isdigit()]
    if line.startswith("#!"):
        paper_abstract = line[2:].strip()
    if line == '\n':
        # if paper_date == "":
        #     paper_date = "NULL"
        # if paper_venue == "":
        #     paper_venue = "NULL"
        # if paper_abstract == "":
        #     paper_abstract = "NULL"
        paper_title = paper_title.replace(r"'", r"''")
        paper_abstract = paper_abstract.replace(r"'", r"''")
        paper_venue = paper_venue.replace(r"'", r"''")
        sql_file.write(
            "INSERT INTO ResearchPaper VALUES ({}, \'{}\', \'{}\', \'{}\', \'{}\');\n".format(paper_id, paper_title,
                                                                                              paper_date,
                                                                                              paper_venue,
                                                                                              paper_abstract))
        # for i in range(len(paper_citation_ids)):
        #     sql_file.write("INSERT INTO paper_citation VALUES ({}, {});\n".format(paper_id, paper_citation_ids[i]))
        # for i in range(len(authors_list)):
        #     sql_file.write("INSERT INTO paper_author VALUES ({}, {}, {});\n".format(paper_id, authors_list[i], i + 1))

sql_file.close()
source_file.close()

print(time.time() - start_time)
