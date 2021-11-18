import math, random, sys, time
from termcolor import COLORS, colored

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

    # Oyunun olmazsa olmaz sonsuz döngüsü
    while True:
        number = random.randint(1, 100)
        player_guess = input('..:')

        if player_guess.upper() == "HOF POF":
            print(colored('Yine gelllll', 'yellow'))
            sys.exit()

        factors = findFactors(number)
        print('İzninle bende çarpanları hesap edeceğim')

        for c in WAIT_EFFECT:
            time.sleep(1)
            print(colored(c, 'magenta', attrs=["bold"]))

        if factors == player_guess:
            print(colored('BİLDİN!!!\a', 'green'))
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
                '''.format(factors), 'yellow'))


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
    print(','.join(factors))


if __name__ == '__main__':
    main()