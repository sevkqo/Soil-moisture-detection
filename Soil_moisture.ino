int soil_moisture_1 = A0; //soil moisture sensor for plant no. 1
int soil_moisture_2 = A1; //soil moisture sensor for plant no. 2
int soil_moisture_3 = A3; //soil moisture sensor for plant no. 3
void setup() {
  Serial.begin(9600);        
  pinMode(2, OUTPUT);      //pin 2 - diode to inform to water plant no. 1
  pinMode(3, OUTPUT);      //pin 3 - diode to inform to water plant no. 2
  pinMode(4, OUTPUT);      //pin 4 - diode to inform to water plant no. 3
}
 
void loop() {
  int read_soil_moisture_1 = analogRead(soil_moisture_1);
  int read_soil_moisture_2 = analogRead(soil_moisture_2); 
  int read_soil_moisture_3 = analogRead(soil_moisture_3);
//  Serial.println("Soil moisture for plant no. 1: ");      
  Serial.print(read_soil_moisture_1);
  Serial.print("\t");
//  Serial.println();
//  Serial.println("Soil moisture for plant no. 2: ");
  Serial.print(read_soil_moisture_2);
  Serial.print("\t");
//  Serial.println("");
//  Serial.println("Soil moisture for plant no. 3: ");
  Serial.print(read_soil_moisture_3);
  Serial.println("");
//  Serial.println("");
  if (read_soil_moisture_1 > 500)            
  { 
    digitalWrite(2, HIGH);
  }
  else
  {
    digitalWrite(2, LOW);
  };
  if (read_soil_moisture_2 > 500)            
  { 
    digitalWrite(3, HIGH);
  }
  else
  {
    digitalWrite(3, LOW);
  };
  if (read_soil_moisture_3 > 500)            
  { 
    digitalWrite(4, HIGH);
  }
  else
  {
    digitalWrite(4, LOW);
  };
  delay(10000);
}
