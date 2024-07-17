# Turret Project

This project uses Python and Arduino to create an automated turret that detects and tracks a person using a camera and moves a servo motor accordingly. The system uses OpenCV for object detection and communicates with Arduino via serial communication to control the servo motor.

## Components

- Arduino Uno
- Servo motor
- Camera
- LCD Display (I2C)
- Connecting wires
- Computer with Python installed

## Setup

### Arduino

1. Connect the servo motor to pin 9 on the Arduino.
2. Connect the LCD display to the I2C pins.
3. Upload the provided Arduino code (`turret_arduino.ino`) to the Arduino.

### Python

1. Install the required Python libraries:
    ```sh
    pip install opencv-python pyserial
    ```
2. Download the YOLOv4-tiny model and the `classes.txt` file.
3. Place the `yolov4-tiny.weights`, `yolov4-tiny.cfg`, and `classes.txt` files in a folder named `dnn_model`.
4. Run the provided Python script (`turret.py`).

## Usage

1. Ensure all hardware is connected and both the Arduino and Python scripts are running.
2. The camera will detect a person and send the coordinates to the Arduino.
3. The Arduino will adjust the servo motor to follow the detected person.
4. The LCD display will show the current status (`ENEMY` or `CLEAR`) and the servo position.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
