# OpenCV 라이브러리 불러오기 (영상 처리 및 객체 인식에 사용)
import cv2

# GPIO 핀에 연결된 부저를 제어하기 위한 라이브러리 불러오기
from gpiozero import Buzzer

# 시간 관련 기능을 사용하기 위한 라이브러리
import time

# GPIO 16번 핀에 연결된 부저 객체 생성
buzzerPin = Buzzer(16)

# 메인 함수 정의
def main():

    # 카메라 장치 열기 (-1은 자동으로 연결된 카메라 탐색)
    camera = cv2.VideoCapture(-1)

    # 카메라 해상도 설정 (가로 640픽셀)
    camera.set(3, 640)

    # 카메라 해상도 설정 (세로 480픽셀)
    camera.set(4, 480)

    # 얼굴 검출을 위한 Haar Cascade 모델 경로 지정
    face_xml = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

    # 눈 검출을 위한 Haar Cascade 모델 경로 지정
    eye_xml = cv2.data.haarcascades + 'haarcascade_eye.xml'

    # 얼굴 검출 분류기 생성
    face_cascade = cv2.CascadeClassifier(face_xml)

    # 눈 검출 분류기 생성
    eye_cascade = cv2.CascadeClassifier(eye_xml)

    # 카메라가 정상적으로 열려 있는 동안 반복 실행
    while(camera.isOpened()):

        # 카메라로부터 한 프레임 읽어오기
        _, image = camera.read()

        # 얼굴 검출 성능 향상을 위해 흑백 이미지로 변환
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 흑백 이미지에서 얼굴 검출 수행
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,      # 탐색 창 크기를 10%씩 증가시키며 탐색
            minNeighbors=5,       # 5번 이상 검출된 경우 얼굴로 판단
            minSize=(100, 100),   # 최소 얼굴 크기 지정
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # 검출된 얼굴 개수를 터미널에 출력
        print("faces detected Number: " + str(len(faces)))

        # 얼굴이 하나 이상 검출된 경우
        if len(faces):

            # 검출된 얼굴마다 반복
            for (x, y, w, h) in faces:

                # 얼굴 영역에 파란색 사각형 표시
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # 얼굴 영역만 흑백 이미지로 추출
                face_gray = gray[y:y+h, x:x+w]

                # 얼굴 영역만 컬러 이미지로 추출
                face_color = image[y:y+h, x:x+w]

                # 얼굴 영역 안에서 눈 검출 수행
                eyes = eye_cascade.detectMultiScale(
                    face_gray,
                    scaleFactor=1.1,
                    minNeighbors=5
                )

                # 검출된 눈이 1개 이하이면 졸음 상태로 판단하여 부저 작동
                if len(eyes) <= 1:
                    buzzerPin.on()

                # 눈이 2개 이상 검출되면 정상 상태로 판단하여 부저 정지
                else:
                    buzzerPin.off()

                # 검출된 눈마다 반복
                for (ex, ey, ew, eh) in eyes:

                    # 눈 영역에 초록색 사각형 표시
                    cv2.rectangle(
                        face_color,
                        (ex, ey),
                        (ex+ew, ey+eh),
                        (0, 255, 0),
                        2
                    )

        # 결과 영상을 화면에 출력
        cv2.imshow('result', image)

        # q 키를 누르면 반복문 종료
        if cv2.waitKey(1) == ord('q'):
            break

    # 모든 OpenCV 창 닫기
    cv2.destroyAllWindows()

    # 프로그램 종료 전 부저 끄기
    buzzerPin.off()


# 현재 파일을 직접 실행했을 때만 main() 함수 실행
if __name__ == '__main__':
    main()
