# Object Detection with TensorFlow Lite (Android Figure and TPU Support)

Bu proje, OpenCV kullanarak TensorFlow Lite nesne tespiti modelini çalıştırmayı sağlar. Bu model, özellikle Android figürü üzerine eğitilmiştir ve gerçek zamanlı nesne tespiti için kullanılabilir. Ayrıca, TPU (Tensor İşleme Birimi) desteği de mevcuttur.

## Kurulum

1. **Gerekli Python Kütüphanelerini Yükleyin:**

   Python 3.x yüklü olduğundan emin olun. Ardından, gerekli kütüphaneleri pip kullanarak yükleyin:

   ```bash
   pip install tensorflow opencv-python protobuf==3.20.*
   ```

## Nesne Tespitini Çalıştırma

1. **Modelinizi ve Etiketlerinizi Yerleştirin:**

   - **Model:** TensorFlow Lite modelinizi (`.tflite` dosyası) `custom_model_lite` klasörüne yerleştirin. Bu model, Android figürünü tespit etmek üzere eğitilmiştir.
   - **Etiketler:** Android figürüne dair etiketlerin bulunduğu `labelmap.txt` dosyasını aynı klasöre yerleştirin.

   Klasör yapısı şu şekilde olmalıdır:

   ```
   custom_model_lite/
   ├── detect.tflite
   └── labelmap.txt
   ```

2. **Betik Çalıştırma:**

   Nesne tespiti betiğini aşağıdaki komutla çalıştırabilirsiniz:

   ```bash
   python detect_objects.py --threshold 0.5 --resolution 1280x720 --edgetpu
   ```

   - `--threshold`: Tespit edilen nesnelerin gösterilmesi için minimum güven eşiğini ayarlar.
   - `--resolution`: İstenilen web kamerası çözünürlüğünü WxH formatında girin (örneğin, `1280x720`).
   - `--edgetpu`: Coral Edge TPU Hızlandırıcısını kullanın (isteğe bağlı).

3. **Programdan Çıkış:**

   Nesne tespiti penceresinden çıkmak için `q` tuşuna basın.

## TPU ve Android Figürü

- **TPU (Tensor İşleme Birimi):** Eğer TPU kullanıyorsanız, betiği çalıştırmadan önce cihazınızın doğru bir şekilde kurulduğundan emin olun.
- **Android Figürü:** Bu model, Android figürünü tespit etmek üzere eğitilmiştir.

## Notlar

- Bu betik, bir web kamerası akışı ile çalışacak şekilde tasarlanmıştır. Web kameranızın düzgün bir şekilde bağlandığından emin olun.
- Coral Edge TPU kullanıyorsanız, doğru bir şekilde kurulduğundan ve makinenize bağlı olduğundan emin olun.

## Sorun Giderme

- **Model Yükleme Sorunları:** Model dosyasının doğru bir şekilde adlandırıldığından (`detect.tflite`) emin olun.
- **Etiket Dosyası Sorunları:** `labelmap.txt` dosyasının doğru formatlandığından ve her satırda bir etiket bulunduğundan emin olun.
