import math, random, sys, time
from termcolor import COLORS, colored

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
elif player_response.upper(
) == "START":  # Cevap START ise oyunu başlatacağımız yer
    print(colored('Haydi başlayalım', "yellow"))
else:  # Ne Help ne Start girmişse oyunu sonlandırdığımız yer
    print(colored('Üzgünüm ama ne demek istediğini anlayamadım', "red"))
    sys.exit()
