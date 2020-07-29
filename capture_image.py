import cv2 # importing cv2 liberary

cam = cv2.VideoCapture(0)

count = 0

while True:
    ret, img = cam.read()

    cv2.imshow("Test", img)

    if not ret:
        break

    k = cv2.waitKey(30) & 0xff

    if k == 27: # press 'ESC' to quit
    #For Esc key
        print("Close")
        break 
    elif k%256==32:
        #For Space key

        print("Image "+str(count)+"saved")
        file='C:/Users/Soujanya/Desktop/TM/'+str(count)+'.jpg'
        cv2.imwrite(file, img)
        count +=1
    

cam.release()
cv2.destroyAllWindows()
