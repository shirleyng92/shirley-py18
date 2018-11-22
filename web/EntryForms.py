# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:57:12 2018

@author: shirley.ng
"""

from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
import logging
from logging.handlers import RotatingFileHandler

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Shir0725'
app.config['MYSQL_DATABASE_DB'] = 'company'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/entryform')
def showCustomerForm():
    return render_template('customerform.html')


@app.route('/submit',methods=['POST','GET'])
def submit():
    try:
        _cus_code = request.form['cus_code']
        _cus_lname = request.form['cus_lname']
        _cus_fname = request.form['cus_fname']
        _cus_initial = request.form['cus_initial']
        _cus_areacode = request.form['cus_areacode']
        _cus_phone = request.form['cus_phone']
        _cus_balance = request.form['cus_balance']


        # validate the received values
        if _cus_code and _cus_lname and _cus_fname and _cus_initial and _cus_areacode and _cus_phone and _cus_balance:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            sqlQuery = "insert into customer values(" + _cus_code + ",'" + _cus_lname + "','" + _cus_fname + "','" + _cus_initial + "','" + _cus_areacode + "','" + _cus_phone + "','" + _cus_balance + "')"

            print("SQL Query:",sqlQuery)
            app.logger.warning("SQL Query:"+str(sqlQuery))

            cursor.execute(sqlQuery)
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully ! </p> <a href=http://127.0.0.1:725/> Back to Home </a></p>'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        app.logger.error('An error occurred' + str(e))
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

if __name__ == "__main__":
    handler = RotatingFileHandler('apperror.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run(port=725)
