#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

from flask import Flask, jsonify, render_template, request
from flask import make_response
import os
from flask_cors import CORS
import time
import csv
import polyline

# 提供给 js AJax 调用的 CGI

app = Flask(__name__)
CORS(app)

# @app.route('/route/v1/driving/-<float:source_lng>,<float:source_lat>;-<float:destination_lng>,<float:destination_lat>', methods=['GET'])
@app.route('/',methods=['GET'])
def put():
    return render_template('index.html')

# @app.route('/route',methods=['GET','POST'])
# def route():
#     source_lng = -float(request.form['source_lng1'])
#     source_lat = float(request.form['source_lat1'])
#     destination_lng = -float(request.form['des_lng2'])
#     destination_lat = float(request.form['des_lat2'])
#     time_con = int(request.form['time'])
#     print('Time: %d; Coord1:%f,%f; Coord2: %f,%f') %(time_con, source_lat, source_lng, destination_lat,destination_lng)  
#     print 'start', time.time()
#     count=0
#     latlng_list=[]
#     with open('./data/node_info_span_5.txt') as f:
#         for line in f:
#             if count<2:     #the first 2 lines are not coordinates
#                 count+=1
#                 continue
#             else:
#                 count+=1
#                 temp=line.strip().split(',')
#                 temp_latlng=[float(temp[1]),float(temp[2]),int(temp[0])]
#                 latlng_list.append(temp_latlng)
#     min_source_id=-1
#     min_source_distance=1000000
#     min_destination_id=-1
#     min_destination_distance=1000000
#     for i in range(count-2):
#         source_temp=(latlng_list[i][0]-source_lat)**2+(latlng_list[i][1]+source_lng)**2     #the received source_lng is the absolute value
#         if source_temp<min_source_distance:
#             min_source_distance=source_temp
#             min_source_id=latlng_list[i][2]
#         destination_temp=(latlng_list[i][0]-destination_lat)**2+(latlng_list[i][1]+destination_lng)**2
#         if destination_temp<min_destination_distance:
#             min_destination_distance=destination_temp
#             min_destination_id=latlng_list[i][2]

#     os.system('./main '+str(min_source_id)+' '+str(min_destination_id)+' '+str(time_con))
#     os.system('chmod +x *.sh')
#     os.system('./get_fastest_shortest_optimal_gra_js.sh '+str(min_source_id)+' '+str(min_destination_id)+' '+str(time_con))
#     file_fastest=open('./trash_fastest')
#     file_shortest=open('./trash_shortest')
#     file_optimal=open('./trash_optimal')
#     list_solution=[]
#     with open('./result/T800/info/info_'+str(min_source_id)+'_'+str(min_destination_id)+'_'+str(time_con)+'.csv','rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             for column in row:
#                 list_solution.append(float(column))

#     latlng=[]
#     steps=[]
#     for line in file_fastest:
#         temp=str(line.strip()).split(':')
#         temp2=(float(temp[1][0:9]),float(temp[2][0:9]))
#         temp_geometry=polyline.encode([temp2])
#         latlng.append(temp2)
#         intersections=[{'out':0,'entry':'true','location':temp2,'bearings':0}]
#         maneuver={'bearing_after':0,'location':temp2,'type':'','modifier':'','bearing_before':0}
#         steps.append({'intersections':intersections,'maneuver':maneuver,'distance':0,'duration':0,'geometry':temp_geometry,'mode':'','name':'','weight':0})
#     legs=[{'distance':0,'duration':0,'steps':steps,'weight':0,'summary':''}]
#     route1={'distance':0,'duration':0,'weight':0,'weight_name':'','coordinates':latlng,'legs':legs}
    
    
#     latlng=[]
#     steps=[]
#     for line in file_shortest:
#         temp=str(line.strip()).split(':')
#         temp2=(float(temp[1][0:9]),float(temp[2][0:9]))
#         temp_geometry=polyline.encode([temp2])
#         latlng.append(temp2)
#         intersections=[{'out':0,'entry':'true','location':temp2,'bearings':0}]
#         maneuver={'bearing_after':0,'location':temp2,'type':'','modifier':'','bearing_before':0}
#         steps.append({'intersections':intersections,'maneuver':maneuver,'distance':0,'duration':0,'geometry':temp_geometry,'mode':'','name':'','weight':0})
#     legs=[{'distance':0,'duration':0,'steps':steps,'weight':0,'summary':''}]
#     route2={'distance':0,'duration':0,'weight':0,'weight_name':'','coordinates':latlng,'legs':legs}

#     latlng=[]
#     steps=[]
#     for line in file_optimal:
#         temp=str(line.strip()).split(':')
#         temp2=(float(temp[1][0:9]),float(temp[2][0:9]))
#         temp_geometry=polyline.encode([temp2])
#         latlng.append(temp2)
#         intersections=[{'out':0,'entry':'true','location':temp2,'bearings':0}]
#         maneuver={'bearing_after':0,'location':temp2,'type':'','modifier':'','bearing_before':0}
#         steps.append({'intersections':intersections,'maneuver':maneuver,'distance':0,'duration':0,'geometry':temp_geometry,'mode':'','name':'','weight':0})
#     legs=[{'distance':0,'duration':0,'steps':steps,'weight':0,'summary':''}]
#     route3={'distance':0,'duration':0,'weight':0,'weight_name':'','coordinates':latlng,'legs':legs}

#     waypoint1={'hint':'','location':[source_lat,source_lng],'name':''}
#     waypoint2={'hint':'','location':[destination_lat,destination_lng],'name':''}

#     result = jsonify({"code":"Ok","routes":[route1,route2,route3],"waypoints":[waypoint1,waypoint2]})

#     print 'end', time.time()
#     return result

#array version
@app.route('/route',methods=['GET','POST'])
def route():
    source_lng = -float(request.form['source_lng1'])
    source_lat = float(request.form['source_lat1'])
    destination_lng = -float(request.form['des_lng2'])
    destination_lat = float(request.form['des_lat2'])
    time_con = int(request.form['time'])
    print('Time: %d; Coord1:%f,%f; Coord2: %f,%f') %(time_con, source_lat, source_lng, destination_lat,destination_lng)  
    print 'CGI begin', time.time()
    count=0
    latlng_list=[]
    with open('./data/node_info_span_5.txt') as f:
        for line in f:
            if count<2:     #the first 2 lines are not coordinates
                count+=1
                continue
            else:
                count+=1
                temp=line.strip().split(',')
                temp_latlng=[float(temp[1]),float(temp[2]),int(temp[0])]
                latlng_list.append(temp_latlng)
    min_source_id=-1
    min_source_distance=1000000
    min_destination_id=-1
    min_destination_distance=1000000
    for i in range(count-2):
        source_temp=(latlng_list[i][0]-source_lat)**2+(latlng_list[i][1]+source_lng)**2     #the received source_lng is the absolute value
        if source_temp<min_source_distance:
            min_source_distance=source_temp
            min_source_row = i
        destination_temp=(latlng_list[i][0]-destination_lat)**2+(latlng_list[i][1]+destination_lng)**2
        if destination_temp<min_destination_distance:
            min_destination_distance=destination_temp
            min_destination_row = i
    min_source_id=latlng_list[min_source_row][2]
    source_lat_disp = latlng_list[min_source_row][0]
    source_lng_disp = latlng_list[min_source_row][1]
    min_destination_id=latlng_list[min_destination_row][2]
    destination_lat_disp = latlng_list[min_destination_row][0]
    destination_lng_disp = latlng_list[min_destination_row][1]


    os.system('./main '+str(min_source_id)+' '+str(min_destination_id)+' '+str(time_con))
    os.system('chmod +x *.sh')
    os.system('./get_fastest_shortest_optimal_gra_js.sh '+str(min_source_id)+' '+str(min_destination_id)+' '+str(time_con))
    file_fastest=open('./trash_fastest')
    file_shortest=open('./trash_shortest')
    file_optimal=open('./trash_optimal')
    list_solution=[]
    with open('./result/T800/info/info_'+str(min_source_id)+'_'+str(min_destination_id)+'_'+str(time_con)+'.csv','rb') as f:
        reader = csv.reader(f)
        for row in reader:
            for column in row:
                list_solution.append(float(column))

    lat_fast = []
    lng_fast = []
    for line in file_fastest:
        temp=str(line.strip()).split(':')
        lat_fast.append(float(temp[1][0:9]))
        lng_fast.append(float(temp[2][0:9]))
    
    
    lat_short=[]
    lng_short=[]
    for line in file_shortest:
        temp=str(line.strip()).split(':')
        lat_short.append(float(temp[1][0:9]))
        lng_short.append(float(temp[2][0:9]))

    lat_optimal=[]
    lng_optimal=[]
    for line in file_optimal:
        temp=str(line.strip()).split(':')
        lat_optimal.append(float(temp[1][0:9]))
        lng_optimal.append(float(temp[2][0:9]))

    waypoint1=[source_lat_disp,source_lng_disp]
    waypoint2=[destination_lat_disp,destination_lng_disp]

    print 'CGI end', time.time()
    # return render_template('display.html',route_fast=route1,route_short=route2,route_optimal=route3)
    return render_template('display.html',lat_fast=lat_fast,lng_fast=lng_fast,lat_short=lat_short,lng_short=lng_short,lat_optimal=lat_optimal,
    	lng_optimal=lng_optimal,waypoint1=waypoint1,waypoint2=waypoint2)

#test for return data as a list
# @app.route('/route',methods=['GET','POST'])
# def route():
# 	lat_f1=[]
# 	lng_f1=[]
# 	lat_f1.append(1.1)
# 	lat_f1.append(2.1)
# 	lat_f1.append(3.1)
# 	lng_f1.append(4.1)
# 	lng_f1.append(5.1)
# 	lng_f1.append(6.1)
	# # route1=jsonify({'coordinates':latlng})
	# # route1 = latlng
	# # return route1
# 	return render_template('display.html',lat_fast=lat_f1,lng_fast=lng_f1)
# latlng=[]
# steps=[]
# for line in file_shortest:
#     temp=str(line.strip()).split(':')
#     temp2=(float(temp[1][0:9]),float(temp[2][0:9]))
#     latlng.append(temp2)
# route2={'coord':latlng}

# latlng=[]
# steps=[]
# for line in file_optimal:
#     temp=str(line.strip()).split(':')
#     temp2=(float(temp[1][0:9]),float(temp[2][0:9]))
#     latlng.append(temp2)
# route3={'coord':latlng}

# waypoint1={'location':[source_lat,source_lng]}
# waypoint2={'location':[destination_lat,destination_lng]}

# print 'CGI end', time.time()
# # return render_template('display.html',route_fast=route1,route_short=route2,route_optimal=route3)
# return render_template('display.html',route_fast=route1)



@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'This page not found!!'}), 404)

if __name__ == '__main__':
    app.run(host='10.6.60.187',port=5000, debug=True, threaded=True)
	
