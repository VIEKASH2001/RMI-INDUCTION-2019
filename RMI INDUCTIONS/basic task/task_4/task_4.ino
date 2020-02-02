#include <TimerOne.h>
float f,t,val;
void setup() {
  pinMode(9,OUTPUT);
  pinMode(3,INPUT);
  pinMode(A1,INPUT);
  Timer1.initialize(1000000);  //Initialize Timer1 and set period as 1 second
  Timer1.pwm(9,511);    //Initialize PWM in pin 9, set 50% dutyCycle
  f=38000;
  t=1/f;
  Timer1.setPeriod(t*1000000);
  Serial.begin(9600);  
  
 }
void loop() {
    //val=digitalRead(A1);
    
    if(digitalRead(3)==1)
    {
     Timer1.setPwmDuty(9,511); 
     Serial.println(digitalRead(A1));
      }
    else
    {
      Timer1.setPwmDuty(9,0);
      Serial.println(digitalRead(A1));
     
      } 
 }
