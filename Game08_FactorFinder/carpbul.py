import math, random, sys, time
from termcolor import COLORS, colored

# Bekleme efektinde kullanacağımız karakterler.
# Sankin dönen bir çarkmış hissiyatı uyandırmak için
WAIT_EFFECT = ['-', '\\', '|', '/', '-', '|', '\\']


def main():

    print(
        colored(
            '''
        Sevgili matematik sever hoşgeldin. Benimle güzel bir oyuna var mısın? :)
        Sana 1 ile 100 arasında bir sayı söyleyeceğim ve çarpanlarını bulup yazmanı isteyeceğim.

        Örneğin 26 sayısı için

            1,2,13,16

            yazıp enter'la.
        
        Eğer sıkılırsan HOF POF yaz.

        Hazır olduğunda herhangi bir tuşa bas.
    ''', "yellow"))
    input()

    # 1 ile 100 arası rastgele sayı üretiyoruz
    number = random.randint(1, 100)

    # Oyunun olmazsa olmaz sonsuz döngüsü
    while True:
        print(colored('Sayımız : {}'.format(number), 'green'))
        # oyuncunun tahminini istiyoruz
        player_guess = input('..:')

        # Önce oyuncunun girdiği bilgiyi kontrol ediyoruz. HOF POF yazarsa sisteme çıkıyoruz.
        if player_guess.upper() == "HOF POF":
            print(colored('Yine gelllll', 'yellow'))
            sys.exit()

        # Bilgisayar o sırada çarpanları buluyor
        factors = findFactors(number)
        # Formatlı halini de hesaplatalım.
        formated_factors = displayFactors(factors)
        print('İzninle bende çarpanları hesap edeceğim')
        doWaitEffect()

        # Oyuncusun girdiği sayı ile programın hesapladığı ifadeyi kıyaslıyoruz.
        # İfadeler doğruysa programdan çıkıyoruz.
        if formated_factors == player_guess:
            print(colored('BİLDİN!!!\a', 'green'))
            sys.exit()
        else:
            print(
                colored(
                    '''

        Üzgünüm ama bilemedin...
        Yeniden denemek ister misin? (E/H)  

        ''', 'red'))
            response = input('..:')
            if response.upper() == 'E':
                continue
            else:
                print(
                    colored(
                        '''
        Öyleyse sana çarpanları söyleyeyim
        {}

        Benimle oynadığın için teşekkürler ;)
                
                '''.format(formated_factors), 'yellow'))
                sys.exit()


'''
    Parametre olarak gelen sayının çarpanlarını bulan metot.
'''


def findFactors(number):
    # Sonuçları factors isimli bir listede tutacağız
    factors = []

    # gelen sayının tam karaköküne kadar(karekökü dahil) birer birer ilerletiyoruz.
    for i in range(1, int(math.sqrt(number)) + 1):
        # eğer sayının i ile bölümü sıfırsa, onun çarpanıdır.
        if number % i == 0:
            factors.append(i)
            # doğal olarak sayının i ile olan diğer böleni de sayının diğer çarpanıdır
            factors.append(number // i)

    # elde edilen listeyi set türünden bir başka diziye çeviriyor. set elemanların benzersiz olmasını sağlıyor. Yani tekrarlı sayıları önlüyoruz.
    # ardından bunu bir list türüne dönüştürüyoruz.
    factors = list(set(factors))
    # fonksiyondan döndüğümüz içerikse listenin sıralanmış hali.
    factors.sort()
    return factors


'''
Çarpanların formatlı bir şekilde yazılmasını sağlayan fonksiyon.
26 için 1,2,13,26 gibi
'''


def displayFactors(factors):
    # enumerate ile bir iterasyon başlatıyoruz.
    # iterasyondaki her eleman indis ve asıl değerden oluşuyor.
    for i, f in enumerate(factors):
        # buna göre i indisli alan f'nin string dönüştürülmüş hali ekleniyor.
        factors[i] = str(f)
    # join ile factors içerisindeki elemanları birer virgül ekleyip birbirlerine bağlıyor ve ekrana yazdırıyoruz.
    return ','.join(factors)


'''
    Program düşünürken komut satırında WAIT_EFFECT içindeki karakterler bir çark gibi dönecek ve bekleme efekti uygulayacak ;)
'''


def doWaitEffect():
    # Burada sembolik olarak bir bekleme efekti yapıyoruz.
    # Wait effect'teki karakterleri basıp satır başına döndürüyoruz.
    # Tabi aynı işlemi 3 kere tekrar ettiriyoruz.
    for _ in range(1, 3):
        for c in WAIT_EFFECT:
            time.sleep(0.5)  # yarım saniyelik bekletme
            print(colored(c, 'magenta', attrs=["bold"]), end="\r")


if __name__ == '__main__':
    main()