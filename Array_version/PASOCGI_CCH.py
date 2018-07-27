#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

from flask import Flask, jsonify
from flask import make_response
import os
from flask_cors import CORS
import time
import csv
import polyline

# 提供给 js AJax 调用的 CGI

app = Flask(__name__)
CORS(app)

@app.route('/route/v1/driving/-<float:source_lng>,<float:source_lat>;-<float:destination_lng>,<float:destination_lat>', methods=['GET'])
#@app.route('/route/v1/driving/<float:source_lat>,<float:source_lng>;<float:destination_lat>,<float:destination_lng>?overview=<float:overview>&alternatives=<float:alternatives>&steps=<float:steps>&hints=<float:hints>', methods=['GET'])
def get_tasks(source_lat,source_lng,destination_lat,destination_lng):
    print 'start', time.time()
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
            min_source_id=latlng_list[i][2]
        destination_temp=(latlng_list[i][0]-destination_lat)**2+(latlng_list[i][1]+destination_lng)**2
        if destination_temp<min_destination_distance:
            min_destination_distance=destination_temp
            min_destination_id=latlng_list[i][2]

    os.system('./main '+str(min_source_id)+' '+str(min_destination_id)+' '+str(50))
    os.system('chmod +x *.sh')
    os.system('./get_fastest_shortest_optimal_gra_js.sh '+str(min_source_id)+' '+str(min_destination_id)+' '+str(50))
    file_fastest=open('./trash_fastest')
    file_shortest=open('./trash_shortest')
    file_optimal=open('./trash_optimal')
    list_solution=[]
    with open('./result/T800/info/info_'+str(min_source_id)+'_'+str(min_destination_id)+'_'+str(50)+'.csv','rb') as f:
        reader = csv.reader(f)
        for row in reader:
            for column in row:
                list_solution.append(float(column))

    latlng=[]
    steps=[]
    for line in file_fastest:
        temp=str(line.strip()).split(':')
        temp2=(float(temp[1][0:9]),float(temp[2][0:9]))
        temp_geometry=polyline.encode([temp2])
        latlng.append(temp2)
        intersections=[{'out':0,'entry':'true','location':temp2,'bearings':0}]
        maneuver={'bearing_after':0,'location':temp2,'type':'','modifier':'','bearing_before':0}
        steps.append({'intersections':intersections,'maneuver':maneuver,'distance':0,'duration':0,'geometry':temp_geometry,'mode':'','name':'','weight':0})
    legs=[{'distance':0,'duration':0,'steps':steps,'weight':0,'summary':''}]
    route1={'distance':0,'duration':0,'weight':0,'weight_name':'','coordinates':latlng,'legs':legs}
    
    
    latlng=[]
    steps=[]
    for line in file_shortest:
        temp=str(line.strip()).split(':')
        temp2=(float(temp[1][0:9]),float(temp[2][0:9]))
        temp_geometry=polyline.encode([temp2])
        latlng.append(temp2)
        intersections=[{'out':0,'entry':'true','location':temp2,'bearings':0}]
        maneuver={'bearing_after':0,'location':temp2,'type':'','modifier':'','bearing_before':0}
        steps.append({'intersections':intersections,'maneuver':maneuver,'distance':0,'duration':0,'geometry':temp_geometry,'mode':'','name':'','weight':0})
    legs=[{'distance':0,'duration':0,'steps':steps,'weight':0,'summary':''}]
    route2={'distance':0,'duration':0,'weight':0,'weight_name':'','coordinates':latlng,'legs':legs}

    latlng=[]
    steps=[]
    for line in file_optimal:
        temp=str(line.strip()).split(':')
        temp2=(float(temp[1][0:9]),float(temp[2][0:9]))
        temp_geometry=polyline.encode([temp2])
        latlng.append(temp2)
        intersections=[{'out':0,'entry':'true','location':temp2,'bearings':0}]
        maneuver={'bearing_after':0,'location':temp2,'type':'','modifier':'','bearing_before':0}
        steps.append({'intersections':intersections,'maneuver':maneuver,'distance':0,'duration':0,'geometry':temp_geometry,'mode':'','name':'','weight':0})
    legs=[{'distance':0,'duration':0,'steps':steps,'weight':0,'summary':''}]
    route3={'distance':0,'duration':0,'weight':0,'weight_name':'','coordinates':latlng,'legs':legs}

    waypoint1={'hint':'','location':[source_lat,source_lng],'name':''}
    waypoint2={'hint':'','location':[destination_lat,destination_lng],'name':''}

    result = jsonify({"code":"Ok","routes":[route1,route2,route3],"waypoints":[waypoint1,waypoint2]})

    print 'end', time.time()
    return result

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'This page not found!!'}), 404)

if __name__ == '__main__':
    app.run(host='10.6.60.166',port=5000, debug=True, threaded=True)
	
