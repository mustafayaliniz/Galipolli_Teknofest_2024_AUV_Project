#include <Servo.h>
Servo servoMotor; 
const int trigPin = 7;
const int echoPin = 6;
const int buzzer = 10;
long mesafe;
long sure;
long deger = 0;

/*
@author: MUSTAFA YALINIZ
*/

void setup() {
  Serial.begin(9600);
  servoMotor.attach(9);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  pinMode(buzzer,OUTPUT);
}

void loop() {
  
  for (int donus = 0; donus <= 180; donus += 1) { 
    servoMotor.write(donus);  
    delay(50);  
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    sure = pulseIn(echoPin, HIGH);
    mesafe = sure / 58.0;

    Serial.print("Mesafe: ");
    Serial.print(mesafe);
    Serial.println(" cm");

    if (mesafe >= deger) {
      deger = mesafe;
      deger = deger - 10;
    }
    if (deger > mesafe) {
      Serial.println("Nesne Bulundu :)");
      digitalWrite(buzzer,HIGH);
      delay(500);
      digitalWrite(buzzer,LOW);
      delay(500);
      deger = mesafe;
    }
  }
  for (int donus = 180; donus >= 0; donus -= 1) { 
    servoMotor.write(donus);  
    delay(50); 
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
  sure = pulseIn(echoPin, HIGH); 
    
    mesafe = sure / 58.0;

    Serial.print("Mesafe: ");
    Serial.print(mesafe);
    Serial.println(" cm");
    if (mesafe >= deger) {
      deger = mesafe;
      deger = deger - 10;
    }
    if (deger > mesafe) {
      Serial.println("Nesne Bulundu :)");
      digitalWrite(buzzer,HIGH);
      
      deger = mesafe;
    }
  }
}
