import cv2
import serial

# Arduino'ya bağlı seri port
arduino_port = "COM3"  # Seri port numarasını uygun şekilde değiştirin
arduino_baudrate = 9600

# Arduino ile seri iletişim
arduino = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

# Opencv DNN
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

# Load class lists
classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()  # satır arası boşluklar için
        classes.append(class_name)

# Initialize camera
cap = cv2.VideoCapture(0)

# Servo motorunun sınırları
servo_min = 0
servo_max = 180

while True:
    # Get frames
    ret, frame = cap.read()

    # Object Detection
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
    

    if class_ids is not None and len(class_ids) > 0 and class_ids[0] == classes.index('person'):
        # İnsan tespiti yapıldı
        bbox = bboxes[0]
        (x, y, w, h) = bbox

        # Yüzün merkezini hesapla
        center_x = x + w // 2

        # Yeni bir oran belirle
        ratio = 2.0  

        # Arduino'ya veri gönder
        servo_pos = int(servo_max - (center_x / frame.shape[1]) * (servo_max - servo_min)) + 100
        arduino.write((str(servo_pos) + '\n').encode())

        # Nesneyi çerçevele
        cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 0, 50), 3)

        class_name = classes[class_ids[0]]

        cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 3, (200, 0, 50), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

# Seri portu kapat
arduino.close()

# Kamera penceresini kapat
cap.release()
cv2.destroyAllWindows()
