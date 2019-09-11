import bluetooth

define BT_TX 2
define BT_RX 3

SoftwareSerial BT(BT_TX, BT_RX);

void setup(){
  Serial.begin(9600);
  BT.begin(9600);
}

void loop(){
  if (BT.available()){
    Serial.write(BT.read());
  }

  if(Serial.available()){
    BT.write(Serial.read());
  }

}