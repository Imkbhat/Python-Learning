from array import array
from __builtin__ import set
print("Hello World")
array = [100,101,102,103,104]
for i in array :
    print i
    
    
def addition(n):
    return n+n

#result = map(addition, numbers)
#print result

l = ['kiran','bhat']
test = list(map(list, l))
print test


def iAmFrom(country = 'India'):
    print("I am from "+country)


iAmFrom('Australia');
iAmFrom()

#####################JDBC Connectivity###########################################
#Need to install psycopg2 in ubuntu
import psycopg2

conn = psycopg2.connect(database = "dbname", user="postgres", password="postgres", host = "127.0.0.1", port = "5432")

print "Opened database successfully"

cur = conn.cursor()
cur.execute('''SET search_path to schema''')
cur.execute('''SELECT * FROM table LIMIT 1''')
rows = cur.fetchall()

for row in rows :
    print "Record : "+row[0]

conn.close()
