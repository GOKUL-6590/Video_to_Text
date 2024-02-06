import cv2

video_path = "video.mp4"
cap = cv2.VideoCapture(video_path)

frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

from moviepy.editor import VideoFileClip

video_clip = VideoFileClip(video_path)
audio_clip = video_clip.audio
audio_clip.write_audiofile("audio.wav")

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("audio.wav") as source:
    audio_text = recognizer.record(source)

text = recognizer.recognize_google(audio_text)
print("Text from audio:", text)

with open("output.txt", "w") as file:
    file.write(text)


