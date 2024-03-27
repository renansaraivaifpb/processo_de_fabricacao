const int pinSensorUmidade = A0;
//int valorumidade;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pinSensorUmidade, INPUT);
  
}

void loop() {
  //float data_input = Serial.read();
  // put your main code here, to run repeatedly:
  Serial.println(analogRead(pinSensorUmidade));
  //float data = analogRead(pinSensorUmidade);
  valorumidade = map(data, 1023, 0, 0, 100); 
  //String dataToSend = String(valorumidade);
  //Serial.println((String)dataToSend+", "+(String)data);
  //Serial.println(4.8);
  delay(300);
}
