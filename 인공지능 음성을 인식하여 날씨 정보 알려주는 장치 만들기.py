# 음성 인식 기능을 사용하기 위한 speech_recognition 라이브러리 불러오기
import speech_recognition as sr

# OpenWeatherMap API 요청을 보내기 위한 requests 라이브러리 불러오기
import requests

# 운영체제 명령어 실행을 위한 os 라이브러리 불러오기
import os

# 시간 관련 기능 사용을 위한 time 라이브러리 불러오기
import time


# OpenWeatherMap에서 발급받은 API 키 입력
API_KEY = "Enter your API key here"

# 서울의 현재 날씨 정보를 요청하는 URL 생성
url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"


# espeak를 이용하여 문자열을 음성으로 출력하는 함수
def speak(option, msg):
    
    # espeak 명령어 실행
    os.system("espeak {} '{}'".format(option, msg))


try:
    
    # 프로그램을 계속 실행하기 위한 무한 반복문
    while True:
        
        # 음성 인식 객체 생성
        r = sr.Recognizer()
        
        
        # 마이크 장치를 입력 소스로 사용
        with sr.Microphone() as source:
            
            # 사용자에게 음성 입력 안내 메시지 출력
            print("Say something!")
            
            # 마이크로부터 음성 데이터 입력 받기
            audio = r.listen(source)
            
            
        try:
            
            # Google Speech Recognition API를 사용하여
            # 한국어 음성을 텍스트로 변환
            text = r.recognize_google(audio, language='ko-KR')
            
            # 인식된 텍스트 출력
            print("You said: " + text)
            
            
            # 사용자가 "날씨"라는 단어를 말했는지 확인
            if text in "날씨":
                
                # 날씨 음성이 인식되었음을 출력
                print("날씨 음성을 인식하였습니다.")
                
                
                # OpenWeatherMap API에 GET 요청 보내기
                response = requests.get(url)
                
                # 응답 데이터를 JSON 형식으로 변환
                data = response.json()
                
                
                # 현재 기온 데이터 가져오기
                temp = data["main"]["temp"]
                
                # 현재 습도 데이터 가져오기
                humi = data["main"]["humidity"]
                
                
                # 음성으로 출력할 메시지 생성
                msg = '기온은 ' + str(int(temp)) + '도 습도는 ' + str(humi) + '퍼센트 입니다'
                
                
                # espeak 음성 옵션 설정
                # -s : 말하기 속도
                # -p : 음성 높낮이
                # -a : 음량
                # -v : 음성 종류(한국어 여성 음성)
                option = '-s 180 -p 50 -a 200 -v ko+f5'
                
                
                # 날씨 정보를 음성으로 출력
                speak(option, msg)
            
            
        # 음성을 제대로 인식하지 못했을 때 발생하는 예외 처리
        except sr.UnknownValueError:
            
            print("Google Speech Recognition could not understand audio")
        
        
        # Google Speech API 요청 실패 시 발생하는 예외 처리
        except sr.RequestError as e:
            
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


# Ctrl + C 입력 시 프로그램 정상 종료
except KeyboardInterrupt:
    
    pass
