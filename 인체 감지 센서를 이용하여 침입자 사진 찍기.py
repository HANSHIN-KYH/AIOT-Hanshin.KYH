from gpiozero import MotionSensor  # GPIO 장치 제어를 위한 인터페이스 라이브러리
import time
from picamera2 import Picamera2    # Raspberry Pi 카메라 모듈 제어를 위한 라이브러리
import datetime

# 1. PIR 센서 객체 인스턴스화 (GPIO 16번 핀 사용)
pirPin = MotionSensor(16)

# 2. 카메라 하드웨어 설정 및 초기화
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()  # 카메라 스트리밍 프로세스 시작

try:
    # 3. 모션 감지 및 데이터 처리를 위한 메인 루프
    while True:
        try:
            # 디지털 입력값 모니터링 (High: 1, Low: 0)
            sensorValue = pirPin.value
            
            if sensorValue == 1:
                # 이벤트 발생 시점의 시스템 타임스탬프 획득
                now = datetime.datetime.now()
                print(now)
                
                # 시계열 데이터를 기반으로 고유 파일명 생성
                fileName = now.strftime('%Y-%m-%d %H:%M:%S')
                
                # 이미지 캡처 실행 및 지정된 경로로 파일 저장
                picam2.capture_file(fileName + '.jpg')
                
                # 센서의 채터링 방지 및 프로세서 부하 감소를 위한 딜레이 설정
                time.sleep(0.5)
                
        except:
            # 예외 발생 시 무시하고 루프를 유지하여 시스템 가용성 확보
            pass

except KeyboardInterrupt:
    # 사용자 인터럽트(Ctrl+C) 발생 시 안전하게 프로그램을 종료
    pass
