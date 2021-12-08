import Adafruit_DHT
from urllib.request import urlopen
import json
import os
from time import sleep


conf = json.loads(
    open('/home/'+os.environ['USER']+'/pi-system-service/').read())
sensor = Adafruit_DHT.DHT11
gpio = int(conf['pin'])
ip = conf['ip']


while True:
    try:
        sleep(2)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
        # print(humidity, temperature)

        # http://192.168.0.103/sensor/1.0
        URL = 'http://'+ip+':80/sensor/'+str(temperature)

        with urlopen(URL) as url:
            data = json.loads(url.read().decode())
            # print(data)
    except Exception as e:
        # print(str(e))
        pass
