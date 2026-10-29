import cv2
import numpy as np

def paraları_tespit_et(gorsel):
    # Görseli gri tonlara çevirme
    grilestirme = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)

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

    return daireler

def sonuclari_cizdirme_sayma(gorsel, daireler):

    islenmis_gorsel = gorsel.copy()

    # Daire koordinatlarını tamsayıya yuvarla
    daireler = np.uint16(np.around(daireler))
    toplam_para = len(daireler[0])
    for i in daireler[0, :]:
        x, y, r = i[0], i[1], i[2]
        # Dış çemberi çiz (Yeşil: (0, 255, 0), Kalınlık: 2)
        cv2.circle(islenmis_gorsel, (x, y), r, (0, 255, 0), 2)
        # Merkez noktasını çiz (Kırmızı: (0, 0, 255), Kalınlık: 3)
        cv2.circle(islenmis_gorsel, (x, y), 2, (0, 0, 255), 3)
    return islenmis_gorsel, toplam_para