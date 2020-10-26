""" 
#duplicate table 
create table BI_TMP.TX like BI_TMP.T1
#get the columne name 
select tbname, name, coltype, length, scale from sysibm.syscolumns 
where tbname = 'T1'
order by tbname 
"""
# test db2
import ibm_db
import ibm_db_dbi as dbi
import csv
import os

#file_path = os.path.join('C:\\Users\\nliu\Documents\py', 'test.csv')
file_path = os.path.join('C:\\Users\\nliu\Google Drive\py', 'test4.csv')

# pdconn = ibm_db.connect("DATABASE=DWHPROD;HOSTNAME=PDBIDB04;PORT=50055;PROTOCOL=TCPIP;UID=nliu;PWD=Ytm^pTo7z8F!XZU;", "", "") 

try: 
    conn = ibm_db.connect("DATABASE=DWHDEV;HOSTNAME=DVBIDB03;PORT=50005;PROTOCOL=TCPIP;UID=nliu;PWD=Ytm^pTo7z8F!XZU;", "", "") 
#    pdconn = ibm_db.connect("DATABASE=DWHPROD;HOSTNAME=PDBIDB04;PORT=50055;PROTOCOL=TCPIP;UID=nliu;PWD=Ytm^pTo7z8F!XZU;", "", "") 
except:
    print ("Unable to connect")

stmt = "Select * from BI_TMP.T1"
# pdstmt = "Select * from BI_TMP.T1 "

#print ("Number of affected rows ")
result = ibm_db.exec_immediate(conn, stmt)
#result = ibm_db.exec_immediate(pdconn, stmt)

# if sql_stmt is not None:
sqlrow = ibm_db.fetch_tuple(result)

"""
with open(file_path, 'wb') as csv_file:
    filewriter = csv.writer(csv_file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
"""
"""
with open(file_path, 'w', newline='') as csv_file:
"""
# new file 
with open(file_path, 'wb') as csv_file:
    filewriter = csv.writer(csv_file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
csv_file.close()

# existing empty file
with open(file_path, 'w', newline='') as csv_file:                           
    fieldnames =[
        'name', 
        'dept',
        'month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()                            
    while ( sqlrow ):        
        writer.writerow({fieldnames[0]: sqlrow[0], fieldnames[1]: sqlrow[1], fieldnames[2]: sqlrow[2]})   
        sqlrow = ibm_db.fetch_tuple(result)

csv_file.close()
ibm_db.close(conn)
#ibm_db.close(pdconn)