# test db2
import ibm_db
import ibm_db_dbi as dbi

# pdconn = ibm_db.connect("DATABASE=DWHPROD;HOSTNAME=PDBIDB04;PORT=50055;PROTOCOL=TCPIP;UID=nliu;PWD=Ytm^pTo7z8F!XZU;", "", "") 
try: 
    conn = ibm_db.connect("DATABASE=DWHDEV;HOSTNAME=DVBIDB03;PORT=50005;PROTOCOL=TCPIP;UID=nliu;PWD=Ytm^pTo7z8F!XZU;", "", "") 
#    pdconn = ibm_db.connect("DATABASE=DWHPROD;HOSTNAME=PDBIDB04;PORT=50055;PROTOCOL=TCPIP;UID=nliu;PWD=Ytm^pTo7z8F!XZU;", "", "") 
except:
    print ("Unable to connect")

stmt = "Select * from BI_TMP.T1"
# pdstmt = "Select * from BI_TMP.GL_BU_DIM "

print ("Number of affected rows ")
result = ibm_db.exec_immediate(conn, stmt)
#result = ibm_db.exec_immediate(pdconn, stmt)

# if sql_stmt is not None:
row = ibm_db.fetch_tuple(result)

while ( row ):
    for i in row:
        print(i)

    row = ibm_db.fetch_tuple(result)
ibm_db.close(conn)
#ibm_db.close(pdconn)