# MQTT 통신을 위한 paho mqtt 라이브러리 import
import paho.mqtt.client as mqtt

# 시간 지연 함수 사용을 위한 time 라이브러리 import
import time

# 라즈베리파이 GPIO 핀으로 LED를 제어하기 위한 gpiozero 라이브러리 import
from gpiozero import LED

# 동시에 여러 작업을 처리하기 위한 threading 라이브러리 import
import threading


# GPIO 16번 핀에 연결된 초록색 LED 객체 생성
greenLed = LED(16)

# GPIO 20번 핀에 연결된 파란색 LED 객체 생성
blueLed = LED(20)

# GPIO 21번 핀에 연결된 빨간색 LED 객체 생성
redLed = LED(21)


# MQTT 메시지를 수신했을 때 자동으로 실행되는 함수
def on_message(client, userdata, msg):

    # 수신한 토픽과 메시지 내용을 출력
    print(msg.topic + " " + str(msg.payload))

    # byte 형태의 메시지를 문자열로 변환
    message = msg.payload.decode()

    # 변환된 메시지 출력
    print(message)

    # 수신한 메시지에 따라 LED 제어 수행
    if message == "green_on":
        greenLed.on()      # 초록색 LED 켜기

    elif message == "green_off":
        greenLed.off()     # 초록색 LED 끄기

    elif message == "blue_on":
        blueLed.on()       # 파란색 LED 켜기

    elif message == "blue_off":
        blueLed.off()      # 파란색 LED 끄기

    elif message == "red_on":
        redLed.on()        # 빨간색 LED 켜기

    elif message == "red_off":
        redLed.off()       # 빨간색 LED 끄기


# MQTT 클라이언트 객체 생성
client = mqtt.Client()

# 메시지를 수신했을 때 실행할 콜백 함수 등록
client.on_message = on_message


# MQTT 브로커(서버)의 IP 주소 저장
broker_address = "192.168.137.230"

# MQTT 브로커에 연결 요청
client.connect(broker_address)


# "led"라는 토픽을 구독
# QoS(Quality of Service) 레벨은 1로 설정
client.subscribe("led", 1)


# 메시지 전송 횟수를 저장할 변수
count = 0


# 별도의 스레드에서 실행될 함수 정의
def send_thread():

    # 전역 변수 count 사용 선언
    global count

    # 무한 반복 수행
    while 1:

        # count 값을 1 증가
        count = count + 1

        # "hello" 토픽으로 count 값 전송
        client.publish("hello", str(count))

        # 1초 동안 대기
        time.sleep(1.0)


# send_thread 함수를 실행할 스레드 객체 생성
task = threading.Thread(target=send_thread)

# 스레드 시작
task.start()


# MQTT 네트워크 루프 실행
# 프로그램이 종료되지 않고 계속 메시지를 수신 대기함
client.loop_forever()
