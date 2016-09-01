#
from sys import argv
import psycopg2
import csv

# sets argv with filename to be imported
script, load = argv



# Column names for neiss_table
column_names = ['case_id', 'trmt_date', 'psu', 'weight', 'stratum', \
'age', 'sex', 'race', 'race_other', 'diag', 'diag_other', 'body_part', \
'disposition', 'location', 'fmv', 'prod1', 'prod2', 'narr1', 'narr2' ]


#Define connection string
conn_string = "host='localhost' dbname='alex' user='postgres'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cur = conn.cursor()

# creates table it it does not already exsit
cur.execute("""CREATE TABLE IF NOT EXISTS neiss_table
(case_id integer PRIMARY KEY, trmt_date varchar, psu integer, weight decimal,
stratum varchar, age integer, sex integer, race integer, race_other varchar,
diag integer, diag_other varchar, body_part integer, disposition integer,
location integer, fmv integer, prod1 integer, prod2 integer, narr1 varchar,
narr2 varchar)""")


# expression to pass row of csv file to db
passData = """INSERT INTO neiss_table (case_id, trmt_date, psu, weight, stratum,
age, sex, race, race_other, diag, diag_other, body_part, disposition, location,
fmv, prod1, prod2, narr1, narr2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

# Opens tsv file (specified in argv) to be read into database
with open (load,'r') as f:
    reader = csv.reader(f, delimiter='\t')
    reader.next() # skips header row
    for row in reader:
        csvline = row
        for item in range(len(csvline)): #change '' to None
            if csvline[item] == "":
                csvline[item] = None
        print csvline
        cur.execute(passData, csvline)

# commit to database changes
conn.commit()

#close cursor and connection
cur.close()
conn.close()
