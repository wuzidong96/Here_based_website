#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'
@app.route('/hello/-<float:lng1>,<float:lat1>;-<float:lng2>,<float:lat2>',methods=['GET'])
def hello(lng1,lat1,lng2,lat2):
	return 'User1: %f,%f;%f,%f' %(lng1,lat1,lng2,lat2)
# @app.route('/hello/<float:lng1>,<float:lat1>',methods=['GET'])
# def hello(lng1,lat1):
# 	# print("%f,%f" %lng1 % lat1)
# 	return "%flalala%f" %(lng1,lat1)

if __name__ == '__main__':
	app.run(host='10.6.60.166',port=5000, debug=True, threaded=True)

with app.test_request_context():
	print url_for('hello_world','nub,1')