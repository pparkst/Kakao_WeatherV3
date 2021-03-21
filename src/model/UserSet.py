import json
import time
import datetime
from App import getLocalGeo
from util.Common import getKtc


def initEntity(request):
    userSet = request['action']
    time = json.loads(userSet['params']['time'])['time']
    time_ = time.split(':')
    ntime = ':'.join(time_[0:2])

    entity = {  'id': request['userRequest']['user']['id'], 
                'location': userSet['params']['location'],
                'time': ntime,
                'work':1,
                'created': getKtc(),
               }

    return entity

def initUnsetEntity(request):
    entity = {
        'id': request['userRequest']['user']['id'], 
    }

    return entity

def initMessageQue(data):
    entity = {  'id': data['id'], 
                'location': data['location'],
                'message' : '',
               }

    return entity
