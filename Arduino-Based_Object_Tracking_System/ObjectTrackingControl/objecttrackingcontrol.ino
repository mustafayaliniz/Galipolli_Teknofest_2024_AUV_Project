String goruntu;
int a, b; 
const int x1 = 9;
const int x2 = 10;
const int y1 = 5;
const int y2 = 6;
int isik = 0; 
void setup() {
  Serial.begin(9600);
}

/*
@author: MUSTAFA YALINIZ
*/

void loop() {
  if(Serial.available()){
    goruntu = Serial.readStringUntil('\n');
    int commaIndex = goruntu.indexOf(',');
    a = goruntu.substring(0, commaIndex).toInt();
    b = goruntu.substring(commaIndex + 1).toInt();
    Serial.print("X: ");
    Serial.print(a);
    Serial.print(", Y: ");
    Serial.println(b);
    if(a<=540&&a>0){
      isik = map(a, 0, 540, 0, 255); 
      analogWrite(x1, isik); 
      analogWrite(x2,0);
    }
    if(a<0&&a>=-540){
      isik = map(a, -540, 0, 255, 0); 
      analogWrite(x2, isik); 
      analogWrite(x1,0);
    }
    if(b<=405&&a>0){
      isik = map(b, 0, 405, 0, 255); 
      analogWrite(y1, isik); 
      analogWrite(y2,0);
     }
    if(b<0&&b>=-405){
      isik = map(b, -405, 0, 255, 0); 
      analogWrite(y2, isik); 
      analogWrite(y1,0);
    }
    
              
  }
}

