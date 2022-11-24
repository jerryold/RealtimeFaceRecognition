---
tags: Opencv-Python
---
# FaceRecognition Realtime
* Installations    `
    * face_recognition        
    * opencv

* 介紹
* 本實作是透過face_recognition的套件進行相機的即時辨識人名,  根據image folder裡面的圖片資料集進行命名,根據需求將想要辯識的圖片檔案放入即可,本次實作主要將各項球類運動的明星進行辯識

* Find faces in pictures
    * Find all the faces that appear in a picture:
        ![](https://i.imgur.com/yEPocjd.jpg)
        
```
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)
```

* Find and manipulate facial features in pictures
    * Get the locations and outlines of each person's eyes, nose, mouth and chin.
    ![](https://i.imgur.com/T7ekZPA.jpg)    


```
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
```

* Identify faces in pictures
    * Recognize who appears in each photo
    ![](https://i.imgur.com/Lpbin0I.jpg)

```
import face_recognition
known_image = face_recognition.load_image_file("biden.jpg")
unknown_image = face_recognition.load_image_file("unknown.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
```

* 參考資料
   *  https://github.com/ageitgey/face_recognition


* Demo影片

https://user-images.githubusercontent.com/12774427/203752104-36c35963-cddf-484b-b9f5-acc2c1cf1e73.mp4


