import urllib3
from urllib.parse import urlencode
from openpyxl import load_workbook

def Load_Korea_latitude():
    #load_wb = load_workbook("/Korea_latitude&longtitude.xlsx")
    #load_ws = load_wb['Sheet1']
    #print(load_ws['D3'].value)
    #print(load_ws.cells(4,2).value)

    wb = load_workbook('util/Korea_latitude&longtitude.xlsx')
    ws = wb.active

    for r in ws.rows:
        row_index = r[1].row
        top = r[2].value
        mid = r[3].value
        bootom = r[4].value
        full = top+mid+bootom

        if u'서울' in full:
            print(full)
            break

        # print(type(row_index))
        # if len(str(row_index)) > 0:
        #     print(full)
        #     print("row = " + str(row_index))
        # if u'서울' in full:
        #     print("일치")
        #     print(str(row_index)+'@'+full)
    

    str1 = u'서울용두 동  날씨'
    str2 = u'서 울  용두동날씨'
    str3 = u'서울용두동날  씨'
    str4 = u'서울용두동  날씨'
    str5 = u'서울  용두동날씨'
    str6 = u'서울 용두동  날씨'

    strarray = [str1,str2,str3,str4,str5,str6]

    for str in strarray:
        print(str)
        str = str.replace(' ','')
        print(str)
        if '날씨' in str:
            print('있네있어')
        else:
            print("??")

def getLocalGeo():
    http = urllib3.PoolManager()
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    query = '?' + urlencode({'query': '자양2동'})
    url+=query
    print(url)
    r = http.request('GET', url, headers={'Authorization':"KakaoAK "})

    print(r.status)
    print(r.data)

def App():
    # http = urllib3.PoolManager()
    # url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'

    # serviceKey = ''

    # print(urlencode({'serviceKey': serviceKey}))

    # queryParams = '?' + urlencode({'serviceKey': serviceKey, 'pageNo': '1', 'numOfRows': '10', 'dataType': 'JSON', 'dataCd': 'ASOS', 'dateCd': 'HR', 
    #                                 'startDt': '20210130', 'startHh': '01', 'endDt': '20210130', 'endHh': '23', 'stnIds': '108' })
    # url+=queryParams

    # r = http.request('GET', url)

    # print(r.status)
    # print(r.data)


    getLocalGeo()

    #Load_Korea_latitude()

App()