# Madeni Para Tespiti ve Sayma

Bu projeyi Python Programlama dersi için hazırladım. Projenin amacı, verilen bir fotoğraftaki madeni paraları OpenCV kullanarak tespit etmek ve toplam kaç tane para olduğunu saymaktır.

## Nasıl Çalışıyor?

Projede geleneksel görüntü işleme adımlarını kullandım:
1. Görsel yüklenip `cv2.cvtColor` ile gri tonlara çevriliyor.
2. Paranın üstündeki desenler ve ışık parlamaları kenar tespitini yanıltmasın diye `cv2.GaussianBlur` ile hafif bir bulanıklaştırma yapılıyor.
3. Yuvarlak nesneleri bulmak için OpenCV'nin `HoughCircles` fonksiyonu kullanılıyor.
4. Tespit edilen paraların etrafına yeşil çember, merkezine kırmızı nokta çizilip çıktı `outputs/` klasörüne kaydediliyor.

Kodların düzenli olması için projeyi ikiye böldüm:
- `para_tespit.py`: Görseli işleyen ve paraları bulan fonksiyonlar burada yer alıyor.
- `main.py`: Projeyi başlatan, resmi yükleyip fonksiyonları çağıran ana dosya.

## Çalıştırma

Gerekli kütüphaneleri yüklemek için:
```bash
pip install -r requirements.txt
```

Programı çalıştırmak için:
```bash
python main.py
```

Geliştirici: Korkut Eryiğit