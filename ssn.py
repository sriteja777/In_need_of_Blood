import pymysql

def connection():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           passwd="Sriteja@27",
                           db="COMPANY",
                           use_unicode=True,
                           charset="utf8")
    c = conn.cursor()
    return c, conn


c,conn = connection()
ssn = input()
while True:
    x = c.execute("select e1.Super_ssn from EMPLOYEE e1, EMPLOYEE e2 where e1.Super_ssn  = e2.Ssn and e1.Ssn = '{0}'".format(ssn))
    if not int(x) > 0:
        break
    else:
        temp = c.fetchall()
        ssn = temp[0][0]
        print(ssn)

