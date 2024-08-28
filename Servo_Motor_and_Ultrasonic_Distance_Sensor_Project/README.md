# Servo Motor and Ultrasonic Distance Sensor Project

Bu proje, bir servo motor ve ultrasonik mesafe sensörü kullanarak çevredeki nesneleri tespit eden bir sistemdir. Sistem, nesneleri tespit etmek için bir ultrasonik sensör kullanır ve nesne bulunduğunda bir buzzer'ı aktif hale getirir. Ayrıca, tespit edilen mesafeyi seri port üzerinden yazdırır.

## Gereksinimler

- Arduino veya uyumlu bir mikrodenetleyici
- Servo Motor
- Ultrasonik Mesafe Sensörü (HC-SR04)
- Buzzer
- Bağlantı kabloları
- Arduino IDE

## Bağlantılar

1. **Servo Motor:**
   - Sinyal pini: Arduino'nun dijital 9 numaralı pini
   - Güç pini: Arduino'nun 5V pini
   - Toprak pini: Arduino'nun GND pini

2. **Ultrasonik Sensör (HC-SR04):**
   - VCC: Arduino'nun 5V pini
   - GND: Arduino'nun GND pini
   - Trig: Arduino'nun dijital 7 numaralı pini
   - Echo: Arduino'nun dijital 6 numaralı pini

3. **Buzzer:**
   - Pozitif pin: Arduino'nun dijital 10 numaralı pini
   - Negatif pin: Arduino'nun GND pini

## Kod Açıklaması

- **setup() Fonksiyonu:**
  - Seri port iletişimini başlatır.
  - Servo motoru, dijital 9 numaralı pin üzerinden kontrol eder.
  - Trig pini (mesafe ölçümü için sinyal gönderir) ve Echo pini (mesafe ölçümü için sinyal alır) yapılandırılır.
  - Buzzer yapılandırılır.

- **loop() Fonksiyonu:**
  - Servo motoru 0 derece ile 180 derece arasında döndürür ve mesafeyi ölçer.
  - Nesne bulunduğunda buzzer'ı aktive eder ve mesafeyi günceller.
  - Servo motoru tekrar 180 dereceden 0 dereceye geri döner ve aynı işlemi tekrarlar.

## Kullanım

1. Arduino IDE'yi açın ve yukarıdaki kodu yeni bir dosyaya yapıştırın.
2. Arduino'nuzu bilgisayara bağlayın ve uygun kart ve port seçimini yapın.
3. Kodu Arduino'nuza yükleyin.
4. Seri port monitörünü açarak mesafeleri ve nesne tespitlerini izleyin.

## Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için lütfen LICENSE dosyasına bakınız.

## Author

Mustafa Yalınız

