# CRM

# Proje Açıklaması
Bu CRM sistemi, müşteri destek taleplerini şehir bazında en uygun temsilciye yönlendirirken, pazarlama bütçesini en yüksek getiriyi sağlayacak kampanyalara ayıran iki temel işlevi birleştirir. Destek yönlendirme algoritması, müşterilerin şehirlerindeki en uygun temsilciyi seçip atama yaparken, pazarlama optimizasyonu dinamik programlama kullanarak bütçeyi en verimli şekilde kullanmayı amaçlayan 0/1 Knapsack Problem çözümünü uygular. Böylece sistem, hem müşteri memnuniyetini artırırken hem de pazarlama kaynaklarını en iyi şekilde değerlendirir.

# Kullanılan Yöntemler

Müşteri Destek Yönlendirme

Müşterinin bulunduğu şehirdeki temsilciler filtrelenir.

Temsilciler uygunluk skorlarına göre sıralanır.

Talebi karşılayan en uygun temsilci seçilir.

Pazarlama Optimizasyonu

0/1 Knapsack Problemi çözümü için dinamik programlama yöntemi kullanılır.

Kampanya maliyet ve getirilerine göre en iyi seçim yapılır.

# Algoritma Karmaşıklık Analizi

1. Müşteri Destek Yönlendirme

T(n) ve O(n) Hesapları:

Müşteri sayısı: M, Temsilci sayısı: N

Şehir bazında temsilci filtreleme → O(N)

Temsilcileri uygunluk skoruna göre sıralama → O(N log N)

En uygun temsilciyi seçme → O(N)

Temsilci listesinden çıkarma → O(N)

🔹 Toplam karmaşıklık: O(MN log N)

2. Pazarlama Optimizasyonu

T(n) ve O(n) Hesapları:

Kampanya sayısı: n, Bütçe: B

DP tablosu oluşturma → O(nB)

Maksimum getiri hesaplama (Dinamik Programlama) → O(nB)

Seçilen kampanyaları belirleme → O(n)

🔹 Toplam karmaşıklık: O(nB)

