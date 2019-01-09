

#########################################################################################################################################
# Example of simple local db file/table usage. Advantageous in case of large persistence data requirement                               #
#########################################################################################################################################

"""
sqlite3 - module provides connection to sqlite db and execution sql on target

main functions used in the example script:

sqlite3.connect - os file name as parameter, in case file does not exist, it is created automatically
conn = sqlite3.connect("os_file"). conn == connection object that represents the database. Further used by sqlite3 object methods
conn.close() - closing the interface to DB, similar to file I/O close() method.
cur = conn.cursor() - cursor object with alocated row position. similar to text file I/O cursor.
cur.execute("sql command"). method on cursor object to execute SQL (DDL/DML commands, ie. create table ..., select name from ... etc)
cur.executemany(sql command, data as list of tuples) - allows processing chunks of data as opposed to the above relying on single line operations
cur.commit() - confirmation / saving of the changes - standard SQL command
cur.fetchall() - method for retrieving of cursor object data / alternatively cur.fetchone() to retrieve single line


Sample Database: southwind from  http://www.ntu.edu.sg/home/ehchua/programming/sql/mysql_beginner.html
#------------------------------------------------------------------------------------------------------
Table: products

productID INT |	productCode CHAR(3)	| name VARCHAR(30) | quantity INT |	price DECIMAL(10,2)
1001			PEN						Pen Red				5000			1.23
1002			PEN						Pen Blue			8000			1.25
1003			PEN						Pen Black			2000			1.25
1004			PEC						Pencil 2B			10000			0.48
1005			PEC						Pencil 2H			8000			0.49

Create the below data as "CSV_DB_sample.csv" in your python project directory
productID, productCode, name, quantity, price
1001,PEN,Pen Red,5000,1.23
1002,PEN,Pen Blue,8000,1.25
1003,PEN,Pen Black,2000,1.25
1004,PEC,Pencil 2B,10000,0.48
1005,PEC,Pencil 2H,8000,0.49
"""

import os, sqlite3, timeit, sys

#Variables
db_file_name = "my_test_DB.sqlite"
sql_create_table = "create table sample (productID int, productCode CHAR(3), name VARCHAR(30), quantity INT, price DECIMAL(10,2))"
csv_file = "CSV_DB_sample.csv"
sql_select = "select * from sample"



def db_create(db_file_name):


    sql_tables = "select name from sqlite_master"
    table_exists = db_query(sql_tables)


    if not table_exists:
        db_query(sql_create_table)
    else:
        print("following tables exist:",table_exists)
        print("delete existing tables and start again? Y/N")
        choice = input(">>>: ").lower()
        if choice == "y":
            for i in table_exists:
                sql_drop = """DROP TABLE %s""" % i
                db_query(sql_drop)
                db_query(sql_create_table)




# execute SQL commands passed in "sql_query" variable
def db_query(sql_query):
    conn = sqlite3.connect(db_file_name)
    cur = conn.cursor()
    cur.execute(sql_query)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result

# insert data from csv file to sqlite DB - insertion method row by row
def csv_to_db():
    if not os.path.exists(os.path.realpath(db_file_name)):
        print(db_file_name, "does not exist.. creating as new")
        db_create(db_file_name)
    else:
        db_create(db_file_name)

    with open(csv_file,"r") as csv:
        txt = csv.readlines()
        counter = 0
        for counter in range(len(txt)):
            update_progress("reading csv... inserting into DB",counter/len(txt))

            # skipt the first line in CSV containing column names
            if counter > 0:
                values = txt[counter].strip("\n").split(",")

                insert_query = "insert into sample (productID, productCode, name , quantity, price )  values ( " + \
                                "'" + values[0] + "'" + ", " + \
                                "'" + values[1] + "'" + ", " + \
                                "'" + values[2] + "'" + ", " + \
                                "'" + values[3] + "'" + ", " + \
                                "'" + values[4] + "'" + " )"

                db_query(insert_query)
                counter += 1

#cursor.executemany() function allows faster execution of inserting of chunks of data into a table
def exec_many():
    if not os.path.exists(os.path.realpath(db_file_name)):
        print(db_file_name, "does not exist.. creating as new")
        db_create(db_file_name)
    else:
        db_create(db_file_name)

    with open(csv_file,"r") as csv:
        txt = csv.readlines()
        #make a list of tuples to prepare for executemany function
        data = [tuple(line.strip().split(",")) for line  in txt]

        data.pop(0)
        conn = sqlite3.connect(db_file_name)
        cur = conn.cursor()
        cur.executemany("insert into sample values (?,?,?,?,?)", data)
        #result = cur.fetchall()
        conn.commit()
        conn.close()


def update_progress(job_title, progress):
    length = 20 # modify this to change the length
    block = int(round(length*progress))
    msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
    if progress >= 1: msg += " DONE\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()

exec_many()

#csv_to_db()

csv_t_start = timeit.default_timer()
with open(csv_file, "r") as csv:
    txt = csv.readlines()
    print(*txt,sep = "")
csv_t_stop = timeit.default_timer()



db_t_start = timeit.default_timer()
print(*db_query(sql_select),sep="\n")
db_t_stop = timeit.default_timer()

print()
print("csv file read and print duration",csv_t_stop - csv_t_start)
print("db read and print duration", db_t_stop - db_t_start)






