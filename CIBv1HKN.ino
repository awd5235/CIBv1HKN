/*
    Adam Dykhouse
    9/6/2017
    Pennsylvania State University
    Dept. of Physics

    CIBv1HKN
      This sketch allows the Arduino nano to take a select group of signals from the CIBv1 (via DB15 connector)
      and pass the integer DAC output values of each signal to a python program over serial USB every second.

    CIBv1 Signals     Arduino Pin       DB15 Pin
      VSUB                A0              7
      VDDA                A1              6
      VDD3P3              A2              13
      VDD2P5              A3              5
      VDDIO               A4              12
      TSENSE2             A5              11
      TSENSE              A6              3
      TSENSE0             A7              10
      F HEART BEAT        D13             1
*/

// Analog pin Declarations
const int VSUB    = A0;
const int VDDA    = A1;
const int VDD3P3  = A2;
const int VDD2P5  = A3;
const int VDDIO   = A4;
const int TSENSE2 = A5;
const int TSENSE  = A6;
const int TSENSE0 = A7;

// Digital pin declarations
const int FHEART = 13;

// Local variables
float vsub    = 0;
float vdda    = 0;
float vdd3p3  = 0;
float vdd2p5  = 0;
float vddio   = 0;
float tsense2 = 0;
float tsense  = 0;
float tsense0 = 0;
bool fheart = 0;

void setup()
{
  Serial.begin(9600);    // 9600 Baud Rate
  // Arduino pins initialize as inputs by default, no further initialization necessary.
}

void loop()
{
  // Read value for vsub (V)
  vsub = analogRead(VSUB);

  // Read value for vdda (V)
  vdda = analogRead(VDDA);

  // Read value for vdd3p3 (V)
  vdd3p3 = analogRead(VDD3P3);

  // Read value for vdd2p5 (V)
  vdd2p5 = analogRead(VDD2P5);

  // Read value for vddio (V)
  vddio = analogRead(VDDIO);

  // Read value for tsense2 (C)
  tsense2 = analogRead(TSENSE2);

  // Read value for tsense (C)
  tsense = analogRead(TSENSE);

  // Read value for tsense0 (C)
  tsense0 = analogRead(TSENSE0);

  // Read value for fheart
  fheart = digitalRead(fheart);

  // Print values to terminal
  Serial.print(vsub);
  Serial.print(" ");
  Serial.print(vdda);
  Serial.print(" ");
  Serial.print(vdd3p3);
  Serial.print(" ");
  Serial.print(vdd2p5);
  Serial.print(" ");
  Serial.print(vddio);
  Serial.print(" ");
  Serial.print(tsense2);
  Serial.print(" ");
  Serial.print(tsense);
  Serial.print(" ");
  Serial.print(tsense0);
  Serial.print(" ");
  Serial.print(fheart);
  Serial.print("\n");
 
  delay(1000); // delay half a second
}


