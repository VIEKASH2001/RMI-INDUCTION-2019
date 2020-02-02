#include <Servo.h>
Servo myservo; 
int potentiometer_pin = A0;  
int servo_angle;   
int potentiometer_value;
void setup() {
  Serial.begin(9600);        
  myservo.attach(9);  
  myservo.write(0);
  delay(2000);
  Serial.println("Potentiometer_voltage :Angle");
}

void loop() {
  potentiometer_value = analogRead(potentiometer_pin);     
  Serial.print(potentiometer_value );
  Serial.print("                     : ");
  servo_angle = map(potentiometer_value, 0, 1023, 0, 180);    
  myservo.write(servo_angle);               
  Serial.print(servo_angle);
  Serial.println();
  delay(100);              
}
 
