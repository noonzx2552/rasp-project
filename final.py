from gpiozero import LED
from gpiozero import Button
import time
import requests

def send_line_notify(message, token):
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + "6hrQvIiWDsoKoUYwa07F5XsRYVqyIMD7SMDhn0cqCsX"}
    data = {"message": message}
    requests.post(line_notify_api, headers=headers, data=data)

line_notify_token = "6hrQvIiWDsoKoUYwa07F5XsRYVqyIMD7SMDhn0cqCsX"

pump = LED(17)
sensor = Button(4)
while True:
    if sensor.is_pressed: 
        print("none runpump")
        messagehigh = f"highsoil!"
        send_line_notify(messagehigh, line_notify_token)
    else:
        message = f"lowsoil!"
        send_line_notify(message, line_notify_token)
        print("runpump")
        messagerun = "pumprun!"
        send_line_notify(messagerun, line_notify_token)
        pump.on()
        time.sleep(2)
        for i in range(1,3):
            print(i)
            time.sleep(1)
        pump.off()
        messagestop = "pumpstop!"
        send_line_notify(messagestop, line_notify_token)
    time.sleep(60)