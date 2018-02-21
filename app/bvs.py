#!/usr/bin/python
from flask import Flask, render_template,request, url_for
import os
import datetime
#import db
import MySQLdb

app = Flask(__name__)
@app.route("/")
def new_regi():
	return render_template('registration.html')
@app.route('/scan',methods=['POST'])
def scan():
    id= request.form['id']
    name = request.form['name']
    data = {'id' : id, 'name' : name}
    data1 = { 0 : id, 1 : name}
    #db.store(data1)
    db = MySQLdb.connect(host='db',user="root",passwd="admin",db="bvs")
    cursor = db.cursor()
    sql = "insert into regi(id,name) values (%d, '%s')" %(int(id), data1[1])
    cursor.execute(sql)
    db.commit()
    return render_template('registration.html')



if __name__ == "__main__":
     app.run(host="0.0.0.0",port=8080, debug=True)

