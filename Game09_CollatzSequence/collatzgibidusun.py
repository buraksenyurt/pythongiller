import math, random, sys, time
from termcolor import COLORS, colored


def main():
    print(
        colored(
            '''
            Collatz Gibi Düşün oyununa hoşgeldin :)

            Sana 1 ile 100 arasında bir sayı vereceğim
            ve Collatz dizilimine göre kaç hamlede 1'e
            ulaşılacağını tahmin etmeni isteyeceğim.

            Collatz Serisi hakkında bilgi almak için
            HELP yazıp enter'la.

            Başlamak için START yazman yeterli...
    ''', "cyan"))

    # Başlangıçta oyuncunun cevabını alalım.
    player_response = input('..:')

    # Eğer Help yazmışsa readme.txt içeriği ekrana basıyoruz
    if player_response.upper() == "HELP":
        # with ile readme.txt isimli dosyayı açıyoruz. encoding olarak UTF-8 belirtmezsek Türkçe karakterler bozuk çıkacaktır.
        with open('readme.txt', encoding='utf8') as f:
            # Dosyayı satır satır okumak için bir döngü başlatıyoruz.
            for line in f:
                print(colored(line.strip(), "magenta"))
            start()
    # Cevap START ise oyunu başlatacağımız yer
    elif player_response.upper() == "START":
        start()

    else:  # Ne Help ne Start girmişse oyunu sonlandırdığımız yer
        print(colored('Üzgünüm ama ne demek istediğini anlayamadım', "red"))
        sys.exit()


# oyunun oynandığı fonksiyon.
def start():
    # Program 1 ile 100 arasında rastgele bir sayı üretiyor.
    number = random.randint(1, 100)
    print(
        colored(
            '''
        Haydi başlayalım.
        Sayımız {}

        Kitap, defter, kalem, hesap makinesi serbest :P

        Süren 20 saniye.
        
        '''.format(number), "yellow"))
    # Sembolik bir bekletme efekti
    doWaitEffect()
    # Bekleme sonrası program collatz serisini bulacak ve hem seriyi hem de kaç seferde 1 e gelindiğini geriye döndürecek.
    count, series = find_collatz(number)
    # oyuncunun tahminini alıyoruz
    player_guess = input(colored("Tahminini alabilir miyim?..: ", "yellow"))
    # öncelikle girilen tahminin sayısal bir değer olup olmadığını veya 0 olup olmadığına bakıyoruz.
    if not player_guess.isnumeric() or player_guess == '0':
        print(
            # /a normal şartlarda sistem beep sesini veriyor
            colored("0 dan farklı pozitif bir tahminde bulunmalıydın\a",
                    "red"))
    # oyuncunun tahminine göre bir cevap verilip collatz serisi ekrana basılıyor.
    if player_guess == count:
        print(colored('Bravo bildin :)', "yellow"))
    else:
        print(colored('Üzgünüm. Sayı dizisi şöyle.', "yellow"))

    for n in series:
        print(colored('{},'.format(n), 'green'))


# fonksiyon collatz serisini parametre olarak gelen sayı içim bulur.
# Ayrıca kaç hamelde 1'e ulaşıldığını da geriye döndürür.
def find_collatz(number):
    return 1, [1, 2, 3, 4]


# carpbul.py uygulamasında kullandığımız bekletme efektini burada da kullanabiliriz
# 20 saniyeye tekabül eden bir bekletme söz konusu
def doWaitEffect():
    for _ in range(1, 3):
        for c in ['-', '\\', '|', '/', '-', '|', '\\']:
            time.sleep(0.5)  # yarım saniyelik bekletme
            print(colored(c, 'magenta', attrs=["bold"]), end="\r")


if __name__ == '__main__':
    main()
