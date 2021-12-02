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

    countries = getCountryNames()
    print(countries)


'''
Json veri dosyasından ülke adlarını alan fonksiyondur.
Geriye ülke adlarından oluşan listeyi döndürür.
'''


def getCountryNames():
    names = []
    # cities.json dosyası utf8 formatlı olarak açılır(Türkçe karakter desteği olsun diye)
    file = open('cities.json', encoding='utf8')
    # dosyadaki veriler json paketinin load fonksiyonu ile yüklenir.
    data = json.load(file)

    # countries json içeriğinde dolaşılır
    for i in data['countries']:
        # name alanı değerleri names listesine eklenir
        names.append(i["name"])

    # açılmış dosya kapatılır
    file.close()

    # elde edilen ülke adları geriye döndürülür.
    return names


if __name__ == '__main__':
    # Normalde program çalışırken Ctrl+C'ye basıldığında uygulama interrupt olur.
    # Bunu KeyboardInterrupt'ta yakalayıp sys.exit() ile düzgün bir çıkış sağlıyoruz.
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()