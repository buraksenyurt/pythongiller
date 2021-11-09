import random, sys  # Rastgele sayı üretimi için random modülünü kullanacağız. sys modülünü ise uygulamadan sistem çıkmak için.

# Zardaki rakamların metinsel ifadeleri için basit bir Dictionary kullanılıyor.
# Sabit olduğu içinde değişken adı büyük harflerler yazıldı
DICE_NUMBERS = {1: 'Bir', 2: 'İki', 3: 'Üç', 4: 'Dört', 5: 'Beş', 6: 'Altı'}

print(
    '''Merhaba oyuncu\nHoşgeldin.Bahse var mısın?\n\nElimde iki zar var. Onları attığımda toplamlarının tek mi çift mi olduğunu tahmin edebilir misin? Bilirsen '''
)

made = 100  # Oyun başlamadan önce mutfaktaki suşi sayısı

# Diğer oyunlarda da olduğu gibi burada da oyunun ana döngüsü kullanıcı çıkmak isteyen kadar devam eder
while True:
    print(
        '''Mutfakta {} suşi var. Ne kadar yatıracaksın? Gitmek istersen Sayanora yazman yeterli.'''
        .format(made))

    # Oyuncudan mutfağa yatıracağı suşi adedi istenir
    while True:
        betto = input('..:')  # Oyuncudan bir girdi alıyoruz

        # Oyuncu sayanora yazarsa
        # eğer terminalden girilen içerik sayısal değilse
        # bu oyuncuya ifade edilir
        if betto.upper() == 'SAYANORA':
            print('''Ki o tsukete(Kendine iyi bak)''')
            sys.exit()  # uygulamadan çıkılır
        elif not betto.isdecimal():
            print('''Kaç tane suşi dedin anlamadım.''')
        else:
            # buraya gelindiyse girilen değer kullanılabilir. Bu nedenle int türüne dönüştürülür
            betto = int(betto)
            break

    # 1 ile 6 arasında iki rastgele integer üretilip saikoro(Japonca zar demek) değişkenlerine atanır
    saikoro1 = random.randint(1, 6)
    saikoro2 = random.randint(1, 6)

    print('''Zarları attım. Tahminin nedir? Tek mi Çift mi?''')

    # Oyuncudan tek mi çift mi tahmini alınır
    # Ekrandan girilen tahmin alınır ve büyük harfe çevrilir
    # Oyuncunun terminalden girdiği içerik geçerlideğilse
    # Oyuncu uyarılır ve döngü devam eder
    while True:
        yosoku = input('..:').upper()
        if yosoku != 'TEK' and yosoku != 'ÇİFT':
            print('''Tek veya Çift yazmalısın''')
        else:
            break

    # Bilgisayar sonuçları paylaşır
    print('''İşte sonuçlar''')
    print('''{}-{} geldi. Toplamı {}'''.format(DICE_NUMBERS[saikoro1],
                                               DICE_NUMBERS[saikoro2],
                                               saikoro1 + saikoro2))
