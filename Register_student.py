import cv2
import os

try:
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    Id = input('Enter your name with your Enrollment number(please give space between name & enrollment): ')
    path = 'C:/Users/kusha/PycharmProjects/Attendace managemnt system/Datasets/' + Id
    new_path = 'C:/Users/kusha/PycharmProjects/Attendace managemnt system/Datasets/' + Id + '/'
    os.mkdir(path)
    sampleNum = 0
    print('We are getting your face images.......')
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w + h), (255, 0, 0), 2)
            # incrementing sample number
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder
            cv2.imwrite(new_path + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            cv2.imshow('frame', img)
        # wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 100
        elif sampleNum > 199:
            print('Thanks!! you are registered on our Datasets')
            break
    cam.release()
    cv2.destroyAllWindows()

except FileExistsError as f:
    print(f)
