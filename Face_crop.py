# import cv2,glob
import  os
Id =input('Enter your name with your Enrollment number: ')
path='C:/Users/kusha/PycharmProjects/Attendace managemnt system/Datasets/'+ Id

try:
    os.mkdir(path)
except FileExistsError as e:
    print(e)
#
# images=glob.glob("*.jpg")
#
# for image in images:
#     facedata = "haarcascade_frontalface_alt.xml"
#     cascade = cv2.CascadeClassifier(facedata)
#     img=cv2.imread(image,0)
#
#     re=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
#     faces = cascade.detectMultiScale(re)
#
#     for f in faces:
#         x, y, w, h = [v for v in f]
#         Rect=cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#         sub_face = img[y:y + h, x:x + w]
#
#         f_name = image.split('/')
#         f_name = f_name[-1]
#         cv2.imshow("checking",sub_face)
#         cv2.waitKey(500)
#         cv2.destroyAllWindows()
#
#
#
#         cv2.imwrite("resized_"+image,sub_face)