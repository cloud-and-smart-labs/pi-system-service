import json
import time

conf = json.loads(open('/tmp/system-service/conf.json').read())
filename = conf["filename"]

number = 1

while True:
    file = open(f'/tmp/{filename}', 'w')
    file.write(str(number))
    number += 1
    file.close()
    time.sleep(1)
