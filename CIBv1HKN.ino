/*
    Adam Dykhouse
    6/30/2017
    Pennsylvania State University
    Dept. of Physics

    CIBv1HKN
      This sketch allows the Arduino nano to take a select group of signals from the CIBv1 (via DB15 connector)
      and print the values of each signal to a console or terminal once every half a second (via USB) for monitoring.

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
  Serial.print("VSUB    VDDA    VDD3P3   VDD2P5  VDDIO   TSENSE2  TSENSE  TSENSE0  FHEART\n");     // Print header with variable names one time.
  // Arduino pins initialize as inputs by default, no further initialization necessary.
}

void loop() 
{
  // Read and determine decimal value for vsub
  vsub = analogRead(VSUB);
  vsub = (vsub*5)/1024;

  // Read and determine decimal value for vdda
  vdda = analogRead(VDDA);
  vdda = (vdda*5)/1024;

  // Read and determine decimal value for vdd3p3
  vdd3p3 = analogRead(VDD3P3);
  vdd3p3 = (vdd3p3*5)/1024;
  
  // Read and determine decimal value for vdd2p5
  vdd2p5 = analogRead(VDD2P5);
  vdd2p5 = (vdd2p5*5)/1024;

  // Read and determine decimal value for vddio
  vddio = analogRead(VDDIO);
  vddio = (vddio*5)/1024;
  
  // Read and determine decimal value for tsense2
  tsense2 = analogRead(TSENSE2);
  tsense2 = (((tsense2*5)/1024)-0.5)*100;
  
  // Read and determine decimal value for tsense
  tsense = analogRead(TSENSE);
  tsense = (((tsense*5)/1024)-0.5)*100;
  
  // Read and determine decimal value for tsense0
  tsense0 = analogRead(TSENSE0);
  tsense0 = (((tsense0*5)/1024)-0.5)*100;
  
  // Read value for fheart
  fheart = digitalRead(fheart);

  // Print values to terminal
  Serial.print(vsub);
  Serial.print("    ");
  Serial.print(vdda);
  Serial.print("    ");
  Serial.print(vdd3p3);
  Serial.print("     ");
  Serial.print(vdd2p5);
  Serial.print("    ");
  Serial.print(vddio);
  Serial.print("    ");
  Serial.print(tsense2);
  Serial.print("    ");
  Serial.print(tsense);
  Serial.print("   ");
  Serial.print(tsense0);
  Serial.print("    ");
  Serial.print(fheart);
  Serial.print("\n");
  
  delay(500); // delay half a second
}


