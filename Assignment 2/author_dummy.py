ptr = open("insert_author_id.sql", "w", encoding="utf-8")

for i in range(600000):
    ptr.write("INSERT INTO author VALUES ({}, \'{}\');\n".format(i, "author_" + str(i)))

ptr.close()
