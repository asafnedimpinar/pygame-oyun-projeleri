import pygame  # Pygame kütüphanesi kullanılacak
import random  # Rastgele sayılar oluşturmak için
import time  # Zaman işlemleri için
import os  # İşletim sistemi işlemleri için

t0 = time.perf_counter()  # Oyunun başlangıç zamanı

# Pygame'in başlatılması
pygame.init()

# Oyun penceresinin boyutları
xmax = 500
ymax = 500

# Oyunun maksimum süresi (saniye cinsinden)
maxSure = 60

# Düşen topların yarıçapı
ycap = 15

# Oyun döngüsünün çalışmasını kontrol eden değişken
yinele = True

# Aynı anda ekranda olabilecek maksimum topların sayısı
tanemax = 10

# Oyundaki topların bilgisinin tutulacağı liste
taneler = []

# Renklerin tanımlanması
renk = (0, 255, 0)  # Yeşil
arkaplan = (0, 0, 0)  # Siyah
beyaz = (255, 255, 255)  # Beyaz
kirmizi = (255, 0, 0)  # Kırmızı
yesil = (0, 255, 0)  # Yeşil
mavi = (0, 0, 255)  # Mavi

# Renklerin listesi
renkler = [beyaz, kirmizi, yesil, mavi]

# Yeni bir top eklemek için fonksiyon
def tane_ekle():
    while len(taneler) < tanemax:
        x = random.random() * xmax  # Rastgele x pozisyonu
        y = 0  # Y koordinatı
        r = random.randint(0, 3)  # Rastgele renk seçimi
        hizlar = [0.1, 0.2, 0.3, 0.4]  # Farklı düşme hızları
        h = hizlar[r]  # Rastgele hız seçimi
        taneler.append((x, y, r, h))  # Yeni topun listeye eklenmesi

# Oyuncuya mesaj vermek için fonksiyon
def bravo():
    alkis()  # Alkış sesi çal
    pencere.fill(arkaplan)  # Pencereyi siyah renkle doldur
    text1 = font.render("bravo", True, beyaz)  # "Bravo" metni
    text2 = font.render("yeni rekorun", True, beyaz)  # "Yeni rekorun" metni
    text3 = font.render(str(puan), True, beyaz)  # Puanın yazılacağı metin
    h1 = text1.get_height()  # İlk metnin yüksekliği
    h2 = text2.get_height()  # İkinci metnin yüksekliği
    h3 = text3.get_height()  # Üçüncü metnin yüksekliği
    h = h1 + h2 + h3 + 20  # Toplam metin yüksekliği
    y0 = (ymax - h) // 2  # Y koordinatı
    pencere.blit(text1, ((xmax - text1.get_width()) // 2, y0))  # "Bravo" metninin çizimi
    pencere.blit(text2, ((xmax - text2.get_width()) // 2, y0 + h1 + 10))  # "Yeni rekorun" metninin çizimi
    pencere.blit(text3, ((xmax - text3.get_width()) // 2, y0 + h1 + h2 + 20))  # Puanın çizimi

# Topun düşüş sesi fonksiyonu
def plop():
    pygame.mixer_music.load("plop.mp3")  # Plop ses dosyasının yüklenmesi
    pygame.mixer_music.play(0)  # Plop sesinin çalınması

# Alkış sesi fonksiyonu
def alkis():
    pygame.mixer_music.load("alkis.mp3")  # Alkış ses dosyasının yüklenmesi
    pygame.mixer_music.play(0)  # Alkış sesinin çalınması

# Puanı dosyaya kaydetme fonksiyonu
def kaydet(puan):
    if os.path.exists("cip12_puan.txt"):  # Dosya var mı kontrolü
        with open("cip12_puan.txt", "r") as d:  # Dosyayı okuma modunda aç
            s = d.readline()  # İlk satırı oku
            if int(s) < puan:  # Eğer okunan puan kaydedilen puandan küçükse
                bravo()  # Bravo mesajı göster
                with open("cip12_puan.txt", "w") as d:  # Dosyayı yazma modunda aç
                    d.write(str(puan))  # Puani dosyaya yaz
    else:  # Dosya yoksa
        bravo()  # Bravo mesajı göster
        with open("cip12_puan.txt", "w") as d:  # Dosyayı yazma modunda aç
            d.write(str(puan))  # Puani dosyaya yaz

# Oyun penceresinin oluşturulması
pencere = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption("cip12_pygame02.py")  # Oyun penceresinin başlığı
tiktak = pygame.time.Clock()  # Oyun döngüsündeki zamanlama işlemleri için kullanılacak Clock nesnesi
font = pygame.font.SysFont("comicsansms", 48)  # Oyun için kullanılacak yazı tipi ve boyutu
puan = 0  # Oyuncunun puanı
kaydedildi = False  # Puanın kaydedilip kaydedilmediğini belirten bayrak
tane_ekle()  # Oyuna başladığında topların eklenmesi

# Oyun döngüsü
while yinele:
    for olay in pygame.event.get():  # Olayları kontrol et
        if olay.type == pygame.QUIT:  # Çıkış düğmesine basıldıysa
            yinele = False  # Oyun döngüsünü sonlandır
        if olay.type == pygame.KEYDOWN:  # Bir tuşa basıldıysa
            if olay.key == pygame.K_ESCAPE:  # Eğer o tuş ESC ise
                yinele = False  # Oyun döngüsünü sonlandır
                break
        if olay.type == pygame.MOUSEBUTTONDOWN:  # Fare tıklaması algılandıysa
            mx, my = olay.pos  # Tıklanan noktanın koordinatlarını al
            for tane in range(len(taneler)):  # Tüm toplar için kontrol et
                (x, y, r, h) = taneler[tane]  # Topun bilgilerini al
                if (my + ycap > x) and (mx - ycap < x) and (my + ycap > y) and (my - ycap < y):  # Eğer tıklanan nokta bir topun içindeyse
                    plop()  # Düşüş sesi çal
                    puan += h * 10  # Puanı artır
                    taneler.pop(tane)  # Topu listeden kaldır
                    tane_ekle()  # Yeni bir top ekle
        if time.perf_counter() - t0 > maxSure:  # Maksimum süre aşıldıysa
            if not kaydedildi:  # Puan henüz kaydedilmediyse
                kaydet(puan)  # Puani kaydet
                kaydedildi = True  # Kaydedildiği belirt
            continue  # Sonraki adıma geç

    pencere.fill(arkaplan)  # Pencereyi siyahla doldur

    # Topların çizimi
    for tane in range(len(taneler)):
        (x, y, r, h) = taneler[tane]
        y += h
        if y > ymax + ycap * 2:
            taneler.pop(tane)
            tane_ekle()
            continue
        taneler[tane] = (x, y, r, h)
        renk = renkler[r]
        pygame.draw.circle(pencere, renk, (x, y), ycap, 0)

    text = font.render(str(puan), True, beyaz)  # Puanı ekrana yazdır
    pencere.blit(text, ((xmax - text.get_width()) // 2, ymax - text.get_height()))  # Puanı ekrana yerleştir
    pygame.display.flip()  # Ekranı güncelle
    tiktak.tick()  # Oyun döngüsündeki zamanı güncelle

pygame.quit()  # Pygame'i kapat
quit()  # Programı sonlandır