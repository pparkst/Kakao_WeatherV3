import os
from flask import Flask, jsonify, request
import string
import urllib.request
import urllib.parse
import json
import socket
import sys
from http.cookies import _getdate
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from App import getLocalGeo, getWeatherInfo
from common.ApiKey import ApiKey
from util.Common import AbTemperatureConvertCelsius, convertUnixTime, strWeatherCurrent, strWeather3Day, strToday
import datetime
from model.UserSet import initEntity, initUnsetEntity
from db.conn import conn

app = Flask(__name__)

@app.route('/test')
def Server_Run_Test():
    req = request.args.get('name','empty')
    print(req)

    testData = {
        'txt': 'Hello',
        'name' : req
    }

    return jsonify(testData)


@app.route('/kakaoTest', methods=['GET', 'POST'])
def Server_Weather_Test():
    req = request.get_json()
    print(req)

    testData = {
            "version": "1.0",
            "data": {
                "msg":"HI2",
                "name":"Ryan",
                "position":"Senior Managing Director"
            }
        }

    return jsonify(testData)


@app.route('/kakaoLive', methods=['GET', 'POST'])
def Server_Weather_Live():
    req = request.get_json()
    print(req)
    admin = req['action']['detailParams']['position']['origin']
    
    print(admin)

    if '관리자 6652' in admin:
        print("Admin Service")
        adminData = {
            "data": {
                "txt":"\n관리자모드 App v" + ApiKey.APP_VERSION,
                "location":"\n " + ApiKey.BLOG,
                "info":"\n관리자가 아니라면 멈춰주세요. \n\n email: " + ApiKey.EMAIL
            }
        }
        return jsonify(adminData)
    
    value = req['action']['detailParams']['position']['value']
    #print(value)

    lat, lon = getLocalGeo(value)
    weatherData = getWeatherInfo(lat, lon)
    print(weatherData[0])
    print('***********************************************************************************')
    print(weatherData[1])
    
    action = req['action']
    #print(action)
    str3Days = strWeather3Day(weatherData)

    strCurrent = strWeatherCurrent(weatherData, 0 if len(str3Days) < 4 else 1)

    for test in str3Days:
        print(test)


    testData = {
            "version": "1.0",
            "data": {
                "location": "새해 복 많이 받으세요.\n\n" + "요청하신 지역 : " + value + '\n',
                "txt": strToday() + " 오늘 -",
                "info": strCurrent + '\n' + ''.join(str3Days)
            }
        }

    print(testData)

    return jsonify(testData)

@app.route('/userset', methods=['POST'])
def PutUserSet():
    req = request.get_json()
    print(request.headers)
    print(req)
    
    if(request.headers['P-RequestType'] != ''):
        if(request.headers['P-RequestType'] == 'set'):
            entity = initEntity(req)
            print(entity)
            conn.addData(entity)
            resData = {
                'msg' : '설정되었습니다.',
                'location' : entity['location'],
                'time' : entity['time'],
                'type' : 'PutUserSet'
            }
        elif(request.headers['P-RequestType'] == 'unset'):
            entity = initUnsetEntity(req)
            print(entity)
            conn.disableTalk(entity)
            resData = {
                'msg' : '설정해제되었습니다.',
                'location' : '-',
                'time' : '-',
                'type' : 'PatchUserUnSet'
            }
    else:
        resData = {
            'msg' : "don't match",
            'location' : '-',
            'time' : '-',
            'type' : 'none'
        }

    return jsonify(resData)

@app.route('/userunset', methods=['POST'])
def PatchUserSet():
    req = request.get_json()
    print(req)
    entity = initEntity(req)
    conn.disableTalk(entity)

    resData = {
        'msg' : '설정해제되었습니다.',
        'type' : 'PatchUserSet'
    }

    return jsonify(resData)


@app.route('/userSet', methods=['GET'])
def GetUserSet():
    req = request.get_json()
    print(req)
    time = '07:00:00'
    rows = conn.getData(time)
    return jsonify({ 'msg' : 'GetUserSet!'})

if __name__=='__main__':
    app.run(host='0.0.0.0', port = 4005)
    print("Run Server")