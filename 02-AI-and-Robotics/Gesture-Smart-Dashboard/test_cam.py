import cv2

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

for i in range(5):
    ret, frame = cap.read()

cv2.imshow("Test", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()