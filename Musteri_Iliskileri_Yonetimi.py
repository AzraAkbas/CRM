def destek_yonlendirme(musteri_talepleri, temsilciler):
    """
    Müşteri destek taleplerini şehir bazında uygun temsilcilere yönlendirir.

    T(n) ve O(n) Hesapları:
    -----------------------
    - M: Müşteri sayısı
    - N: Temsilci sayısı
    - Filtreleme işlemi: O(N)
    - Sıralama işlemi: O(N log N)
    - İç döngüde uygun temsilci arama: O(N)
    - remove() işlemi en kötü durumda O(N)
    - Toplam: O(M (N log N))

    En kötü durumda tüm müşteriler için temsilcileri kontrol ettiğimizden **O(MN log N)** zaman karmaşıklığına sahiptir.
    """

    eslesmeler = []

    for musteri_id, talep, musteri_sehir in musteri_talepleri:  # O(M)
        # 1. Şehir bazında temsilcileri filtrele (O(N))
        uygun_temsilciler = [t for t in temsilciler if t[2] == musteri_sehir]

        # 2. Temsilcileri uygunluk skoruna göre büyükten küçüğe sırala (O(N log N))
        uygun_temsilciler.sort(key=lambda x: x[1], reverse=True)

        for i, (temsilci_id, uygunluk, temsilci_sehir) in enumerate(uygun_temsilciler):  # O(N)
            if uygunluk >= talep:
                eslesmeler.append((musteri_id, temsilci_id, musteri_sehir))

                # 3. Atanan temsilciyi listeden kaldır (O(N))
                temsilciler.remove((temsilci_id, uygunluk, temsilci_sehir))
                break

    return eslesmeler  # Toplam: O(MN log N)


def pazarlama_optimizasyonu(kampanyalar, butce):
    """
    Pazarlama bütçesi dahilinde en iyi getiriyi sağlayacak kampanyaları seçer.

    T(n) ve O(n) Hesapları:
    -----------------------
    - n: Kampanya sayısı
    - B: Bütçe miktarı
    - DP tablosu oluşturma: O(nB)
    - DP hesaplama: O(nB)
    - Seçilen kampanyaları belirleme: O(n)
    - Toplam: O(nB)

    Bu algoritma, dinamik programlama kullanarak **0/1 Knapsack Problem** çözüyor.
    """

    n = len(kampanyalar)

    # 1. DP tablosu oluşturma (O(nB))
    dp = [[0] * (butce + 1) for _ in range(n + 1)]

    # 2. Dinamik programlama ile maksimum getiriyi hesaplama (O(nB))
    for i in range(1, n + 1):
        kampanya_id, maliyet, getiri = kampanyalar[i - 1]
        for b in range(butce + 1):
            if maliyet > b:
                dp[i][b] = dp[i - 1][b]  # Önceki değeri taşı (O(1))
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - maliyet] + getiri)  # Maksimum getiriyi seç (O(1))

    # 3. Seçilen kampanyaları belirleme (O(n))
    secilenler = []
    b = butce
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            kampanya_id, maliyet, _ = kampanyalar[i - 1]
            secilenler.append(kampanya_id)
            b -= maliyet

    return secilenler  # Toplam: O(nB)


def crm_sistemi():
    """
    CRM Sistemi: Müşteri Destek Yönlendirme + Pazarlama Optimizasyonu

    - Destek yönlendirme O(MN log N)
    - Pazarlama optimizasyonu O(nB)
    - Genel karmaşıklık: O(MN log N + nB)
    """

    print(" CRM Sistemi Başlatılıyor...\n")

    # Müşteri destek yönlendirme için giriş verileri
    musteriler = [
        (1, 3, "İstanbul"),
        (2, 5, "Ankara"),
        (3, 2, "İstanbul"),
        (4, 4, "İzmir")
    ]

    temsilciler = [
        (101, 4, "İstanbul"),
        (102, 5, "Ankara"),
        (103, 3, "İzmir"),
        (104, 2, "İstanbul")
    ]

    # Pazarlama kampanyaları için giriş verileri
    kampanyalar = [
        (1, 10, 60),  # (kampanya_id, maliyet, getiri)
        (2, 20, 100),
        (3, 30, 120),
        (4, 25, 80)
    ]
    butce = 50

    # Müşteri destek yönlendirme (O(MN log N))
    print(" Müşteri Destek Yönlendirme Sonuçları (Şehir Bazlı):")
    eslesmeler = destek_yonlendirme(musteriler, temsilciler)
    if eslesmeler:
        for musteri, temsilci, sehir in eslesmeler:
            print(f"Müşteri {musteri} ({sehir}) → Temsilci {temsilci} ({sehir})")
    else:
        print(" Eşleşme bulunamadı.")

    # Pazarlama optimizasyonu (O(nB))
    print("\n Pazarlama Kampanyası Seçimi (Maksimum ROI):")
    secilen_kampanyalar = pazarlama_optimizasyonu(kampanyalar, butce)
    if secilen_kampanyalar:
        print(f"Seçilen Kampanyalar: {secilen_kampanyalar}")
    else:
        print("Hiçbir kampanya seçilemedi (bütçe yetersiz).")

    print("\n CRM Sistemi Tamamlandı.")


if __name__ == "__main__":
    crm_sistemi()
