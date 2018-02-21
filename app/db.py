import MySQLdb
import time
while(True):
        db = MySQLdb.connect(host='db',user="root",passwd="admin",db="bvs")
        if (db):
                print ("Connection successful")
                exit()
        else:
                print ("Connection unsuccessful")
                time.sleep(30)






# Open database connection
db = MySQLdb.connect(host='db',user="root",passwd="admin",db="bvs")
#db = MySQLdb.connect("127.0.0.1","root","admin","bvs" )

# prepare a cursor object using cursor() method
cursor = db.cursor()



def store(data) :
    r = data
    print (r)
    id = int(r[0])
    name = r[1]
    sql = "insert into regi(id,name) values (%d, '%s')" %(id, name) 
    try:
        cursor.execute(sql)
        db.commit()
        print ("Done Hiiiiiiiii")
    except:
        db.rollback()
        print ("Error: unable to fecth data")
#store(data1)
def ser(id) : 
	i = int(id)
	sql1 = "select * from regi where finger = '%d'" %i 
	#sql1 = "select * from regi where finger = '1'", 
	print ("HI query : ",sql1)
	try:
 	   cursor.execute(sql1)
           results = cursor.fetchall()
	   for row in results:
              id1 = int(row[0])
              name = row[3]
              age = int(row[4])
	      vote = int(row[7])
	      
	   data = {'id':id1, 'name':name, 'age':age, 'status':vote}
	   print (data)
	   if vote == 0:
                # ---------------- Status = 1 bcz of revote avoid ---------------------- #
	    	new_sql = "update regi set status = 1 where finger=%d" %(i)
                cursor.execute(new_sql)
	        db.commit()
	   return(data)
 
        except:
	    db.rollback()
            print ("Error: unable to fecth data")


def display() :
	#sql = "SELECT id,accno,village,name,age,gender FROM regi"
	sql = "SELECT id,accno,village,name,age,gender FROM regi"
	try:
           cursor.execute(sql)
           results = cursor.fetchall()
           rows=[]
           for row in results:
		rows.append(row)
                print(row)
           return(rows)

        except:
            db.rollback()
            print ("Error: unable to fecth data")

def status():
        total = "select count(id) from regi;"
        male = "select count(gender) from regi where gender='male';"
        try:
           t1 = cursor.execute(total)
           data = cursor.fetchone()
           return(data)
        except:
            db.rollback()
            print ("Error: unable to fecth data")

def male():
        male = "select count(gender) from regi where gender='male';"
        try:
           cursor.execute(male)
           data = cursor.fetchone()
           return(data)
        except:
            db.rollback()
            print "Error: unable to fecth data"

def male_status():
        male = "select count(status) from regi where gender='male' and status=1"
        try:
           cursor.execute(male)
           data = cursor.fetchone()
           return(data)
        except:
            db.rollback()
            print ("Error: unable to fecth data")

def female_status():
        male = "select count(status) from regi where gender='female' and status=1"
        try:
           cursor.execute(male)
           data = cursor.fetchone()
           return(data)
        except:
            db.rollback()
            print ("Error: unable to fecth data")

