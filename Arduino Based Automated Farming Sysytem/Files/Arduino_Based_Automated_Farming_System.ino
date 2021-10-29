#include<LiquidCrystal.h>
#define echo 9
#define trigger 10
#define water_tank_motor 4
#define water_pump 13
#define moisture_sensor A0

long duration;
int distance;
int moisture_value;
int water_level;
int moisture;
LiquidCrystal lcd(12,11,8,7,6,5);


void setup(){
lcd.begin(20,4);
Serial.begin(9600);
pinMode(echo,INPUT);
pinMode(moisture_sensor,INPUT);
pinMode(trigger,OUTPUT);
digitalWrite(trigger,LOW);
pinMode(water_pump,OUTPUT);
pinMode(water_tank_motor,OUTPUT);
digitalWrite(water_pump,LOW);
digitalWrite(water_tank_motor,LOW);
lcd.setCursor(0,1);
lcd.print("CSE360-FINAL PROJECT");
lcd.setCursor(0,2);
lcd.print("AUTOMATED FARMING");
lcd.setCursor(0,3);
lcd.print("GROUP-DEBUG ENTITY");
delay(700);
lcd.clear(); 
}


void loop(){
digitalWrite(trigger,LOW);
delayMicroseconds(2);
digitalWrite(trigger,HIGH);
delayMicroseconds(10); 
digitalWrite(trigger,LOW);
duration=pulseIn(echo,HIGH);
distance=duration*0.017; 
water_level=map( distance,0,1023,0,100);
moisture_value= analogRead(moisture_sensor);
moisture=map(moisture_value,0,1023,0,100);
condition();
}

void condition(){
if (water_level>50 && moisture<70){
LCD_3();
digitalWrite(water_tank_motor,LOW);
digitalWrite(water_pump,HIGH);
delay(500);
}
else if (water_level<50 &&moisture>70){
LCD_2();
digitalWrite(water_tank_motor,HIGH);
digitalWrite(water_pump,LOW);
delay(500);
}
else if (water_level>50 && moisture>70){
LCD_4();
digitalWrite(water_tank_motor,LOW);
digitalWrite(water_pump,LOW);
delay(500);
}
else if (water_level<50 && moisture<70){
LCD_1();
digitalWrite(water_tank_motor,HIGH);
digitalWrite(water_pump,HIGH);
delay(500);
}
}

void LCD_1(){
lcd.clear();
lcd.setCursor(0,0);
lcd.print("TANK LEVEL = ");
lcd.print(water_level);
lcd.print("%");
lcd.setCursor(0,1);
lcd.print("MOISTURE = ");
lcd.print(moisture);
lcd.print("%");
lcd.setCursor(0,2);
lcd.print("WATER-PUMP:");
lcd.print(" ON");
lcd.setCursor(0,3);
lcd.print("WATER-TANK-MOTOR:");
lcd.print(" ON");
}

void LCD_2(){
lcd.clear();
lcd.setCursor(0,0);
lcd.print("TANK LEVEL = ");
lcd.print(water_level);
lcd.print("%");
lcd.setCursor(0,1);
lcd.print("MOISTURE = ");
lcd.print(moisture);
lcd.print("%");
lcd.setCursor(0,2);
lcd.print("WATER-PUMP:");
lcd.print(" OFF");
lcd.setCursor(0,3);
lcd.print("WATER-TANK-MOTOR:");
lcd.print(" ON");
}

void LCD_3(){
lcd.clear();
lcd.setCursor(0,0);
lcd.print("TANK LEVEL = ");
lcd.print(water_level);
lcd.print("%");
lcd.setCursor(0,1);
lcd.print("MOISTURE = ");
lcd.print(moisture);
lcd.print("%");
lcd.setCursor(0,2);
lcd.print("WATER-PUMP:");
lcd.print(" ON");
lcd.setCursor(0,3);
lcd.print("WATER-TANK-MOTOR:");
lcd.print(" OFF");
}

void LCD_4(){
lcd.clear();
lcd.setCursor(0,0);
lcd.print("TANK LEVEL = ");
lcd.print(water_level);
lcd.print("%");
lcd.setCursor(0,1);
lcd.print("MOISTURE = ");
lcd.print(moisture);
lcd.print("%");
lcd.setCursor(0,2);
lcd.print("WATER-PUMP:");
lcd.print(" OFF");
lcd.setCursor(0,3);
lcd.print("WATER-TANK-MOTOR:");
lcd.print(" OFF");
}
