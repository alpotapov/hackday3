#include <SoftwareSerial.h>
SoftwareSerial vSerial(10, 11); // RX, TX

const int ledPin = 13;
const int lightPin = A0; 
const int calibrationTime = 1000;
const int calibrateMeasurmentCount = 10;
const int s = 500;

int avgLevel = 0;
int minLevel = 1024;
int maxLevel = 0;
int sensitivity = 1024;
void setup() {
	Serial.begin(9600);
	vSerial.begin(9600);  
	pinMode(ledPin, OUTPUT);
	calibrate();
}

void loop() {
	detectCoins();
}

void calibrate()
{
	vSerial.print("Calibration:");

	int light = analogRead(lightPin);
	int count = 1;
	avgLevel = light;
	for(int i=1;i<calibrateMeasurmentCount;i++)
	{  
		int light = analogRead(lightPin);
		minLevel = min(minLevel,light);
		maxLevel = max(maxLevel,light);
		avgLevel = avgLevel + light;
		count ++;
		delay(calibrationTime/calibrateMeasurmentCount);
	}
	avgLevel = avgLevel / count;
	vSerial.print("Avg:");
	vSerial.println(avgLevel);
	vSerial.print("Min:");
	vSerial.println(minLevel);
	vSerial.print("Min:");
	vSerial.println(maxLevel);
	sensitivity = (maxLevel - minLevel) / 2;
}

void detectCoins()
{
	int light = analogRead(lightPin);
	if(light<930)
	{
		digitalWrite(ledPin,LOW);
		vSerial.println("Coin");
		delay(1000);
		digitalWrite(ledPin,HIGH);
	}	
	vSerial.println(light);
	delay(100);
}





