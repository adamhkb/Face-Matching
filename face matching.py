import cv2
import face_recognition
import numpy as np


#### PATH TO IC IMAGE
imgIC_path = '/Users/adamkamarul/PycharmProjects/face_recognition/IC and Selfie/mrbean ic.jpeg'
#imgIC_path = '/Users/adamkamarul/PycharmProjects/face_recognition/IC and Selfie/chad smith.jpg'
#imgIC_path = '/Users/adamkamarul/PycharmProjects/face_recognition/IC and Selfie/ic example.jpeg'

### PATH TO SELFIE IMAGE
#imgSelfie_path = '/Users/adamkamarul/PycharmProjects/face_recognition/IC and Selfie/mrbean selfie 2.jpg'
imgSelfie_path = '/Users/adamkamarul/PycharmProjects/face_recognition/IC and Selfie/Obama.jpg'
#imgSelfie_path = '/Users/adamkamarul/PycharmProjects/face_recognition/IC and Selfie/will ferrell.jpeg'


imgIC = face_recognition.load_image_file(imgIC_path)
imgIC = cv2.cvtColor(imgIC, cv2.COLOR_BGR2RGB)


imgSelfie = face_recognition.load_image_file(imgSelfie_path)
imgSelfie = cv2.cvtColor(imgSelfie, cv2.COLOR_BGR2RGB)


faceLocIC = face_recognition.face_locations(imgIC)[0]
encodeIC = face_recognition.face_encodings(imgIC)[0]
cv2.rectangle(imgIC, (faceLocIC[3],faceLocIC[0]),(faceLocIC[1],faceLocIC[2]), (0,255,255),2)


faceLocSelfie = face_recognition.face_locations(imgSelfie)[0]
encodeSelfie = face_recognition.face_encodings(imgSelfie)[0]
cv2.rectangle(imgSelfie, (faceLocSelfie[3],faceLocSelfie[0]),(faceLocSelfie[1],faceLocSelfie[2]), (0,255,255),2)


results = face_recognition.compare_faces([encodeIC], encodeSelfie)
faceDis = face_recognition.face_distance([encodeIC], encodeSelfie)


if results[0] == True:
    cv2.putText(imgSelfie, f'Face matches! Confidence: {round(faceDis[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0),2)
    cv2.rectangle(imgIC, (faceLocIC[3], faceLocIC[0]), (faceLocIC[1], faceLocIC[2]), (0, 255, 0), 2)
    cv2.rectangle(imgSelfie, (faceLocSelfie[3], faceLocSelfie[0]), (faceLocSelfie[1], faceLocSelfie[2]), (0, 255, 0), 2)


else:
    cv2.putText(imgSelfie, f'Face does not match! Confidence: {round(faceDis[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255),2)
    cv2.rectangle(imgIC, (faceLocIC[3], faceLocIC[0]), (faceLocIC[1], faceLocIC[2]), (0, 255, 0), 2)
    cv2.rectangle(imgSelfie, (faceLocSelfie[3], faceLocSelfie[0]), (faceLocSelfie[1], faceLocSelfie[2]), (0, 0, 255), 2)

# concatanate image Horizontally
#Hori = np.concatenate((imgIC, imgSelfie), axis=1)
# concatanate image Vertically
#Verti = np.concatenate((imgIC, imgSelfie), axis=0)
#cv2.imshow('IC and Selfie Images Comparison', Verti)

cv2.imshow('IC Image', imgIC)
cv2.imshow('Selfie Image', imgSelfie)
cv2.waitKey(0)

# Not a match -------------------------------- 0 -------------------------------- It's a match



