
int pin = 2;
int valDig;
float temp = 0;
 String valor;
 
void setup(){
  pinMode(pin, OUTPUT);
}
 
void loop(){
  Serial.begin(9600);
  
  valor = readSerialLine();
  
  digitalWrite(pin, valor=="teste da string" ? 1 : 0);
  Serial.end();

  delay(1000);
}


String readSerialLine(){
  String inData = "";
  char recieved;
  while (Serial.available() > 0 && recieved != '\n') {
    recieved = Serial.read();
    inData += recieved;
  }
  return inData;
}
