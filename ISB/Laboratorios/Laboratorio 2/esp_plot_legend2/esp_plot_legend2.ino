/*************************************
 Course: ISB-UPCH
 Date: 05/04/2024
 Autor: Grupo 4
**************************************/

unsigned long lastMsg = 0;
float F=1;                      // 1 hz
double Fs = 10*F;               // 10 hz
double Ts_ms = (1/Fs)*1000;     //  100 ms  

void setup() {
  Serial.begin(9600);
  while (!Serial);
}

void loop() {

  unsigned long now = millis();

  if (now - lastMsg > Ts_ms) {
    
    lastMsg = now;

    int r2 = analogRead(A0);

    Serial.print("Señal2:");
    Serial.println(r2);
  }

}
