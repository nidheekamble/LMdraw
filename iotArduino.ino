/*
 * Program for gesture control VLC Player
 * Controlled uisng Python
 * Code by B.Aswinth Raj
 * Dated: 11-10-2017
 * Website: www.circuitdigest.com
 */
int ledPin = 7;
const int sensor=A1; // Assigning analog pin A1 to variable 'sensor'
float tempc;  //variable to store temperature in degree Celsius
float tempf;  //variable to store temperature in Fahreinheit 
float vout;  //temporary variable to hold sensor reading

void setup() {
  Serial.begin(9600); 
  pinMode(sensor,INPUT); // Configuring pin A1 as input
  pinMode(ledPin, OUTPUT);
}

void loop() { //infinite loop
  vout=analogRead(sensor);
  vout=(vout*500)/1023;
  tempc=vout; // Storing value in Degree Celsius
  
  if (tempc>30)
  {
    Serial.println("high");
  }
  else
  {
    Serial.println("low");
  }   

   delay (2000);
}
