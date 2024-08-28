# Object Detection with TensorFlow Lite

## Genel Bakış

Bu proje, TensorFlow'un önceden eğitilmiş modellerini ve OpenCV'yi kullanarak nesne tespiti göstermektedir. Script, bir webcam'den video alır, her bir kareyi nesne tespit modelinden geçirir ve tespit edilen nesneleri etiketleri ve sınırlayıcı kutularıyla birlikte görüntüler.

## Gereksinimler

- Python 3.x
- TensorFlow
- OpenCV
- Protobuf

## Kurulum

### 1. Bağımlılıkları Yükleyin

Gerekli Python paketlerini pip ile yükleyin:

```bash
pip install opencv-python
pip install tensorflow-object-detection-api
```

### 2. Protobuf Yükleyin

Belirli bir `protobuf` sürümünü yüklemeniz gerekebilir:

```bash
pip uninstall protobuf
pip install protobuf==3.20
```

### 3. Kütüphane ve Dosya Konumlarını Güncelleyin

Bu projede kullanılan yeni kütüphane `utils/label_map.py` dosyasının konumuyla birlikte yer değiştirilecektir. Lütfen aşağıdaki adımları takip edin:

1. **Kütüphane Dosyası Konumu**:
   - `utils/label_map.py` dosyasını mevcut proje dizininde uygun bir konuma taşıyın veya mevcut dosya yolunu güncelleyin.

2. **Model ve Etiket Haritasını İndirin**:
   - Önceden eğitilmiş model (`frozen_inference_graph.pb`) ve etiket haritası dosyasını (`mscoco_label_map.pbtxt`) indirin. Bu dosyaları TensorFlow Model Zoo'dan alabilir veya kendi dosyalarınızı kullanabilirsiniz.

### 4. Proje Yapısı

Proje dizininizin aşağıdaki dosyaları içerdiğinden emin olun:
- `frozen_inference_graph.pb`: Önceden eğitilmiş model dosyası.
- `mscoco_label_map.pbtxt`: Model için etiket haritası dosyası.
- `tf_galipolli.py`: Nesne tespiti gerçekleştiren script.

### 5. Script'i Çalıştırma

Script'i çalıştırmak için:

```bash
python tf_galipolli.py
```

Bu, webcam'inizden video akışını başlatır ve tespit edilen nesneleri gerçek zamanlı olarak görüntüler. Akıştan çıkmak için 'q' tuşuna basın.

## Kod Açıklaması

1. **Yolları Ayarla ve Modeli Yükle**:
   - Model ve etiket haritası dosyalarının yollarını tanımlayın.
   - TensorFlow modelini ve etiket haritasını yükleyin.

2. **Video Yakalamayı Başlat**:
   - Webcam'den video yakalamayı başlatın.

3. **Video Karelerini İşleme**:
   - Her kareyi nesne tespiti için işleyin.
   - Tespit edilen nesnelerin üzerine sınırlayıcı kutular ve etiketler çizin.

4. **Sonuçları Görüntüleme**:
   - İşlenmiş kareleri tespit edilen nesneler ve FPS ile birlikte görüntüleyin.

## Sorun Giderme

- Tüm bağımlılıkların doğru şekilde yüklendiğinden emin olun.
- Model ve etiket haritası dosyalarının yollarını doğrulayın.
- TensorFlow ve protobuf sürümlerinin uyumluluğunu kontrol edin.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.
