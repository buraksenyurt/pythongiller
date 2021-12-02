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
        Güzel güzeli diyarlardan seçtiğin yer 

        {}

        İşte sorun da geliyor.
    """.format(countries[code]), "yellow"))

    # Oyuncunun seçtiği şehre göre şehirlerin listesini çekiyoruz
    cities = getCities(countries[code])


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


if __name__ == '__main__':
    # Normalde program çalışırken Ctrl+C'ye basıldığında uygulama interrupt olur.
    # Bunu KeyboardInterrupt'ta yakalayıp sys.exit() ile düzgün bir çıkış sağlıyoruz.
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()