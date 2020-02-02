#define R1 2
#define R2 3
#define R3 4
#define R4 5
#define C1 6
#define C2 7
#define C3 8
#define C4 9

String s;
int v;

const byte rows[] = {R1,R2,R3,R4};//positive terminal
const byte columns[] = {C1,C2,C3,C4};//negative terminal

byte A[] = {B0110,B1001,B1111,B1001};
byte C[] = {B1111,B0001,B0001,B1111};
byte I[] = {B1111,B0110,B0110,B1111};
byte O[] = {B1111,B1001,B1001,B1111};
byte U[] = {B1001,B1001,B1001,B1111};
byte all_on[] = {B1111,B1111,B1111,B1111};
byte all_off[] = {B0000,B0000,B0000,B0000};

void  drawScreen(byte letter[])
 {
 
    for (byte i = 0; i < 4; i++)       
     {
        digitalWrite(rows[i], 0);   
        for (byte a = 0; a < 4; a++)  
        {
          v=((letter[i] >> a) & 0x01);

          digitalWrite(columns[a],v);
          delayMicroseconds(50); 
          digitalWrite(columns[a],0); 
        }  
      
        digitalWrite(rows[i], 1);
             
    }
   
}

void setup() 
{   
    Serial.begin(9600);
    for (byte i = 2; i <= 9; i++)
        pinMode(i, OUTPUT);     
   digitalWrite(C1, 0);
   digitalWrite(C2, 0);
   digitalWrite(C3, 0);
   digitalWrite(C4, 0); 
   digitalWrite(R1, 1);
   digitalWrite(R2, 1);
   digitalWrite(R3, 1);
   digitalWrite(R4, 1);    
}

void loop() {
if(Serial.available()!=0){
s=Serial.readString(); }
Serial.println(s);
switch(s[0])
{
case 'A':drawScreen(A);
         Serial.println("letter A is being displayed");
         break;
case 'C':drawScreen(C);
         Serial.println("letter C is being displayed");
         break;
case 'I':drawScreen(I);
         Serial.println("letter I is being displayed");
         break;
case 'O':drawScreen(O);
         Serial.println("letter O is being displayed");
      
         break;
case 'U':drawScreen(U);
         Serial.println("letter U is being displayed");
         break;
case 'b':drawScreen(all_on);
         delay(500);
         drawScreen(all_off);
         delay(250);
         drawScreen(all_on);
         delay(500);
         drawScreen(all_off);
         Serial.println("LED matrix blinks twice");
         break;}
             

}


  /* this is siplest resemplation how for loop is working with each row.
    digitalWrite(COL_1, (~b >> 0) & 0x01); // Get the 1st bit: 10000000
    digitalWrite(COL_2, (~b >> 1) & 0x01); // Get the 2nd bit: 01000000
    digitalWrite(COL_3, (~b >> 2) & 0x01); // Get the 3rd bit: 00100000
    digitalWrite(COL_4, (~b >> 3) & 0x01); // Get the 4th bit: 00010000
    digitalWrite(COL_5, (~b >> 4) & 0x01); // Get the 5th bit: 00001000
    digitalWrite(COL_6, (~b >> 5) & 0x01); // Get the 6th bit: 00000100
    digitalWrite(COL_7, (~b >> 6) & 0x01); // Get the 7th bit: 00000010
    digitalWrite(COL_8, (~b >> 7) & 0x01); // Get the 8th bit: 00000001
*/
