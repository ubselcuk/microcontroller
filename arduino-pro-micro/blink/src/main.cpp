#include <Arduino.h>
#define BoardLed 17

void setup() {
  pinMode(BoardLed, OUTPUT);
}

void loop() {
  digitalWrite(BoardLed,LOW);
  delay(1000);
  digitalWrite(BoardLed,HIGH);
  delay(1000);
}