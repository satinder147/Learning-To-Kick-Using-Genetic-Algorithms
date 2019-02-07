#include<Servo.h>
Servo a_1,a_2,b_1,b_2,c_1,c_2,d_1,d_2;
int r;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
a_1.attach(2);
a_2.attach(3);
b_1.attach(4);
b_2.attach(5);
c_1.attach(6);
c_2.attach(7);
d_1.attach(8);
d_2.attach(9);

a_1.write(70);
delay(500);
a_2.write(60);
delay(500);
b_1.write(70);
delay(500);
b_2.write(60);
delay(500);
c_1.write(70);
delay(500);
c_2.write(60);
delay(500);
d_1.write(70);
delay(500);
d_2.write(60);
delay(500);
}

void loop() {
  
  // put your main code here, to run repeatedly:
if(Serial.available()>0)
{
  r=Serial.read();
    int x=int(r);
    int motor=x%10;
    x=x/10;
    x=x*5;

    switch(motor)
    {
      case 0:
        a_1.write(x+60);
        delay(500);
        //Serial.println("got it");
        break;
      case 1:
        a_2.write(x);
        delay(500);
        break;

      case 2:
        b_1.write(x+60);
        delay(500);
        break;

      case 3:
        b_2.write(x);
        delay(500);
        break;

      case 4:
        c_1.write(x+60);
        delay(500);
        break;

      case 5:
        c_2.write(x);
        delay(500);
        break;
      case 6:
        d_1.write(x);
        delay(500);
        break;
      case 7:
        d_2.write(x+60);
        delay(500);
        break;
      case 9:
      bringBack();
      break;
      
      
      }
    //String s="moving motor "+String(motor)+"at angle "+String(x);
    //Serial.println(s);
 
  //a_1.write(120);
  //delay(500);
  
 
  }
}


void bringBack()
{
  a_1.write(70);
delay(500);
a_2.write(60);
delay(500);
b_1.write(70);
delay(500);
b_2.write(60);
delay(500);
c_1.write(70);
delay(500);
c_2.write(60);
delay(500);
d_1.write(70);
delay(500);
d_2.write(60);
delay(500);
  }
