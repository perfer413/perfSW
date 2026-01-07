#source .env/bin/activate
#импорты
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import Image, ImageFormat
import numpy as np
#открытие камеры
cap = cv2.VideoCapture(0)
#настройка опций
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2,
                                       running_mode=vision.RunningMode.VIDEO
                                       )
detector = vision.HandLandmarker.create_from_options(options)
#введение переменной
timestamp_ms = 0
#вечный цикл
while True:
# преобразование изображенияя с камеры
   ret, img = cap.read()
   rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
#созданеие массива numpy
   mp_image = Image(
       image_format=ImageFormat.SRGB,
       data=rgb_frame
   )
#обработка видео
   result = detector.detect_for_video(mp_image, timestamp_ms)
   timestamp_ms += 33
   print(result.hand_landmarks)
   print(" ")

   annotated_image = img.copy()
   height, width, _ = annotated_image.shape
        
   # Просто рисуем точки без соединений
   for hand_landmarks in result.hand_landmarks:
      for landmark in hand_landmarks:
            x = int(landmark.x * width)
            y = int(landmark.y * height)
            cv2.circle(annotated_image, (x, y), 5, (0, 0, 255), -1)   
#открытие окна
   cv2.imshow("hand", annotated_image)
   if cv2.waitKey(10) == ord('q'):
       break

cap.release()
cv2.destroyAllWindows() 
