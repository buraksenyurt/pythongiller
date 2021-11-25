import sys, random
from termcolor import COLORS, colored

# Oyunda kullanacağımı sabitler
EMPTY_BLOCK = ' '  # Tahtadaki boş kısımlar boşluk ile gösterilir.
PLAYER_1 = colored('X', 'cyan')  # Birinci oyuncunun pulları X ile gösterilir.
PLAYER_2 = colored('O', 'blue')  # İkinci oyuncunun pulları O ile gösterilir.
BOARD_COLUMNS = 7  # 7 sütundan ve 6 satırdan oluşacak bir oyun tahtası söz konusu
BOARD_ROWS = 6
COLUMN_LABELS = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G'
)  # Oyuncunun pulu hangi sütuna atacağını gösteren yardımcı değerleri tutan tuple

# Oyun tahtasının string gösterimi
# Tahmin edileceği üzere {} ile ifade edilen placeholder'lar bordun o anki durumuna göre oyuncu hamleleri ile dolacaktır
BOARD = colored(
    """
 ABCDEFG
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+""", "yellow")

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
    players = ["Oyuncu 1", "Oyuncu 2"]
    number = random.randint(0, 1)
    print(colored("{} başlar!".format(players[number]), "magenta"))

    # Önce boş bir oyun tahtası hazırlanıyor
    board = getEmptyBoard()
    # Hangi oyuncunun başlayacağını seçmiştik.
    playerTurn = players[number]
    showBoard(board)


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
