import cv2
from PIL import Image
from util import get_limits
import requests
import json

red = [0, 0, 255]  # red in BGR colorspace
cap = cv2.VideoCapture('video/2.mp4')

while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=red)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        # Define the JSON payload
        payload = {
            "name": "Blood"
        }
        # Convert the payload to a JSON string
        json_payload = json.dumps(payload)
        # Define the API endpoint
        url = "http://127.0.0.1:5000/notifications"
        # Send a POST request with the JSON payload
        response = requests.post(url, data=json_payload)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
