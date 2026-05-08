import requests      # 웹에서 데이터를 요청하기 위한 라이브러리
import re            # 문자열에서 원하는 패턴을 찾기 위한 정규표현식 라이브러리
import time          # 프로그램 실행 시간 제어를 위한 라이브러리
import datetime      # 현재 날짜와 시간을 가져오기 위한 라이브러리
import telepot       # 텔레그램 봇 제어 라이브러리

# 텔레그램 채팅방 ID
telegram_id = '8676460552'

# 텔레그램 봇 토큰
my_token = '7748975963:@@FHzMmA45grcNzPCU-neNhMCIoFbnwvKMU'
 
# 텔레그램 봇 객체 생성
bot = telepot.Bot(my_token)

# 날씨 정보를 가져오는 함수
def getWeather():
    
    # 기상청 동네예보 RSS 주소
    url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4139054000"
    
    # 해당 주소에 접속하여 데이터 요청
    response = requests.get(url)

    # 정규표현식을 사용하여 시간 정보 추출
    time = re.findall(r'<hour>(.+?)</hour>', response.text)
    
    # 기온 정보 추출
    temp = re.findall(r'<temp>(.+)</temp>', response.text)
    
    # 습도 정보 추출
    humi = re.findall(r'<reh>(.+?)</reh>', response.text)
    
    # 날씨 상태 정보 추출
    wfKor = re.findall(r'<wfKor>(.+?)</wfKor>', response.text)

    # 최종 출력할 문자열 변수
    text = ""

    # 앞에서 가져온 날씨 데이터 8개 출력
    for i in range(8):
        
        # 시간 추가
        text = text + "(" + str(time[i]) + "시 "
        
        # 기온 추가
        text = text + str(temp[i]) + "C "
        
        # 습도 추가
        text = text + str(humi[i]) + "% "
        
        # 날씨 상태 추가
        text = text + str(wfKor[i]) + ")"

    # 완성된 문자열 반환
    return text

try:
    
    # 무한 반복 실행
    while True:
        
        # 현재 날짜와 시간 가져오기
        now = datetime.datetime.now()
        
        # 시:분:초 형식으로 변환
        hms = now.strftime('%H:%M:%S')

        # 현재 시간 출력
        print(hms)

        # 특정 시간이 되면 실행
        if hms == "20:15:50":
            
            # 날씨 정보 가져오기
            msg = getWeather()

            # 콘솔에 출력
            print(msg)

            # 텔레그램으로 메시지 전송
            bot.sendMessage(chat_id = telegram_id, text = msg)
        
        # 1초마다 반복 실행
        time.sleep(1.0)

# Ctrl + C 입력 시 프로그램 종료
except KeyboardInterrupt:
    pass
