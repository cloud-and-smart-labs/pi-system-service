from urllib.request import urlopen
import json
import time


def fetch_update():
    with urlopen('https://raw.githubusercontent.com/cloud-and-smart-labs/pi-system-service/master/demo/conf.json') as url:
        data = json.loads(url.read().decode())
        return data['filename']


filename = fetch_update()
number = 1

while True:
    file = open(f'/tmp/{filename}', 'w')
    file.write(str(number))
    number += 1
    file.close()
    time.sleep(1)
