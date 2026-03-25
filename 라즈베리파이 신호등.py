Python 3.15.0a7 (tags/v3.15.0a7:6024d3c, Mar 10 2026, 13:09:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from gpiozero import LED # 라즈베리파이 GPIO 핀을 제어하기 위해 라이브러리에서 LED 클래스를 불러옴
... from time import sleep   # 일정 시간 동안 동작을 멈추기 위해 sleep 함수를 불러옴
... 
... # GPIO 핀 번호를 숫자로 할당하는 부분 
... carLedRed = 2
... carLedYellow = 3
... carLedGreen = 4
... humanLedRed = 20
... humanLedGreen = 21
... 
... # GPIO 핀 번호에 맞춰 각 LED 객체를 생성
... # 차량용 신호등 (2번: 빨강, 3번: 노랑, 4번: 초록)
... carLedRed = LED(2)
... carLedYellow = LED(3)
... carLedGreen = LED(4)
... # 보행자용 신호등 (20번: 빨강, 21번: 초록)
... humanLedRed = LED(20)
... humanLedGreen = LED(21)
... 
... try:
...     while 1: # 신호등 패턴 반복
...         
...         # 1단계: 차도 '초록불' / 보행자 '빨간불' (차량 통행)
...         carLedRed.value = 0      # 차량 빨간불 OFF
...         carLedYellow.value = 0   # 차량 노란불 OFF
...         carLedGreen.value = 1    # 차량 초록불 ON
...         humanLedRed.value = 1    # 보행자 빨간불 ON 
...         humanLedGreen.value = 0  # 보행자 초록불 OFF
...         sleep(3.0)               # 이 상태를 3초 동안 유지
... 
...         # 2단계: 차도 '노란불' / 보행자 '빨간불' (차량 감속 및 정지 준비)
...         carLedRed.value = 0      # 차량 빨간불 OFF
...         carLedYellow.value = 1   # 차량 노란불 ON 
...         carLedGreen.value = 0    # 차량 초록불 OFF
...         humanLedRed.value = 1    # 보행자 빨간불 ON  (보행자는 계속 대기)
...         humanLedGreen.value = 0  # 보행자 초록불 OFF
...         sleep(1.0)               # 이 상태를 1초 동안 유지
... 
...         # 3단계: 차도 '빨간불' / 보행자 '초록불' (보행자 횡단)
...         carLedRed.value = 1      # 차량 빨간불 ON 
...         carLedYellow.value = 0   # 차량 노란불 OFF
...         carLedGreen.value = 0    # 차량 초록불 OFF
...         humanLedRed.value = 0    # 보행자 빨간불 OFF
...         humanLedGreen.value = 1  # 보행자 초록불 ON 
...         sleep(3.0)               # 이 상태를 3초 동안 유지
...         
... except KeyboardInterrupt:  # 사용자가 강제 종료하려할때 켜진채로 방치되는 것을 방지
...     pass # 에러가 발생해도 멈추지 않고 루프를 끝내 아래 줄로 진행
... 
... # 프로그램이 종료되기 전에 모든 불빛을 꺼서 안전하게 상태를 초기화
... carLedRed.value = 0
... carLedYellow.value = 0
... carLedGreen.value = 0
... humanLedRed.value = 0
