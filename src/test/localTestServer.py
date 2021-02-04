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
from common.Config import Config

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
    #print(req)
    admin = req['action']['detailParams']['position']['origin']

    print(admin)

    if '관리자 6652' in admin:
        print("Admin Service")
        adminData = {
            "data": {
                "txt":"\n관리자모드 App v" + Config.APP_VERSION,
                "location":"\n " + Config.BLOG,
                "info":"\n관리자가 아니라면 멈춰주세요. \n\n email: " + Config.EMAIL
            }
        }
        return jsonify(adminData)
    
    value = req['action']['detailParams']['position']['value']
    print(value)

    lat, lon = getLocalGeo(value)
    weatherData = getWeatherInfo(lat, lon)
    print(weatherData)
    
    action = req['action']
    print(action)

    testData = {
            "version": "1.0",
            "data": {
                "txt":"새해 복 많이 받으세요~\n",
                "location":"요청하신 ",
                "info":"는 매우 춥겠습니다."
            }
        }

    return jsonify(testData)

if __name__=='__main__':
    app.run(host='0.0.0.0', port = 4005)
    print("Run Server")