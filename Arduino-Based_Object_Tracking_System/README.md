# Arduino-Based Object Tracking System

## Author: Mustafa Yalınız

### Açıklama
Bu proje, bir webcam ve Arduino kullanarak gerçek zamanlı bir nesne takip sistemini içerir. Sistem, mavi renkli bir nesneyi tespit eder, nesnenin kameranın merkezine olan konumunu hesaplar ve bu konumsal veriyi bir Arduino'ya seri iletişim yoluyla gönderir. Arduino, bu veriyi işleyerek dört LED'in parlaklığını kontrol eder ve nesnenin X ve Y eksenlerindeki konumunu gösterir.






![Arduino](images/arduino_serial.gif)







### Bileşenler
- **Webcam**: Nesne tespiti için video akışını yakalar.
- **Arduino**: Konumsal veriyi alır ve LED'leri kontrol eder.
- **LED'ler**: Dört LED, nesnenin X ve Y eksenlerindeki konumunu gösterir.
- **Bilgisayar**: Görüntü işleme ve Arduino ile iletişim kurma için Python scriptini çalıştırır.

### Kurulum
1. **Yazılım Gereksinimleri**:
   - Python 3.x
   - Python için OpenCV kütüphanesi (`opencv-python`)
   - Python için imutils kütüphanesi (`imutils`)
   - Arduino kodu için Arduino IDE

2. **Donanım Gereksinimleri**:
   - Arduino kartı (örneğin, Arduino Uno)
   - 4 LED
   - LED'ler için uygun değerlerde dirençler
   - Jumper kablolar
   - Breadboard

### Kurulum
1. **Python Scripti**:
   - Gerekli Python kütüphanelerini yükleyin:
     ```bash
     pip install opencv-python imutils pyserial
     ```
   - Webcam'inizin OpenCV ile çalıştığından emin olun.
   - Python scriptindeki `port` değerini Arduino'nuzun bağlı olduğu porta (örneğin, `COM10`) göre güncelleyin.

2. **Arduino Devresi**:
   - LED'leri Arduino'nun dijital pinlerine 9, 10, 5 ve 6 bağlayın.
   - LED'lerin yanmasını önlemek için direnç kullanın.
   - Arduino'yu güç kaynağına bağlayın ve bağlantıların sağlam olduğundan emin olun.

3. **Arduino Kodunu Yükleme**:
   - Arduino IDE'yi açın.
   - Sağlanan Arduino kodunu kopyalayın.
   - Kodu derleyin ve Arduino'ya yükleyin.

### Projeyi Çalıştırma
1. Python scriptini çalıştırın:
   ```bash
   python object_tracking.py
   ```
   Script, video akışını yakalar, mavi nesneyi tespit eder ve konumsal veriyi Arduino'ya gönderir.

2. Arduino üzerindeki LED'leri gözlemleyin:
   - LED'ler, nesnenin kameranın merkezine olan konumuna göre yanacaktır.

### Özelleştirme
- **Renk Aralığı**:
  - Python scriptindeki `blue_low` ve `blue_high` değişkenlerini farklı renkleri takip etmek için değiştirin.
- **LED Kontrolü**:
  - Arduino kodundaki haritalama değerlerini LED parlaklık aralığını değiştirmek için ayarlayın.

### Sorun Giderme
- **Seri İletişim Yok**:
  - Python scriptinde doğru COM portunun belirtildiğinden emin olun.
  - Arduino'nun bilgisayara düzgün şekilde bağlandığını kontrol edin.

- **Nesne Tespit Edilemiyor**:
  - Nesnenin Python scriptinde belirtilen renk aralığında olduğundan emin olun.
  - Nesne tespitini iyileştirmek için aydınlatma koşullarını ayarlayın.

### Lisans
Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
