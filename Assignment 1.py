import cv2

cap = cv2.VideoCapture(0)

x = int(input('enter '))


if x == 1:
    image = cv2.imread('Partnercappikachu.jpg')
    while True:
        flag, frame = cap.read()
        if not flag:
            print('could not open cam')
            break

        image = cv2.resize(image, (frame.shape[1], frame.shape[0]))
        blended_frame = cv2.addWeighted(frame, 0.8, image, 0.2, gamma=0.1)
        cv2.imshow("blended frame", blended_frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break

elif x == 2:
    image1 = cv2.imread('download.jpg')
    while True:
        flag, frame = cap.read()
        if not flag:
            print('could not open cam')
            break

        image1 = cv2.resize(image1, (frame.shape[1], frame.shape[0]))
        blended_frame1 = cv2.addWeighted(frame, 0.8, image1, 0.2, gamma=0.1)
        cv2.imshow("blended frame", blended_frame1)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break


elif x == 3:
    image2 = cv2.imread('happy-ash-ketchum-and-pikachu-paint-by-number.jpg')
    while True:
        flag, frame = cap.read()
        if not flag:
            print('could not open cam')
            break

        image2 = cv2.resize(image2, (frame.shape[1], frame.shape[0]))
        blended_frame2 = cv2.addWeighted(frame, 0.8, image2, 0.2, gamma=0.1)
        cv2.imshow("blended frame", blended_frame2)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break


elif x == 4:
    image3 = cv2.imread('images.jpg')
    while True:
        flag, frame = cap.read()
        if not flag:
            print('could not open cam')
            break

        image3 = cv2.resize(image3, (frame.shape[1], frame.shape[0]))
        blended_frame3 = cv2.addWeighted(frame, 0.8, image3, 0.2, gamma=0.1)
        cv2.imshow("blended frame", blended_frame3)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break


elif x == 5:
    image4 = cv2.imread('images (1).jpg')
    while True:
        flag, frame = cap.read()
        if not flag:
            print('could not open cam')
            break

        image4 = cv2.resize(image4, (frame.shape[1], frame.shape[0]))
        blended_frame4 = cv2.addWeighted(frame, 0.8, image4, 0.2, gamma=0.1)
        cv2.imshow("blended frame", blended_frame4)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break


elif x == 6:
    image5 = cv2.imread('1456503103-ash-ketchum-wallpaper-3.jpg')
    while True:
        flag, frame = cap.read()
        if not flag:
            print('could not open cam')
            break

        image5 = cv2.resize(image5, (frame.shape[1], frame.shape[0]))
        blended_frame5 = cv2.addWeighted(frame, 0.8, image5, 0.2, gamma=0.1)
        cv2.imshow("blended frame", blended_frame5)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break