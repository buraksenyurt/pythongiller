import random, sys  # Rastgele sayı üretimi için random modülünü kullanacağız. sys modülünü ise uygulamadan sistem çıkmak için.
from termcolor import colored  # terminali şenlendirmek için kullanılan harici modül

# Zardaki rakamların metinsel ifadeleri için basit bir Dictionary kullanılıyor.
# Sabit olduğu içinde değişken adı büyük harflerler yazıldı
DICE_NUMBERS = {1: 'Bir', 2: 'İki', 3: 'Üç', 4: 'Dört', 5: 'Beş', 6: 'Altı'}

print('\a')  # Terminalden bell komutunu çalıştırır. Yani ses verir :)
print(
    colored(
        'Merhaba oyuncu, hoşgeldin. Küçük bir bahse var mısın?\nKazanırsan daha çok suşi yiyebilirsin.\nElimde iki zar var. Onları attığımda toplamlarının tek mi çift mi olduğunu tahmin etmen yeterli?',
        'yellow'))

made = 100  # Oyuncunun tabağındaki varsayılan suşi sayısı

# Diğer oyunlarda da olduğu gibi burada da oyunun ana döngüsü kullanıcı çıkmak isteyen kadar devam eder
while True:
    print(
        colored(
            '''Görüyorum ki tabağında {} suşi var. Ne kadarını paylaşacaksın?\nBu arada eğer seni sıkıyorsam Sayanora demen yeterli.'''
            .format(made), 'cyan'))

    # Oyuncudan mutfağa yatıracağı suşi adedi istenir
    while True:
        betto = input('..:')  # Oyuncudan bir girdi alıyoruz

        # Oyuncu sayanora yazarsa
        # eğer terminalden girilen içerik sayısal değilse
        # bu oyuncuya ifade edilir
        if betto.upper() == 'SAYANORA':
            print(colored('Ki o tsukete! (Kendine iyi bak)', 'cyan'))
            sys.exit()  # uygulamadan çıkılır
        elif not betto.isdecimal():
            print(colored('Kaç suşi dedin anlamadım.', 'red'))
        else:
            # buraya gelindiyse girilen değer kullanılabilir. Bu nedenle int türüne dönüştürülür
            betto = int(betto)
            break

    # 1 ile 6 arasında iki rastgele integer üretilip saikoro(Japonca zar demek) değişkenlerine atanır
    saikoro1 = random.randint(1, 6)
    saikoro2 = random.randint(1, 6)

    print('Zarları attım. Tahminin nedir? Tek(HAN) mi Çift(CHO) mi?')

    # Oyuncudan tek mi çift mi tahmini alınır
    # Ekrandan girilen tahmin alınır ve büyük harfe çevrilir
    # Oyuncunun terminalden girdiği içerik geçerlideğilse
    # Oyuncu uyarılır ve döngü devam eder
    while True:
        yosoku = input('..:').upper()
        if yosoku != 'CHO' and yosoku != 'HAN':
            print(colored('Cho veya Han yazmalısın', 'red'))
        else:
            break

    # Bilgisayar sonuçları paylaşır
    print('İşte sonuçlar')
    print('''{}-{} geldi. Toplamı {}.'''.format(DICE_NUMBERS[saikoro1],
                                                DICE_NUMBERS[saikoro2],
                                                saikoro1 + saikoro2))

    # Zarların toplamının iki ile bölümüne bakılır. Yani çift sayı olup olmadığına.
    ketsuron = (saikoro1 + saikoro2) % 2 == 0
    if ketsuron:
        henji = "CHO"
    else:
        henji = "HAN"

    # Oyuncunun tahmininin doğruluğuna göre hesaplamalar yapılır
    if henji == yosoku:
        made += betto
        print(
            colored(
                '''{} suşi kazandın. Mutfağın payı {} suşi'''.format(
                    betto, made // 10), 'green'))
        made = made - (betto // 10)
        print(
            '''Kendi payımı da aldıktan sonra artık tabağında {} suşi var.'''.
            format(made))
    else:
        made -= betto
        print('Üzgünüm dostum :(')

    if made == 0:
        print(colored('Hiç suşin kalmadı be yaa', 'red'))
        print(colored('Oynadığın için teşekkürler', 'magenta'))
        sys.exit()
