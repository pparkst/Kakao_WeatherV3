import time

def convertUnixTime(unix_time):
    local_time = time.localtime(int(unix_time))
    nDate = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    return nDate
