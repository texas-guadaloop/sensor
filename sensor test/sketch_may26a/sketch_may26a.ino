
#define g_to_ms2 9.80665
#define adc_resolution 1024
#define max_adc_voltage 5
#define milli 0.001
#define BIAS 408

int analogPin = 3;     // potentiometer wiper (middle terminal) connected to analog pin 3

                       // outside leads to ground and +5V

int a = 0;           // variable to store the value read
int delay_milli = 1;   // number of milliseconds to wait
float milli_count = 0;
float xNaut = 0.0;
float vNaut = 0.0;



void setup()

{

  Serial.begin(9600);          //  setup serial

}



void loop()

{
  a = analogRead(analogPin);    // read the input pin
  //Serial.println(a);
  a =  a - BIAS;
  float a_in_g = ((float) a / adc_resolution) * max_adc_voltage;
  float a_in_ms2 = a_in_g * g_to_ms2;
  float v = vNaut + a_in_ms2 * milli;
  float x = xNaut + vNaut * milli;
  Serial.println(v);
  vNaut = v;
  xNaut = x;
  delay(delay_milli);
}

