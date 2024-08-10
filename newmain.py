import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog  # QFileDialog 추가
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QPainter, QPen, QBrush, QColor
import shutil

from main import analyze_audio

from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_file_path, audio_file_path):
    video = VideoFileClip(video_file_path)
    video.audio.write_audiofile(audio_file_path, codec='pcm_s16le')

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('업로드')
        self.setGeometry(100, 100, 800, 600)  # 윈도우 위치와 크기 설정

        self.rect_x = 150
        self.rect_y = 150
        self.rect_width = 500
        self.rect_height = 300

        # QLabel 생성 및 설정
        label = QLabel(self)
        label.setText('Video Upload')
        label.setAlignment(Qt.AlignCenter)  # 가운데 정렬
        label.setStyleSheet("font: bold 32px;")  # 폰트 설정
        label.resize(label.sizeHint())
        label.move((self.width() - label.width()) // 2, 50)

        # 사진을 QLabel에 표시
        pixmap = QPixmap('upload_icon.png')
        pixmap = pixmap.scaledToWidth(150)  # 사진 크기 조정
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)
        image_label.setGeometry((self.width() - pixmap.width()) // 2, 180, pixmap.width(), pixmap.height())

        # 텍스트 추가
        text_label = QLabel('딥페이크 걱정없는 안전한 업로드', self)
        text_label.setAlignment(Qt.AlignCenter)  # 가운데 정렬
        text_label.setStyleSheet("font: bold 16px;")  # 폰트 설정
        text_label.adjustSize()  # 텍스트에 맞게 크기 조정
        text_label.setGeometry((self.width() - text_label.width()) // 2, 180 + pixmap.height() + 30, text_label.width(), text_label.height())

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.DotLine))
        painter.setBrush(QBrush(Qt.NoBrush))
        painter.drawRoundedRect(self.rect_x, self.rect_y, self.rect_width, self.rect_height, 20, 20)

    def mousePressEvent(self, event):
        if self.rect_x <= event.x() <= self.rect_x + self.rect_width and self.rect_y <= event.y() <= self.rect_y + self.rect_height:
            # 파일 업로드 다이얼로그 표시
            file_dialog = QFileDialog()
            file_path = file_dialog.getOpenFileName(self, '파일 업로드', '', 'All Files (*.*)')[0]
            wav_file_path = f'./uploaded_file/{file_path[0]}.wav'
            extract_audio_from_video(file_path, wav_file_path)

            filee_name = file_path.split('/')[-1]
            if analyze_audio(wav_file_path):
                shutil.copy(file_path, f'./uploaded_file/{filee_name}$fake.mp4')
            else:
                shutil.copy(file_path, f'./uploaded_file/{filee_name}$real.mp4')                    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    sys.exit(app.exec_())
