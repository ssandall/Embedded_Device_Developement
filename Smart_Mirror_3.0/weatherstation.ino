#include <ThingSpeak.h>

#include <Adafruit_DHT/Adafruit_DHT.h>

#define DHTPIN 2 

#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
TCPClient client;

unsigned long myChannelNumber = 502804;
const char * myWriteAPIKey = "BTCK7H1060DMR1ZB";

void setup() {
Serial.begin(9600);
dht.begin();
ThingSpeak.begin(client);
}

void loop() {

delay(2000);

//Variables
//DHT11 sensor floats
float h = dht.getHumidity();
float t = dht.getTempCelcius();
float f = dht.getTempFarenheit();
float hi = dht.getHeatIndex();
//UV sensor floats
float sensorValue = analogRead(A0);
int UVLevel = 0;

//Error Retry
    if (isnan(h) || isnan(t) || isnan(f)) 
    {
        Serial.println("Failed to read from DHT sensor!");
        return;
    }

    if (sensorValue <= 10)
        UVLevel = 0;
    else if (sensorValue <= 46)
        UVLevel = 1;
    else if (sensorValue <= 65)
        UVLevel = 2;
    else if (sensorValue <= 83)
        UVLevel = 3;
    else if (sensorValue <= 103)
        UVLevel = 4;
    else if (sensorValue <= 124)
        UVLevel = 5;
    else if (sensorValue <= 142)
        UVLevel = 6;
    else if (sensorValue <= 162)
        UVLevel = 7;
    else if (sensorValue <= 180)
        UVLevel = 8;
    else if (sensorValue <= 200)
        UVLevel = 9;
    else if (sensorValue <= 221)
        UVLevel = 10;
    else if (sensorValue <= 240)
        UVLevel = 11;
    else if (sensorValue > 240)
        UVLevel = 12;

//Serial Sensor Testing
//Uncomment To test
//Serial Print DHT
/*
Serial.println();
Serial.println();
Serial.print("Humid: ");
Serial.print(h);
Serial.print("%");
Serial.println();
Serial.print("Temp: ");
Serial.print(t);
Serial.print("C ");
Serial.println();
Serial.print("Apparent Temperature: ");
Serial.print(hi);
Serial.println();
Serial.println();

//Serial Print UV
Serial.print("UV Level =");
Serial.print(UVLevel);
Serial.println();
*/

//Publish Data To ThingSpeak
ThingSpeak.setField(1,t);
ThingSpeak.setField(2,h);
ThingSpeak.setField(3,UVLevel);
ThingSpeak.setField(4,hi);

ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey); 
delay(20000);

}
