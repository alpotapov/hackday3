
int s = 500;
int ledPin = 13;
int lightPin = A0; 

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  Serial.println("Yo");
  int light = analogRead(lightPin);
  Serial.println(light);
  digitalWrite(ledPin,LOW);
  delay(s);
  digitalWrite(ledPin,HIGH);
  delay(s);
}


