import asyncio
import websockets
import json
import os

import RPi.GPIO as GPIO

conf = json.loads(
    open('/home/pi/pi-system-service/').read())
PIN = int(conf['pin'])
IP = conf['ip']

URL = 'ws://'+IP+':7890'
STATE = False


async def client():
    try:
        async with websockets.connect(URL) as server:
            info = {}
            info['type'] = 'actuator'
            await server.send(json.dumps(info))

            while True:
                message = await server.recv()
                message = json.loads(message)
                print('Actuation : '+str(message['value']))

                global STATE, PIN

                if STATE:
                    GPIO.output(PIN, GPIO.LOW)
                    STATE = not STATE
                else:
                    GPIO.output(PIN, GPIO.HIGH)
                    STATE = not STATE

    except Exception as e:
        print(str(e))


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
asyncio.run(client())
