import os
import cv2
import tkinter as tk
from PIL import Image, ImageTk

FOLDER_PATH = "uploaded_file"

def get_video_thumbnails(folder_path):
    thumbnails = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.mp4', '.avi', '.mkv', '.mov')):
            video_path = os.path.join(folder_path, file_name)
            cap = cv2.VideoCapture(video_path)
            ret, frame = cap.read()
            if ret:
                thumbnail = cv2.resize(frame, (160, 90))  # 썸네일 크기 설정
                thumbnails.append((file_name, thumbnail))
            cap.release()
    return thumbnails

def display_thumbnails(thumbnails):
    for widget in frame.winfo_children():
        widget.destroy()
    
    for idx, (file_name, thumbnail) in enumerate(thumbnails):
        image = Image.fromarray(cv2.cvtColor(thumbnail, cv2.COLOR_BGR2RGB))
        image_tk = ImageTk.PhotoImage(image)
        
        label = tk.Label(frame, image=image_tk)
        label.image = image_tk
        label.grid(row=idx // 4, column=idx % 4, padx=10, pady=10)

        is_deepfake = file_name.split('$')[-1] == 'fake.mp4'
        
        if is_deepfake:
            text = tk.Label(frame, text=file_name + '\nDeepfake 검출', wraplength=160)
            text.grid(row=idx // 4 + 1, column=idx % 4, padx=10, pady=10)

        else:
            text = tk.Label(frame, text=file_name + '\nDeepfake 안전', wraplength=160)
            text.grid(row=idx // 4 + 1, column=idx % 4, padx=10, pady=10)            

def refresh_thumbnails():
    thumbnails = get_video_thumbnails(FOLDER_PATH)
    display_thumbnails(thumbnails)
    root.after(5000, refresh_thumbnails)  # 5초 후에 다시 refresh_thumbnails 함수 실행

root = tk.Tk()
root.title("Video Viewer")

frame = tk.Frame(root)
frame.pack(pady=20)

refresh_thumbnails()  # 최초 실행하여 썸네일 표시 및 주기적 업데이트 시작

root.mainloop()