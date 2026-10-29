import cv2
import numpy as np
import os

image_path = "/Users/korkuteryigit/Documents/MadeniParaTespit/gorsel/paralar.png"
output_path = "/Users/korkuteryigit/Documents/MadeniParaTespit/outputs/output.png"
img = cv2.imread(image_path)

if img is None:
    print("Görsel yüklenemedi")
    exit()

# Görseli gri tonlara çevirme
grilestirme = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görseli blurlaştırma
blur = cv2.GaussianBlur(grilestirme, (11, 11), 0)

# Daire tespiti
daireler = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1.2,         # Çözünürlük tespiti
    minDist=30,     # Mesafe algulama
    param1=50,      # Kenar algılama hassasiyeti
    param2=35,      # Daire olma eşik değeri
    minRadius=15,   # En küçük para yarıçapı
    maxRadius=60    # En büyük para yarıçapı
)

if daireler is not None:

    daireler = np.uint16(np.around(daireler))
    toplam_para = len(daireler[0])
    print(f"Toplam {toplam_para} adet para tespit edildi.")

    for i in daireler[0, :]:
        x, y, r = i[0], i[1], i[2] # x ve ye merkez koordinat r yarıçap

        cv2.circle(img, (x, y), r, (0, 255, 0), 2) # Daireyi çiz

        cv2.circle(img, (x, y), 2, (0, 0, 255), 3) # Merkez noktası

    cv2.imwrite(output_path, img) # Görseli kaydet
    print(f"Görsel kaydedildi: {output_path}")

    cv2.imshow("Tespit Edilen Paralar", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Daire tespit edilemedi.")

