   /*
Pins  SPI    UNO  
1 (NSS) SAD (SS)   10  a  
2       SCK        13  ab 
3       MOSI       11  c  
4       MISO       12  cb 
5       IRQ        *   n   
6       GND       GND  nb  
7       RST        5   v   
8      +3.3V (VCC) 3V3 vb  
* Not needed
1 on ICPS header
*/

#include <RTClib.h>                 
#include <SoftwareSerial.h>
#include <MFRC522.h>
#include <SPI.h>
#include <Wire.h> 


#define SAD 10
#define RST 5
#define TARJETA 1 
#define LLAVE 1 
#define SalTr 4


RTC_DS1307 RTC;
MFRC522 nfc(SAD, RST);
//CLAVE DE LA TAJETA
byte Autorizado[TARJETA][6] = {{0x99, 0x36, 0x51, 0x35, 0xFF, 0xFF, }};
// CLAVE DEL LLAVERO
byte Autorizado2[LLAVE][6] = {{0xD4, 0xB3, 0x48, 0xCC, 0xFF, 0xFF, }}; 
void imprimeClave(byte *serial);
boolean esIgual(byte *key, byte *serial);
boolean chekaKey(byte *serial);

void setup() {
  SPI.begin();
   Serial.begin(9600);

Serial.println("BUSCANDO MFRC522.");
   byte version = nfc.getFirmwareVersion();
//   if (! version) {
//      Serial.print("NO SE ENCONTRO MFRC522 ");
//      while(1); //halt
//    }
   Serial.print("BUSCANDO CHIP MFRC522 ");
   Serial.print("FIRMWARE VERSION. 0x");
   Serial.print(version, HEX);
   Serial.println(".");
}

void loop() {
  // put your main code here, to run repeatedly:
 byte status;
  byte data[MAX_LEN];
  byte serial[5];

  status = nfc.requestTag(MF1_REQIDL, data);
  
  if (status == MI_OK) {
    status = nfc.antiCollision(data);
    memcpy(serial, data, 5);    
    if(chekaKey(serial)){ 
      Serial.println("AUTORIZADO");
       
      }else{ 
      Serial.println("NO AUTORIZADO");
      imprimeClave(serial);
      delay(200);
      //Open2 = false;
    }    
    nfc.haltTag();
  }
}


boolean esIgual(byte *key, byte *serial){
    for (int i = 0; i < 4; i++){
      if (key[i] != serial[i]){ 
        return false; 
      }
    }    
    return true;
  }

boolean chekaKey(byte *serial)
{
    for(int i = 0; i<TARJETA; i++)
    {
      if(esIgual(serial, Autorizado[i]))
        return true;
    }
      for(int i = 0; i<LLAVE; i++)
    {
      if(esIgual(serial, Autorizado2[i]))
        return true;
    }
   return false;
}

void imprimeClave(byte *serial)
{
    Serial.print("CLAVE: ");
    for (int i = 0; i < 4; i++) {
      Serial.print(serial[i], HEX);
      Serial.print(" ");
    }
    Serial.println("  ");
}
