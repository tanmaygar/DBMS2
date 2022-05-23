import time
import psycopg2
import psycopg2.extras

start_time = time.time()

paper_id = 0
paper_citation_ids = []
authors_list = []
paper_abstract = ""
paper_title = ""
paper_date = ""
paper_venue = ""
# sql_file = open("insert_statements.sql", "w", encoding="utf-8")
source_file = open("source_clean - Copy.txt", "r", encoding="utf-8")
counter = 0

conn = psycopg2.connect("dbname=dbms_a2 user=postgres password=1234")
cur = conn.cursor()
# while True:
#     line = source_file.readline()
#     if not line:
#         break
#     if line.startswith("#*"):
#         paper_title = line[2:].strip()
#         paper_citation_ids.clear()
#         authors_list.clear()
#         paper_venue = ""
#         paper_abstract = ""
#         paper_date = ""
#     if line.startswith("#t"):
#         paper_date = line[2:].strip()
#     if line.startswith("#c"):
#         paper_venue = line[2:].strip()
#     if line.startswith("#index"):
#         paper_id = int(line[6:].strip())
#     # if line.startswith("#%"):
#     #     paper_citation_id = int(line[2:].strip())
#     #     paper_citation_ids.append(paper_citation_id)
#     # if line.startswith("#@"):
#     #     authors_string = line[2:].strip()
#     #     # authors_list = authors_string.split(",")
#     #     authors_list = [int(author_id) for author_id in authors_string.split(",") if author_id.strip().isdigit()]
#     if line.startswith("#!"):
#         paper_abstract = line[2:].strip()
#     if line == '\n':
#         cur.execute("""
#         INSERT INTO ResearchPaper VALUES (%s, %s, %s, %s, %s);
#         """, (str(paper_id), paper_title, paper_date, paper_venue, paper_abstract))
#         counter = counter + 1
all_papers = []
while True:
    line = source_file.readline()
    if not line:
        break
    if line.startswith("#*"):
        paper_title = line[2:].strip()
        paper_citation_ids.clear()
        authors_list.clear()
        paper_venue = ""
        paper_abstract = ""
        paper_date = ""
    if line.startswith("#t"):
        paper_date = line[2:].strip()
    if line.startswith("#c"):
        paper_venue = line[2:].strip()
    if line.startswith("#index"):
        paper_id = int(line[6:].strip())
    # if line.startswith("#%"):
    #     paper_citation_id = int(line[2:].strip())
    #     paper_citation_ids.append(paper_citation_id)
    # if line.startswith("#@"):
    #     authors_string = line[2:].strip()
    #     # authors_list = authors_string.split(",")
    #     authors_list = [int(author_id) for author_id in authors_string.split(",") if author_id.strip().isdigit()]
    if line.startswith("#!"):
        paper_abstract = line[2:].strip()
    if line == '\n':
        paper_dict = {"ID": paper_id, "title": paper_title, "year": paper_date, "venue": paper_venue,
                      "abstract": paper_abstract}
        all_papers.append(paper_dict)
        counter = counter + 1

# psycopg2.extras.execute_batch(cur, """
#     INSERT INTO ResearchPaper VALUES (
#     %(ID)s,
#     %(title)s,
#     %(year)s,
#     %(venue)s,
#     %(abstract)s
#     );
# """, all_papers)

psycopg2.extras.execute_values(cur, """INSERT INTO ResearchPaper VALUES %s;""",
                               (
                                   (paper_i['ID'], paper_i['title'], paper_i['year'], paper_i['venue'],
                                    paper_i['abstract'])
                                   for paper_i in all_papers), page_size=1000
                               )
conn.commit()
cur.close()
conn.close()
# sql_file.close()
source_file.close()
print(time.time() - start_time)
