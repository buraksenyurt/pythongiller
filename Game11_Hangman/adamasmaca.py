import random, sys
from termcolor import COLORS, colored
import json  # Json okumaları için kullanacağız

HANGMAN_PICS = [
    r"""
 +--+
 |  |
    |
    |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""", r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""
]

COUNTRY = "Türkiye"


def main():

    print(
        colored(
            """        
        Adam Asmaca oyununa hoş geldin !!!

        Hazır olduğunda bir tuşa bas ;)
    """, "cyan"))

    input(colored('..:', 'cyan'))

    print(
        colored("""
        Hangi ülke için yarışmak istersin?
    """, "cyan"))

    # Ülke adlarını tutan sözlüğü çektiğimiz yer
    countries = getCountryNames()
    # Key Value çiftleri üstünde dolaşıp oyuncuya seçim yapması için yardımcı oluyoruz.
    for k, v in countries.items():
        print(colored("""{} -> {}""".format(k, v), "green"))

    # Oyuncunun seçtiği ülke bilgisinin kodunu kontrol ettiğimiz yer
    while True:
        selected = input("..:")

        # Oyuncunun girdisinin sayısal olup olmadığı kontrol ediliyor
        if not selected.isnumeric():
            print(colored('Ülkenin kodunu girmelisin', 'red'))
            continue

        # Sayısal int türüne dönüştürülüyor
        code = int(selected)

        # Ülkeler listesinde olup olmadığına bakılıyor
        if not code in countries:
            print(colored('Listede olan kodlardan girmelisin.', 'red'))
        else:
            # Nihayet doğru seçimi yapmış demektir
            break

    print(
        colored(
            """
        Güzel diyarlar arasında seçtiğin yer,

        {}

        İşte sorun da geliyor.
    """.format(countries[code]), "yellow"))

    # Oyuncunun seçtiği şehre göre şehirlerin listesini çekiyoruz
    cities = getCities(countries[code])
    secretCity = random.choice(cities).upper()

    print(secretCity)
    missedLetters = []
    correctLetters = []

    # Oyunun sonsuz döngü motoru
    # Tahmin sayıları bitene veya bilene kadar devam edecek.
    while True:
        # Her harf tahmini sonrası oyun tahtasının güncel durumunu çizdirmeliyiz
        # kullanılan harfler, doğru olanlar ve aranan şehir bilgisine göre bu çizim yapılır.
        draw(missedLetters, correctLetters, secretCity)
        # Oyuncudan harf tahmini alınan yer.
        guess = getPlayerGuess(missedLetters + correctLetters)
        # Harf varsa doğru harfler listesine eklenir.
        if guess in secretCity:
            correctLetters.append(guess)

            # doğru olma hali için bir işaret değişkeni (flag)
            isPlayerCorrect = True
            # Şehirdeki harflerin tamamı correctLetters içerisinde farsa kullanıcı bilmiştir.
            for letter in secretCity:
                if letter not in correctLetters:
                    isPlayerCorrect = False
                    break
            # yani tüm harfler bilindiyse oyun kodu buraya atlar.
            if isPlayerCorrect:
                print(
                    colored(
                        '''
                    BRAVOOO!!! 
                    
                    {} şehrine iki kişilik uçak bileti kazandın.

                    \a'''.format(secretCity), 'yellow'))
                # Oyuncu tebrik edildikten sonra break ile while döngüsünden ve onu takiben devam eden satır olmadığı için programdan çıkılır.
                break
        else:
            # Eğer harf yoksa, kullanılan harfler listesine ekleme yapılır.
            missedLetters.append(guess)
            # Yarışmanın bitip bitmediğini kontrol etmek için bilinemeyen harflerin toplamı ile HANGMAN_PICS uzunluğu kıyaslanır
            # Yani kağıda çizilecek şey kalmayınca iş bitmiştir. Oyuncu kaybeder.
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                # Yine tahtanın son hali çizilir
                draw(missedLetters, correctLetters, secretCity)
                # ve oyuncuya acı mesaj verilir :D
                print(
                    colored(
                        '''
                        Ne yazık ki başka hakkın kalmadı :()

                        Kelime şuydu,
                        {}
                
                        '''.format(secretCity), 'red'))
                break


'''
Json veri dosyasından ülke adlarını alan fonksiyondur.
Geriye ülke listesini sayısal numaralar da ekleyerek dictionary olarak döner.
'''


def getCountryNames():
    # ülke adlarını dictionary olarak tutabiliriz. Çünkü oyuncuya seçim için sayı da vermek istiyorum.
    names = {}
    # cities.json dosyası utf8 formatlı olarak açılır(Türkçe karakter desteği olsun diye)
    file = open('cities.json', encoding='utf8')
    # dosyadaki veriler json paketinin load fonksiyonu ile yüklenir.
    data = json.load(file)
    index = 10
    # countries json içeriğinde dolaşılır
    for c in data['countries']:
        # ülke adı index numarası bilgisi ile sözlüğe eklenir
        names[index] = c['name']
        index += 1

    # açılmış dosya kapatılır
    file.close()

    # elde edilen ülke adları geriye döndürülür.
    return names


'''
Parametre olarak gelen ülke bilgisine göre JSON içeriğinden şehirleri çeken fonksiyon.
'''


def getCities(country):
    # Tipik olarak json dosyasının yükleyip countries içindeki name elementlerinde dolaşıyor
    # ve parametre olarak gelen ülke adına eşit olanı bulunca cities içeriğini listeye alıyoruz.
    cities = []
    file = open('cities.json', encoding='utf8')
    data = json.load(file)

    for c in data['countries']:
        if c['name'] == country:
            cities = c['cities']
            # cities' i bulunca döngüyü devam ettirmeye gerek yok
            break

    file.close()
    return cities


'''
    Oyuncunun girdiği harf tahminini aldığımız fonksiyon.
'''


def getPlayerGuess(usedLetters):
    # Oyuncudan ısrarla doğru bir harf girişi yapmasını istediğimiz için sonsuz bir döngü var
    # Bilgi harf olmalı. Yani tek karakter ve alfa nümerik. Ayrıca daha önceden oyuncu tarafından söylenmemiş olmalı.
    while True:
        guess = input(colored('Harf ? ', 'magenta')).upper()
        if len(guess) != 1:
            print(
                colored('Sadece tek bir harf girmen gerekiyor dostum.', 'red'))
        elif guess in usedLetters:
            print(
                colored('Bu harfi söylemiştin. Lütfen başka bir tane söyle.',
                        'red'))
        elif not guess.isalpha():
            print(colored('Lütfen harf gir.', 'red'))
        else:
            return guess


def draw(missed, correct, word):
    print(colored(HANGMAN_PICS[len(missed)], 'blue'))

    # print(colored('İşte tutturamadığın harfler: ', 'red'), end='')
    for letter in missed:
        print(letter, end=' ')
    # if len(missed) == 0:
    #     print(colored('Harf kalmadı\a', 'red'))
    print()

    # Kelime uzunluğu kadar _ işareti üretiliyor
    blanks = ['_'] * len(word)

    # Doğru bilinen harfleri boşluklarla değiştirdiğimiz yer
    # word ile gelen şehrin tüm harflerine bakılıyor.
    for i in range(len(word)):
        # Eğer harf kelimede olan bir harfse
        if word[i] in correct:
            # _ lerden oluşan kelimedeki yeri bu harfle değiştiriliyor
            blanks[i] = word[i]

    # Kelime, blanks ile gelen _ karakterleri ile birleştiriliyor
    print(' '.join(blanks))


if __name__ == '__main__':
    # Normalde program çalışırken Ctrl+C'ye basıldığında uygulama interrupt olur.
    # Bunu KeyboardInterrupt'ta yakalayıp sys.exit() ile düzgün bir çıkış sağlıyoruz.
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()