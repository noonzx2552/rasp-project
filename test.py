import requests
import time
from gpiozero import MCP3008

def read_soil_moisture():
    soil_sensor = MCP3008(channel=0)
    moisture_value = soil_sensor.value
    return moisture_value

def send_line_notify(message, token):
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + "6hrQvIiWDsoKoUYwa07F5XsRYVqyIMD7SMDhn0cqCsX"}
    data = {"message": message}
    requests.post(line_notify_api, headers=headers, data=data)

line_notify_token = "6hrQvIiWDsoKoUYwa07F5XsRYVqyIMD7SMDhn0cqCsX"

while True:
    moisture_value = read_soil_moisture()

    if moisture_value < 0.5:
        message = f"lowsoil! soil: {moisture_value}"
        send_line_notify(message, line_notify_token)
        time.sleep(60)
        send_line_notify("reduce water on plants!", line_notify_token)
    else:
        messagehigh = f"highsoil! soil: {moisture_value}"
        send_line_notify(messagehigh, line_notify_token)
    print("complete!")
    time.sleep(3600)
                        
