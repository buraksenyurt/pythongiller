import sys, random
from termcolor import colored

# Oyunda kullanacağımı sabitler
EMPTY_BLOCK = ' '  # Tahtadaki boş kısımlar boşluk ile gösterilir.
PLAYER_1 = 'X'  # Birinci oyuncunun pulları X ile gösterilir.
PLAYER_2 = 'O'  # İkinci oyuncunun pulları O ile gösterilir.
BOARD_COLUMNS = 7  # 7 sütundan ve 6 satırdan oluşacak bir oyun tahtası söz konusu
BOARD_ROWS = 6
COLUMN_LABELS = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G'
)  # Oyuncunun pulu hangi sütuna atacağını gösteren yardımcı değerleri tutan tuple

# Oyun tahtasının string gösterimi
# Tahmin edileceği üzere {} ile ifade edilen placeholder'lar bordun o anki durumuna göre oyuncu hamleleri ile dolacaktır
BOARD = colored(
    '''
 ABCDEFG
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+''', 'yellow')

# assert ile kod içerisinde bazı test kabüllerini çalıştırabiliriz.
# assert len(COLUMN_LABELS) == BOARD_COLUMNS


def main():
    print(
        colored(
            """
    Dörtlüyü bulan kazanır!
    Yanyana 4 pul getir oyunu kazan :D

    Birinci oyuncunun pulu  X
    İkinci oyunucun pulu    0

    Kimin başlayacağını rastgele seçeceğim. 
    Hanginiz birinci hanginiz ikinci karar verin.

    """, "yellow"))

    input('Devam etmek için bir tuşa basın..:')

    # Oyuna kimin başlayacağına program karar versin istedim.
    # players dizisinden 0 veya 1 sonucuna göre oyuncu seçilecek.
    players = ["X", "O"]
    number = random.randint(0, 1)
    print(colored("{} başlar!".format(players[number]), "magenta"))

    # Önce boş bir oyun tahtası hazırlanıyor
    board = getEmptyBoard()
    # Hangi oyuncunun başlayacağını seçmiştik.
    playerTurn = players[number]

    #showBoard(board)
    # Bize kazanan belli oluncaya kadar devam edecek bir döngü gerekiyor.
    while True:
        showBoard(board)
        playerMove = askNextMove(playerTurn, board)
        board[playerMove] = playerTurn

        # Hamle sonrası kazanan var mı kontrolü yapılan yer.
        if checkWinner(playerMove, board):
            showBoard(board)
            print(colored('{} kazandı !!!', playerMove, 'blue'))
            sys.exit()
        # Eğer kazanan yoksa ve oyun tahtası tamamen dolmuşsa beraberlik durumu söz konusudur.
        elif isFull(board):
            showBoard(board)
            print(colored('Kazanan yok. Oyun berabere :)', 'green'))
            sys.exit()

        # Buraya gelinmişse oyunda kazanan henüz belli değildir.
        # Hamle sırası diğer oyuncuya geçer
        print("Oyuncu " + playerTurn)
        if playerTurn == PLAYER_1:
            playerTurn = PLAYER_2
        elif playerTurn == PLAYER_2:
            playerTurn = PLAYER_1


'''
    Oyun tahtasında artık hamle yapılacak yer kalıp kalmadığını öğrendiğimiz fonksiyon.
'''


def isFull(board):
    # Tüm oyun tahtası gezilir
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLUMNS):
            # Eğer tahtanın herhangi bir hücresi boşsa false dönülür
            if board[(j, i)] == EMPTY_BLOCK:
                return False
    # Buraya gelindiyse tüm hücreler dolu demektir. Beraberlik durumu.
    return True


'''
    Oyuncuya bir sonraki hamlesini soran fonksiyondur.    
    Parametre olarak board'un güncel halini oyuncunun kendisini alır.
    Uygun sütun söz konusu ise bu sütundaki uygun boşluğun koordinatlarını tuple olarak geriye döndüdür.
'''


def askNextMove(player, board):
    # Sıradaki oyuncu fonksiyona playerName ile gelecek.
    # Ona hamlesini soracağız. Doğru veya uygun hamleyi yapana kadar sormalıyız.
    # Bu nedenle sonsuz döngü var.
    while True:
        print(
            colored(
                '{}, taşını hangi sütuna bırakacaksın? Çıkmak için YETER yaz:',
                'green').format(player))
        response = input('..: ').upper().strip()

        # Eğer response YETER ise sisteme döneriz :D
        if response == 'YETER':
            print(colored('Oynadığın için teşekkürler :(', 'green'))
            # Programdan çık
            sys.exit()

        # Oyuncunun girdiği bilgi COLUMN_LABES isimli Tuple içeriğinde yoksa bunu tekrar isteriz.
        if response not in COLUMN_LABELS:
            print(
                colored(
                    'Geçeri bir sütun girmedin. Şunlardan biri olmalı. {}.',
                    'red').format(COLUMN_LABELS))
            # while döngüsüne devam et
            continue

        # Eğer istenilen girdiye ulaşıldıysa onun index numarasını buluyoruz.
        # Bunu oyun tahtasını ifade eden dictionary'de kullanmaktayız.
        column = COLUMN_LABELS.index(response)

        # Eğer oyuncunun söylediği sütun doluysa tekrardan bir seçim yapmasını istiyoruz.
        if board[(column, 0)] != EMPTY_BLOCK:
            print(colored('Bu sütun dolu. Lütfen başka bir tane seç.', 'red'))
            # döngüye devam et
            continue

        # Buraya kadar gelindiyse oyuncunun girdiği sütun geçerlidir.
        # Alt sütundan başlayarak (ekrana tersten bakmamız lazım) geriye doğru giden bir döngümüz var.
        # Bulunan ilk boş hücrenin sütun ve satır bilgisini tutan Tuple'ı metottan geriye döndürüyoruz.
        for row in range(BOARD_ROWS - 1, -1, -1):
            if board[(column, row)] == EMPTY_BLOCK:
                return (column, row)


'''
    Hamlelere göre oyuncunun kazanıp kazanmadığını tespi eden fonksiyon.
    Teorisi basit. İlk parametre ile oyuncunun sembolü gelir. X veya O.
    Döngüler ikinci parametre ile gelen oyun tahtasını yatay, dikey ve çarpraz olarak kontrol eder.

'''


def checkWinner(symbol, board):
    # Döngülerde satır ve sütunlar belli kriterlere göre dolaşılmakta.

    # ilk döngüde aynı satırda ve sağa doğru ardışıl dört aynı pul var mı bakılıyor.
    for column in range(BOARD_COLUMNS - 3):
        for row in range(BOARD_ROWS):
            stone1 = board[(column, row)]
            stone2 = board[(column + 1, row)]
            stone3 = board[(column + 2, row)]
            stone4 = board[(column + 3, row)]
            # dört pulda parametre olarak gelen sembol ise true döner
            if stone1 == stone2 == stone3 == stone4 == symbol:
                return True

    # Bu döngüde ise aynı sütunda dikey olarak aynı dört pul var mı bakılıyor.
    for column in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS - 3):
            stone1 = board[(column, row)]
            stone2 = board[(column, row + 1)]
            stone3 = board[(column, row + 2)]
            stone4 = board[(column, row + 3)]
            # dört pulda parametre olarak gelen sembol ise true döner
            if stone1 == stone2 == stone3 == stone4 == symbol:
                return True

    # Hem satır hem sütun değiştirilerek bakılıyor. Yani çarprazda ardışıl aynı dört pul var mı buna bakılıyor.
    for column in range(BOARD_COLUMNS - 3):
        for row in range(BOARD_ROWS - 3):
            stone1 = board[(column, row)]
            stone2 = board[(column + 1, row + 1)]
            stone3 = board[(column + 2, row + 2)]
            stone4 = board[(column + 3, row + 3)]
            # dört pulda parametre olarak gelen sembol ise true döner
            if stone1 == stone2 == stone3 == stone4 == symbol:
                return True


'''
    Ekrana oyun tahtasının ilk halini çizdirmek için kullanılan fonksiyondur.
'''


def getEmptyBoard():
    # oyun tahtasını bir dictionary olarak tutacağız.
    board = {}
    # satır sütunları dolaşıp dictionary'deki herbir elemana EMPTY_BLOCK içeriğini basıyoruz.
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLUMNS):
            board[(j, i)] = EMPTY_BLOCK
    # Boş oyun tahtasını hazırladıktan sonra çağıran yere döndürüyoruz.
    return board


'''
    Oyun tahtasını ekrana çizen fonksiyondur.
    Parametre olarak oyun tahtasının güncel içeriğini alır.
'''


def showBoard(board):
    # Oyuncuların yaptıkları hamlelere göre board'un durumu sıklıkla değişecektir.
    # Bu nedenle oyun tahtasını güncel durumuna göre terminale çizdirmeliyiz.

    # Tahtanın güncel halini tutacak dizi
    stones = []
    # oyun tahtasının yani BOARD'un satır ve sütunlarında dolaşacak içi içe döngü
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLUMNS):
            # metoda parametre olarak gelen board'un satır X sütun konumundaki elemanı stones dizisine ekler
            stones.append(board[(j, i)])
    # BOARD şablonundaki placeholder'ların içeriği stones dizisi elemanları ile değiştirilir.
    print(BOARD.format(*stones))


if __name__ == '__main__':
    main()
