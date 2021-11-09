import random  # rastgele sayı üretmek için ihtiyacımız olan python modülü

NUM_DIGITS = 3  # hane sayısı için bir değişken
MAX_TRY_COUNT = 20  # ne kadar tahmin hakkı vereceğimiz


def main():
    print('''Bil Bakalım Aklımdaki Sayı Ne? oyununa hoşgeldin.
    
    Aklımdan {} basamaklı bir sayı tutacağım. 497 gibi. Ama sana söylemeyeceğim.
    
    Sen bir tahmin yapacaksın.
    
    Eğer Elma dersem, rakamlardan biri doğru ama yanlış pozisyonda.
    Armut dersem rakamlardan biri doğru ve doğru pozisyonda.
    Mısır dersem ise karavana :-)
    '''.format(
        NUM_DIGITS))  # {} ile işaret edilen yere NUM_DIGITS değeri gelecektir.

    # print("{}".format(get_game_number())) # Başlarda test için eklendi.

    while True:  # oyunun ana döngüsü
        secret_number = get_game_number()
        # bilgisayarın üreteceği gizli sayıyı alalım
        print('Bir sayı tuttum ama sana söylemeyeceğim. Henüz')
        try_count = 1
        while try_count <= MAX_TRY_COUNT:  # tahmin sayısı kadarlık bir döngü başlattık
            guess = ''

            # başlangıçta guess aşağıdaki kriterleri sağlamadığı için oyuncudan sayı girmesi istenecektir
            # oyuncu rakam sayısı ve sayısallığı tutturana kadar da bu devam edecektir
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Tahminin nedir?')
                guess = input('...')

            # oyuncunun girdiği değerle bilgisayarın ürettiği sayının karşılaştırılması sonrası
            # oyuncuya bazı ipuçları bırakılacak
            tips = check_guess(guess, secret_number)
            print(tips)
            try_count += 1

            # Tahmin doğruysa döngüden çık
            if guess == secret_number:
                break

            # deneme sayısına rağmen oyuncu bilemezse ona üzücü haberi vereceğiz
            if try_count > MAX_TRY_COUNT:
                print(
                    'Ne yazık ki hakların tükendi.Tuttuğum sayı {} idi'.format(
                        secret_number))

        # En dıştaki sonsuz döngünün sebebi işte burası
        # Bir tur oyandıktan sonra oyuncunun yeniden oynamak isteyip istemeyeceğine göre döngüden çıkılır veya devam edilir
        print('Bir tur daha oynamak ister misin ;-)(Evet E, Hayırsa H)')
        if not input('...').lower().startswith('e'):
            break
    print('Seninle oynamak keyifliydi. Tekrardan görüşmek üzere :-)')


"""
Aşağıdaki fonksiyon oyunun ihtiyacı olan rastgele sayıyı üretir.
"""


def get_game_number():
    numbers = list('0123456789')  # Önce rakamları taşıyan bir liste
    random.shuffle(numbers)  # sayıları güzelce bir karşıtırır
    secret_number = ''
    for i in range(NUM_DIGITS):  # 3 atımlık bir döngü
        secret_number += str(
            numbers[i]
        )  # sırayla sayılar secret_number değişkeninde ardışıl toplanır
    return secret_number  # 3 haneli sayı geriye döner


"""
Oyuncunun girdiği tahmini değerlendirip Elma, Armut, Mısır veya Bingo cevaplarını hesaplayan fonksiyon.
İki parametre alıyor.
İlki oyuncunun tahmini, ikincisi ise bilgisayarın bu turda ürettiği rastgele sayı.
"""


def check_guess(player_guess, secret_number):
    if player_guess == secret_number:
        return "BINGO! Doğru tahmin."
    # Sayılar aynı ise zaten bilmiş demektir.
    # Değilse rakamlara göre durumu oyuncuya söylemeliyiz.

    tips = []  # ipuçlarını tutacak liste

    for i in range(
            len(player_guess)
    ):  # oyuncu tarafından yapılan tahmin rakamlarında gezeceğimiz bir döngü. Nitekim her rakamı değerlendirmek lazım.
        if player_guess[i] == secret_number[
                i]:  # eğer i indisindeki rakamlar her iki değişken içinde aynı ise
            tips.append("Armut")  # doğru rakam doğru konum
        elif player_guess[
                i] in secret_number:  # yukarıdaki koşulu atladığında buraya gelir ve bu koşul sağlanırsa rakam doğru ama yanlış yerdedir
            tips.append("Elma")  # doğru rakam yanlış konum

    # döngü sonucu tips dizisine eklenen hiçbir şey yoksa tahmin komple yanlıştır,
    if len(tips) == 0:
        return "MISIR"  # bu nedenle oyuncuya MISIR denir.

    # lakin bir takım rakamlar için ELMA, ARMUT durumu oluşmuşsa
    tips.sort(
    )  # dizi sıralanır. Sıralamazsak oyuncuya çok net bir ipucu vermiş olabiliriz
    return ','.join(
        tips)  # elemanlar arasına birer boşluk konulara geriye döndürülür


if __name__ == '__main__':
    main()