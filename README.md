<div align="center">

# Voice Watermark

### 음성 워터마크 기반 딥페이크 오디오 검출 엔진

**딥페이크 음성을 실시간으로 판별하는 MFCC + SVM 기반 분류 파이프라인**

<br>

<img src="https://img.shields.io/badge/%EC%A0%9C70%ED%9A%8C%20%EC%A0%84%EA%B5%AD%EA%B3%BC%ED%95%99%EC%A0%84%EB%9E%8C%ED%9A%8C-%ED%8A%B9%EC%83%81-FFD700?style=for-the-badge" alt="특상"/>
<img src="https://img.shields.io/badge/%EC%82%B0%EC%97%85%ED%86%B5%EC%83%81%EC%9E%90%EC%9B%90%EB%B6%80%EC%9E%A5%EA%B4%80%EC%83%81-2024.11-0052CC?style=for-the-badge" alt="산업통상자원부장관상"/>

<br><br>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-SVM-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![librosa](https://img.shields.io/badge/librosa-Audio-8B5CF6?style=flat-square)
![PyQt5](https://img.shields.io/badge/PyQt5-Desktop_GUI-41CD52?style=flat-square&logo=qt&logoColor=white)

</div>

---

## 배경

AI 음성 합성 기술의 급격한 발전으로 딥페이크 오디오를 이용한 사기, 여론 조작, 사칭 범죄가 급증하고 있습니다. 사람의 귀로는 구분이 불가능한 수준의 합성 음성이 범죄에 악용되는 현실에서, **미디어 플랫폼 수준의 자동 검증 기술**이 필수적입니다.

**Voice Watermark**는 오디오 신호의 주파수 특성을 분석하여 딥페이크 여부를 자동 판별하는 검출 엔진입니다.

## 동작 원리

```
오디오 입력 (.wav)
    |
    v
MFCC 특징 추출 (13-dimensional)
    |  n_fft=2048, hop_length=512
    v
StandardScaler 정규화
    |
    v
SVM 분류기 (Linear Kernel)
    |
    v
판정 결과: Real / Deepfake
```

1. **MFCC 특징 추출** -- librosa를 사용하여 오디오에서 13차원 MFCC(Mel-Frequency Cepstral Coefficients) 벡터를 추출합니다. MFCC는 사람 음성의 음색 특성을 압축적으로 표현하며, 합성 음성에서 나타나는 미세한 주파수 패턴 차이를 포착합니다.
2. **정규화** -- StandardScaler로 특징 벡터를 정규화하여 모델 입력의 스케일을 통일합니다.
3. **SVM 분류** -- Linear Kernel SVM이 정규화된 MFCC 벡터를 입력받아 Real(진짜) 또는 Deepfake(합성)으로 이진 분류합니다.

## 시스템 구성도

![flowchart](https://github.com/user-attachments/assets/cadffbda-6f52-421a-acf8-ee200299c4cb)

## 주요 기능

| 기능 | 설명 |
|------|------|
| 모델 학습 | Real/Fake 오디오 데이터셋으로 SVM 분류기를 학습 |
| 딥페이크 판별 | 단일 오디오 파일을 입력받아 Real/Deepfake 판정 |
| 데스크톱 GUI | PyQt5 기반 비디오 업로드 인터페이스 제공 |
| 비디오 오디오 추출 | 영상에서 오디오 트랙을 자동 분리하여 분석 |
| 결과 뷰어 | 업로드된 영상의 딥페이크 판별 결과를 썸네일로 확인 |

## 기술 스택

| 분류 | 기술 |
|------|------|
| 오디오 처리 | librosa, MoviePy |
| 머신러닝 | scikit-learn (SVM, StandardScaler) |
| 특징 추출 | MFCC (13-dim) |
| 데스크톱 GUI | PyQt5 |
| 영상 뷰어 | OpenCV, tkinter, PIL |
| 직렬화 | joblib (.pkl) |

## 프로젝트 구조

```
voice-watermark/
  main.py              # 모델 학습 및 딥페이크 판별 핵심 모듈
  newmain.py           # PyQt5 데스크톱 GUI (비디오 업로드 + 판별)
  youtube.py           # 업로드 영상 썸네일 뷰어
  svm_model.pkl        # 학습된 SVM 분류 모델
  scaler.pkl           # 학습된 StandardScaler
  upload_icon.png      # GUI 업로드 아이콘
  watermark.zip        # 워터마크 관련 리소스
```

## 실행 방법

### 사전 준비

```bash
pip install librosa numpy scikit-learn joblib PyQt5 moviepy opencv-python pillow
```

### 딥페이크 판별

```python
from main import analyze_audio

# True = Deepfake, False = Real
result = analyze_audio("sample.wav")
```

### 모델 재학습

`main.py`의 `main()` 함수를 실행하면 지정된 데이터셋 디렉토리에서 Real/Fake 오디오를 읽어 SVM 모델을 새로 학습합니다.

```bash
python main.py
```

### 데스크톱 GUI 실행

```bash
python newmain.py
```

비디오 파일을 업로드하면 오디오를 자동 추출하고, 딥페이크 여부를 판별하여 결과를 표시합니다.

## 관련 프로젝트

| 리포지토리 | 설명 |
|-------------|------|
| [front-watermark](https://github.com/hwan809/front-watermark) | Streamlit 기반 웹 플랫폼 (비디오 업로드 + 보이스 피싱 감지) |

## 수상

**제70회 전국과학전람회 특상 (산업통상자원부장관상)** -- 2024년 11월

---

<div align="center">
<sub>음성 워터마크 기반 딥페이크 검증 플랫폼 프로젝트의 일부입니다.</sub>
</div>
