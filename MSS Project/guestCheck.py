# 손님이 왔는지 확인해서 mqtt로 전달함
import time
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

trig = 20  # 빵판으로는 상단19번
echo = 16  # 빵판으로는 상단18번
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)

ip = "localhost"

client = mqtt.Client()
client.connect(ip, 1883)

client.loop_start()


def measureDistance(trig, echo):
    time.sleep(0.5)
    GPIO.output(trig, True)  # 신호 1 발생
    time.sleep(0.00001)  # 짧은 시간을 나타내기 위함
    GPIO.output(trig, False)  # 신호 0 발생

    while(GPIO.input(echo) == 0):
        pulse_start = time.time()  # 신호 1을 받았던 시간
    while(GPIO.input(echo) == 1):
        pulse_end = time.time()  # 신호 0을 받았던 시간

    pulse_duration = pulse_end - pulse_start
    return 340*100/2*pulse_duration


while True:
    distance = measureDistance(trig, echo)
    if distance < 20:  # 물체가 일정거리 이상 가까워질경우 => 손님방문
        print("손님 방문")
        client.publish("guest", distance, qos=0)
        time.sleep(10)  # 손님 방문사실을 알린 이후, 중복 메세지를 보내지 않도록 하기 위함
