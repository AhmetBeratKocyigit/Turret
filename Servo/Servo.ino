#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

int pos = 0;
int buzzer = 7;
Servo myservo;

LiquidCrystal_I2C lcd(0x3f, 16, 2);

void setup() {
  // Seri iletişim başlat
  Serial.begin(9600);
  pinMode(buzzer, OUTPUT);
  lcd.begin();

  // Servo motor pini
  myservo.attach(9);  // Servo pinini uygun şekilde değiştirin
}

void loop() {
  if (Serial.available() > 0) {
    // Seri porttan gelen veriyi oku
    int xPos = Serial.parseInt();

    // Servo motoru hareket ettir
    int servoPos = map(xPos, 0, 640, 0, 180);  // 0-640 arasındaki x koordinatını 0-180 dereceye çevir

    servoPos = constrain(servoPos, 0, 180);

    myservo.write(servoPos);


    lcd.home();
    lcd.print("DUSMAN");
    lcd.setCursor(4, 1);
    lcd.print(servoPos);


    // Bekleme
    delay(15);
  }
  else
  {
    lcd.clear();
    lcd.home();
    lcd.print("TEMIZ");
    for (pos = 0; pos <= 120; pos += 1)
    {
      myservo.write(pos);
      delay(15);
    }
    for (pos = 120; pos >= 0; pos -= 1)
    {
      myservo.write(pos);
      delay(15);
    } 
  }
}
