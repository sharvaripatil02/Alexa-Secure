int inPin=4;
int val = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(inPin, INPUT);
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:
  val = digitalRead(inPin);  // read input value
  if (val == HIGH) {         // check if the input is HIGH (button released)
    Serial.println("Open");  // turn LED OFF
  } else {
    Serial.println("Close");  // turn LED ON
  }
}


