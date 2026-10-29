import cv2
from para_tespit import paraları_tespit_et, sonuclari_cizdirme_sayma

def main():
    gorsel_yolu = "/Users/korkuteryigit/Documents/MadeniParaTespit/gorsel/paralar.png"
    cikti_yolu = "/Users/korkuteryigit/Documents/MadeniParaTespit/cikti/cikti.png"

    gorsel = cv2.imread(gorsel_yolu)
    if gorsel is None:
        print("Görsel yüklenemedi. Görseli kontrol et.")
        return

    daireler = paraları_tespit_et(gorsel)

    if daireler is not None:

        islenmis_gorsel, toplam_para = sonuclari_cizdirme_sayma(gorsel, daireler)

        print(f"Başarılı! Toplam {toplam_para} adet madeni para tespit edildi.")

        # Görseli outputs klasörüne kaydet
        cv2.imwrite(cikti_yolu, islenmis_gorsel)

        print(f"Sonuç görseli kaydedildi: {cikti_yolu}")
        
        # Ekranda göster
        cv2.imshow("Tespit Edilen Paralar", islenmis_gorsel)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Görselde herhangi bir madeni para tespit edilemedi.")


if __name__ == "__main__":
    main()