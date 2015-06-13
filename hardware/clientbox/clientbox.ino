#include <SoftwareSerial.h>
SoftwareSerial vSerial(10, 11); // RX, TX

const int ledPin = 12;
const int lightPin = 13;
const int sensorPin = A0; 
int measureTime = 3000;
const int measureCount = 5;

int level = 250;
int lightLevel = 950;
int coinLevel = 890;
int sensitivity = (lightLevel-coinLevel)/2;
long unsigned int t = 0;  
long int duration = 0;
int timePast = 0;

void setup() {
	Serial.begin(9600);
	vSerial.begin(9600);  
	pinMode(ledPin, OUTPUT);
	calibrate();
}

void loop() {
	timePast++;  
	detectCoins();
	if(timePast > 2)
	{
		timePast=0;
		processLight();
	}
	//delay(10);
}

void calibrate()
{
	vSerial.println("Calibration:");
	lightLevel = readAVG();
	vSerial.println(lightLevel);
	vSerial.println("Put a coint and wait a second:");
	delay(1000);
	vSerial.print("...");
	coinLevel = readAVG();
	vSerial.println(coinLevel);
	vSerial.println("Ok.");
	sensitivity =  50;//(lightLevel-coinLevel)/2;
	vSerial.print("sensitivity");
	vSerial.println(sensitivity);
	measureTime = 100;
}

void processLight()
{
	level-=2;
	if(level<5) level = 5;
	analogWrite(lightPin,level);
	//vSerial.print("Light ");
	//vSerial.println(level);
}

void lightUP()
{
	level+=50;
	if(level>250) level = 250;
}

void detectCoins()
{
	duration--;
	if(duration<0) 
	{duration = 0;}
	int light = readAVG();

	if(light<(lightLevel-sensitivity) && duration == 0)
	{
		duration = 10;
		digitalWrite(ledPin,LOW);
		vSerial.println("Coin!");
		lightUP();
		digitalWrite(ledPin,HIGH);
	}
	Serial.print(duration);
	//vSerial.print(" ");
	//vSerial.println(light);
}

int readAVG()
{
	int count = 0;
	int result = 0;
	for(int i=1;i<measureCount;i++)
	{  
		result = result + analogRead(sensorPin);;
		count ++;
		delay(measureTime/measureCount);
	}
	return result / count;
}





