CSE101 Dönem Ödevi - Kütüphane Yönetim Sistemi
 Bu proje kütüphane işlerini kolaylaştırmak için Python ile yazıldı. Proje temel olarak kitapları, üyeleri ve kitap alıp-verme olaylarını takip ediyor.

Nasıl Çalıştırılır?
Bilgisayarda Python varsa direkt main.py dosyasını çalıştırmanız yeterli. Veriler için data/ klasörü lazım ama kodda otomatik oluşturma kısmı var, yoksa da kendisi açıyor.

Dosyalar Ne İşe Yarıyor? 

main.py: Programın giriş kapısı, bütün menüler ve ekranlar burada.

catalog.py: Kitap ekleme, silme, arama ve filtreleme işlerine bakıyor.

patron.py: Üyelerin kayıt olması, login işlemleri ve borç takibi burada.

circulation.py: Kitap ödünç alma, iade etme ve gecikme cezası hesaplama mantığı burada dönüyor.


storage.py: Verilerin JSON dosyalarına düzgünce kaydedilmesi ve yedeklenmesini sağlıyor.


reports.py: Kimin kitabı gecikmiş, kimin ne kadar borcu var gibi raporları çıkarıyor.

Bazı Kurallar ve Limitler 

Bir üye aynı anda en fazla 5 kitap alabiliyor, sınırlandırdım.

Kitap iade tarihi geçerse sistem otomatik olarak günlük 2.0 TL ceza kesiyor.

Kitap ararken hem isme hem de yazara göre arama yapabiliyorsunuz.
Ek olarak yıl ve janraya göre filtreleyebiliyoruz.

Örnek Akış 

Önce kütüphaneci olarak girip kitap ekliyoruz, sonra patron (üye) menüsünden kayıt olup o kitabı ödünç alıyoruz. Sistem her şeyi data/ içindeki json dosyalarına kaydediyor.
