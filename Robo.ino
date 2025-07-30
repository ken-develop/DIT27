#include "CytronMotorDriver.h"
CytronMD motorL(PWM_PWM,3,9);
CytronMD motorR(PWM_PWM,10,11);
void setup() {
  pinMode(2,INPUT_PULLUP);
  while(digitalRead(2)== HIGH);
  delay(100);
  tone(8,392,125);  delay(325); 
  delay(1000);

  forward(); delay(2000);
  stops();delay(1000);

}

void loop() { 

}

void forward(){
  motorL.setSpeed(160);
  motorR.setSpeed(180);
  }
void stops(){
  motorL.setSpeed(0);
  motorR.setSpeed(0);
  }
void TL(){
  motorL.setSpeed(-150);
  motorR.setSpeed(150);
  }

void TR(){
  motorL.setSpeed(150);
  motorR.setSpeed(-150);
  }
