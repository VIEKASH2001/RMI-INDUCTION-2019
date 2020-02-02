#define enA 9
#define in1 6
#define in2 7
#define trig 3
#define echo 4

long duration, distance, analog_input, Motor_speed;

void setup() 
{
  Serial.begin(9600); 
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  digitalWrite(in1, 0);
  digitalWrite(in2, 1);
  Serial.println("distance in CM : motor speed");
}

void loop() {
  digitalWrite(trig,HIGH);
  delayMicroseconds(1000);
  digitalWrite(trig, LOW);
  duration=pulseIn(echo, HIGH);
  distance =(duration*0.034/2);
  Serial.print(distance);
  Serial.print("             : ");
  delay(10);
  analog_input=map(distance, 0, 10, 0 , 255); // an assumption is taken here that maximum distance is 10 CM
  analog_input=analog_input*3;//this is done so that to have the speed a bit high so that the rotation is noticible in the video for shorter distances
  analogWrite(enA,analog_input);
  Motor_speed=map(analog_input, 0, 255, 0 , 300); 
  Serial.println(Motor_speed); 
} 
