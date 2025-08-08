import cv2

image = cv2.imread('aceattorneySpeech1.jpg')
if image is None:
    print("Error: Could not read the image.")
else:
    image = cv2.resize(image, (1080, 720))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#canny
    bordas = cv2.Canny(image, 100, 200)
    cv2.imshow('Canny', bordas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



