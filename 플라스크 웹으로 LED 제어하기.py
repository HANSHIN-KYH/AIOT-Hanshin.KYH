Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from flask import Flask, render_template, request
... from gpiozero import LED
... 
... # Flask 웹 애플리케이션 객체 생성
... app = Flask(__name__)
... 
... # GPIO 21번 핀에 연결된 LED 객체 생성
... red_led = LED(21)
... 
... # 루트 URL('/')로 접속했을 때 실행되는 함수
... @app.route('/')
... def home():
...     # index.html 파일을 사용자에게 반환하여 웹 페이지를 표시
...     return render_template("index.html")
... 
... # '/data' URL로 POST 요청이 들어왔을 때 실행되는 함수
... @app.route('/data', methods=['POST'])
... def data():
...     # HTML 폼에서 전달된 'led' 값을 가져옴
...     data = request.form['led']
...     
...     # 전달된 값이 'on'일 경우 LED를 켬
...     if data == 'on':
...         red_led.on()
...     
...     # 전달된 값이 'off'일 경우 LED를 끔
...     elif data == 'off':
...         red_led.off()
...     
...     # 작업 수행 후 다시 메인 페이지를 반환
...     return home()
... 
... # 해당 파일이 직접 실행될 때 Flask 서버를 동작시킴
... if __name__ == "__main__":
...     # 모든 IP에서 접속 가능하도록 설정하고, 80번 포트로 서버 실행
