import time
import datetime

def strToday():
    today = datetime.date.today()
    m = today.strftime('%m')
    d = today.strftime('%d')

    if m[0] == '0':
        m = m[1:]
    if d[0] == '0':
        d = d[1:]
    return ('%s월 %s일' % (m,d))

def convertUnixTime(unix_time):
    local_time = time.localtime(int(unix_time))
    m = time.strftime('%m', local_time)
    d = time.strftime('%d', local_time)

    if m[0] == '0':
        m = m[1:]
    if d[0] == '0':
        d = d[1:]
    return ('%s월 %s일' % (m,d))

def AbTemperatureConvertCelsius(Absolute):
    return str(round(Absolute - 273.15))

def strWeatherCurrent(weatherData, flag):
    current = {
        'temp': AbTemperatureConvertCelsius(weatherData[0]['temp']) + '°',
        'weather': weatherData[0]['weather'][0]['description'].replace('온','')  if len(weatherData[0]['weather']) > 0 else ''
    }

    if flag == 0:
        strCurrent = "   현재기온 : " + current['temp'] + '\n   ' + ('대기상태 : ' + current['weather']) if current['weather'] != '' else ''
    else:
        strCurrent = "   현재기온 : " + current['temp']

    return strCurrent
def strDressCode(night):
    night = int(night)
    dress = ''
    if night <0:
        dress = '패딩, 장갑, 목도리'
    elif night < 6:
        dress = '패딩'
    elif night < 10:
        dress = '코트, 야상, 가죽자켓'
    elif night < 12:
        dress = '트렌치 코트, 야상, 두꺼운 맨투맨, 후드티'
    elif night < 17:
        dress = '자켓, 블레이져, 가디건, 셔츠'
    elif night < 20:
        dress = '니트, 가디건, 적당한 맨투맨, 후드티'
    elif night < 23:
        dress = '롱 슬리브, 가디건, 후드티'
    elif night < 27:
        dress = '반팔, 얇은 셔츠, 긴팔'
    else:
        dress = '반팔, 나시티, 원피스'
    return dress
    


    
            

def strWeather3Day(weatherData):
    dt_0 = {
        'key' : 0,
        'date' : convertUnixTime(weatherData[1][0]['dt']),
        'morn': AbTemperatureConvertCelsius(weatherData[1][0]['temp']['morn']) + '°',
        'day' : AbTemperatureConvertCelsius(weatherData[1][0]['temp']['day']) + '°',
        'night':AbTemperatureConvertCelsius(weatherData[1][0]['temp']['night']) + '°',
        'weather': weatherData[1][0]['weather'][0]['description'].replace('온','')  if len(weatherData[1][0]['weather']) > 0 else '',
        'dress' : strDressCode(AbTemperatureConvertCelsius(weatherData[1][0]['temp']['night']))
    }

    dt_1 = {
        'key' : 1,
        'date' : convertUnixTime(weatherData[1][1]['dt']),
        'morn': AbTemperatureConvertCelsius(weatherData[1][1]['temp']['morn']) + '°',
        'day' : AbTemperatureConvertCelsius(weatherData[1][1]['temp']['day']) + '°',
        'night':AbTemperatureConvertCelsius(weatherData[1][1]['temp']['night']) + '°',
        'weather': weatherData[1][1]['weather'][0]['description'].replace('온','')  if len(weatherData[1][1]['weather']) > 0 else '',
        'dress' : strDressCode(AbTemperatureConvertCelsius(weatherData[1][0]['temp']['night']))
    }

    dt_2 = {
        'key' : 2,
        'date' : convertUnixTime(weatherData[1][2]['dt']),
        'morn': AbTemperatureConvertCelsius(weatherData[1][2]['temp']['morn']) + '°',
        'day' : AbTemperatureConvertCelsius(weatherData[1][2]['temp']['day']) + '°',
        'night':AbTemperatureConvertCelsius(weatherData[1][2]['temp']['night']) + '°',
        'weather': weatherData[1][2]['weather'][0]['description'].replace('온','')  if len(weatherData[1][2]['weather']) > 0 else '',
        'dress' : strDressCode(AbTemperatureConvertCelsius(weatherData[1][0]['temp']['night']))
    }

    dt_3 = {
        'key' : 3,
        'date' : convertUnixTime(weatherData[1][3]['dt']),
        'morn': AbTemperatureConvertCelsius(weatherData[1][3]['temp']['morn']) + '°',
        'day' : AbTemperatureConvertCelsius(weatherData[1][3]['temp']['day']) + '°',
        'night':AbTemperatureConvertCelsius(weatherData[1][3]['temp']['night']) + '°',
        'weather': weatherData[1][3]['weather'][0]['description'].replace('온','')  if len(weatherData[1][3]['weather']) > 0 else '',
        'dress' : strDressCode(AbTemperatureConvertCelsius(weatherData[1][0]['temp']['night']))
    }

    threeDays = []
    now_H = int(datetime.datetime.now().strftime('%H'))

    for dt in ([dt_0, dt_1, dt_2, dt_3]):
        strDt = ''
        if dt['key'] == 0:
            if now_H < 17:
                if now_H < 9:
                    strDt = '   오전 : ' + dt['morn'] + '\n   ' + '오후 : ' + dt['day'] + '\n   ' + '저녁 : ' + dt['night'] + '\n   ' + '대기상태 : ' + dt['weather'] + '\n   ' + '옷 : ' + dt['dress'] + '\n'
                elif now_H < 12 :
                    strDt = '   오후 : ' + dt['day'] + '\n   ' + '저녁 : ' + dt['night'] + '\n   ' + '대기상태 : ' + dt['weather'] + '\n   ' + '옷 : ' + dt['dress'] + '\n'
                elif now_H < 17 :
                    strDt = '   저녁 : ' + dt['night'] + '\n   ' + '대기상태 : ' + dt['weather'] + '\n   ' + '옷차림 : ' + dt['dress'] + '\n'
        else:
            strDt =  '\n' + dt['date'] + ' - \n   ' + '오전 : ' + dt['morn'] + '\n   ' + '오후 : ' + dt['day'] + '\n   ' + '저녁 : ' + dt['night'] + '\n   ' + '대기상태 : ' + dt['weather'] + '\n   ' + '옷 : ' + dt['dress'] + '\n'
        threeDays.append(strDt)
    
    return threeDays