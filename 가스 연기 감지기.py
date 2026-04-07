Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from gpiozero import DigitalInputDevice 
... from gpiozero import OutputDevice       
... import time                             
... 
... # GPIO 핀 번호 할당 및 인스턴스 생성 (18번: 부저, 17번: MQ-2 DO 핀)
... bz = OutputDevice(18)
... gas = DigitalInputDevice(17)
... 
... try: # 무한 루프 시작 
...     while True:
...         # 센서의 Digital Output이 0(Active Low)인 경우 이벤트 처리
...         if gas.value == 0:
...             print("가스 감지됨")  # 출력창에 "가스 감지됨" 출력 
...             bz.on()               # 부저 ON 
...         
...         # 가스 농도가 임계값 미만(Normal)인 경우
...         else:
...             print("정상")         # 출력창에 " 정상 " 출력 
...             bz.off()              # 부저 OFF 
...         
...         # 0.2초마다 센서 확인 설정
...         time.sleep(0.2)
... 
... # 사용자가 직접 프로세스 종료(Ctrl+C) 시 루프 종료 
... except KeyboardInterrupt:
...     pass
... 
... # 프로그램 종료 시 부저 OFF 처리 
