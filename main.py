import cv2
from simple_facerec import SimpleFacerec

# Encode faces from folder
sfr=SimpleFacerec()
sfr.load_encoding_images("images/")

#Load Camera
cap=cv2.VideoCapture(0)



while True:
    ret,frame=cap.read()

    #Detect Fces
    face_loactions,face_names=sfr.detect_known_faces(frame)
    for face_loc,name in zip(face_loactions,face_names):
        y1,x2,y2,x1=face_loc[0],face_loc[1],face_loc[2],face_loc[3]

        cv2.putText(frame,name,(x1,y1-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,200),2)
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,200),4)

    cv2.imshow("Frame",frame)

    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()















# img=cv2.imread("Messi1.webp")
# rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img_encoding=face_recognition.face_encodings(rgb_img)[0]

# img2=cv2.imread("images/Messi.webp")
# rgb_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
# img_encoding2=face_recognition.face_encodings(rgb_img2)[0]

# result=face_recognition.compare_faces([img_encoding],img_encoding2) #compare different image whether they are same
# print("Result:",result)

# cv2.imshow("Img",img)
# # cv2.imshow("Img2",img2)
# cv2.waitKey(0)