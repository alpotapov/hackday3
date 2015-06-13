int s = 500;
int led1 = 13;

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
}

void loop() {
  Serial.println("Yo");
  digitalWrite(led1,LOW);
  delay(s);
  digitalWrite(led1,HIGH);
  delay(s);
}


