# test db2
import ibm_db
import ibm_db_dbi as dbi
import csv
import os

file_path = os.path.join('C:\\Users\\nliu\Documents\py', 'bday.csv')

# pdconn = ibm_db.connect("DATABASE=DWHPROD;HOSTNAME=PDBIDB04;PORT=50055;PROTOCOL=TCPIP;UID=nliu;PWD=Ytm^pTo7z8F!XZU;", "", "") 
try: 
    conn = ibm_db.connect("DATABASE=DWHDEV;HOSTNAME=DVBIDB03;PORT=50005;PROTOCOL=TCPIP;UID=nliu;PWD=Ytm^pTo7z8F!XZU;", "", "") 
except:
    print ("Unable to connect")

#create table BI_TMP.T3 like BI_TMP.T1
#stmt = "CREATE TABLE BI_TMP.T1(name VARCHAR(20) NOT NULL, dept VARCHAR(20), month VARCHAR(20), primary KEY(name))"
# pdstmt = "Select * from BI_TMP.T1"
# print ("Number of affected rows")
#result = ibm_db.exec_immediate(conn, stmt)

sql = "Insert Into BI_TMP.T3(name, dept, month) values(?,?,?)"
insertstmt = ibm_db.prepare(conn, sql)

#sti='john'
#stn='IT'
#sts= 'Jan'
#param =sti, stn, sts

#ibm_db.execute(insertstmt, param)
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            param = row[0], row[1], row[2]
            ibm_db.execute(insertstmt, param)
            line_count += 1
    print(f'Processed {line_count} lines.')

csv_file.close()
ibm_db.close(conn)


