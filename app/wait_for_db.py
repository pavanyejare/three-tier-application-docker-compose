#!/usr/bin/python
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

