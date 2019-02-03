#include<Servo.h>
Servo x;
int r;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
x.attach(3);
}

void loop() {
  
  // put your main code here, to run repeatedly:
if(Serial.available()>0)
{
  r=Serial.read();
 
    Serial.println(int(r));
    x.write(int(r));
  delay(500);
 
  
 
  }
}
