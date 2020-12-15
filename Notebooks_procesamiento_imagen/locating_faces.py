import cv2


faceClassifier = cv2.CascadeClassifier()

image = cv2.imread("Houses/Gryffindor/Padma-Patil.jpeg")

imageAux = image.copy()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)




faces =  faceClassifier.detectMultiScale(gray,1.1,5)
count = 0



for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(128.0,255),2)
    rostro = imageAux[y:y+h,x:x+w]
    rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("rostro_{}.jpg".format(count),rostro)
    count = count+1

    cv2.imshow("rostro",rostro)
    cv2.imshow("image",image)
    cv2.waitKey(0)




cv2.destroyAllWindows()
