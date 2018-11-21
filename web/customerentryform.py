# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:18:58 2018

@author: shirley.ng
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def formpage():
    return render_template('customerform.html')

@app.route("/submit",methods=['POST'])
def submitpage():
    txtValue = request.form['cus_fname']
    print("received:" + txtValue);
    return render_template('customersubmit.html',inputName=txtValue)

if __name__=="__main__":
    app.run()