# Utility function for Postgres

import csv
import psycopg2

def header_names(stuff):
    """ Create Table Header for Postgres from 1st line of CSV file """

    # Opens csv file (load_file) to crete list of table headers for postgres
    # CSV file should be exported as MS DOS Comma Seperated
    with open (stuff,'rU') as f:
        reader = csv.reader(f, delimiter=',',  dialect=csv.excel_tab)
        headers = reader.next()
        return headers

def table_string(table_name, table_headers):
    string = "CREATE TABLE IF NOT EXISTS " + table_name
    string += "(" + table_headers[0] + " integer PRIMARY KEY, "
    string += table_headers[1] + " varchar)"
    return string

def pass_string(table_name, table_headers):
    string2 = "INSERT INTO " + table_name
    string2 += " (" + table_headers[0] + ", " + table_headers[1] + ")"
    string2 += " VALUES (%s, %s);"
    return string2

def write_tables(load, table_s, pass_s):
    #Define connection string
    conn_string = "host='localhost' dbname='alex' user='postgres'"

    # print the connection string we will use to connect
    print "Connecting to database\n	->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cur = conn.cursor()

    # creates table it it does not already exsit
    cur.execute(table_s)

    # Opens tsv file (specified in argv) to be read into database
    with open (load,'rU') as f:
        """for reading from csv, \t is the tab delimiter, csv.QUOTE_NONE treats as
        a quote character and not any type of delimeter """
        reader = csv.reader(f, delimiter=',',  dialect=csv.excel_tab)
        reader.next() # skips header row
        for row in reader:
            csvline = row
            for item in range(len(csvline)): #change '' to None
                if csvline[item] == "":
                    csvline[item] = None
            print csvline
            cur.execute(pass_s, csvline)

    # commit to database changes
    conn.commit()

    #close cursor and connection
    cur.close()
    conn.close()
