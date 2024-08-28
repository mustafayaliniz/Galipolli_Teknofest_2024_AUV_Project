# YOLO Object Detection with Custom Circle Figure

Bu proje, özel bir daire figürü üzerinde eğitilmiş bir YOLO modeli kullanarak gerçek zamanlı nesne tespiti yapmaktadır.

## Gereksinimler

- Python 3.x
- OpenCV
- Ultralytics YOLO
- Özel YOLO modeli (`best.pt`)

## Kurulum

```bash
pip install opencv-python
pip install ultralytics
```

## Kullanım

Gerçek zamanlı nesne tespitine başlamak için script'i çalıştırın:

```bash
python detect.py
```

Bu script, web kameranızdan görüntü alır, gerçek zamanlı olarak özel daire figürünü tespit eder ve sonuçları sınır kutuları ile gösterir.

## Temel Özellikler

- Web kamerası ile gerçek zamanlı tespit
- Daire figürü üzerinde eğitilmiş özel YOLO modeli

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.