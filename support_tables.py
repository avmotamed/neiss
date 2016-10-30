 #
from sys import argv
import util_pg

# sets argv with filename to be imported (load_file) and pg table name
script, load_file, table_name = argv

""" All Neiss support tables are two columns, the ID and the description
    ID is integer PRIMARY KEY
    Description is varchar - a string"""

table_headers = util_pg.header_names(load_file)

table_check_string = util_pg.table_string(table_name, table_headers)

pass_string = util_pg.pass_string(table_name, table_headers)

util_pg.write_tables(load_file, table_check_string, pass_string)
