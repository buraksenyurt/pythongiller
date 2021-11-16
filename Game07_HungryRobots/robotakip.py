import random, sys, time
from termcolor import colored

BOARD_WITH = 80
BOARD_HEIGHT = 40
GHOST_COUNT = 10
TELEPORT_COUNT = random.randint(1, 4)
DEAD_GHOSTS = 2
WALL_COUNT = 100
GHOST = '👻'  # Oyuncuyu kovalayan hayaletler
PLAYER = '🦊'  # Oyuncu
EMPTY_SPACE = ' '
GHOST_HUNTER = '👽'  # Hayaletler çarptığında onları öldüren avcılar
WALL = chr(9617)  # Duvar sembolümüz


def main():
    print(colored('Hayaletten kaç oyununa hoş geldin', 'cyan'))

    board = createBoard()


'''
createBoard fonksiyonu yeni bir oyun sahasını oluşturmak için kullanılır.
Geriye bir dictionary koleksiyonu döndürür.
İçinde kullanılabilecek teleport sayısı bilgisi de bulunur.
'''


def createBoard():
    board = {'teleports': TELEPORT_COUNT}

    # Sahayı önce boşluk karakterleri ile temizliyoruz.
    for x in range(BOARD_WITH):
        for y in range(BOARD_HEIGHT):
            board[(
                x, y
            )] = EMPTY_SPACE  # (x,y) iki boyutlu sahada koordinat belirten bir tuple nesnesidir

    # Üst ve alt oyun sınırlarına duvaları yerleştiren döngü
    for x in range(BOARD_WITH):
        board[(x, 0)] = board[(x, BOARD_HEIGHT - 1)] = WALL

    # Bu sefer de sol ve sağ duvarları dolduruyoruz
    for y in range(BOARD_HEIGHT):
        board[(0, y)] = board[(BOARD_WITH - 1, y)] = WALL
    '''
        Şimdi rastgele duvarları yerleştireceğiz.
        Kaçtane duvar üretmek istediğimize bağlı olarak bir döngü başlattık.
        getRandomLocation ile güncel board'da uygun x,y koordinatı arıyoruz. Bir başka deyişle duvarı eklemek için boş bir yer lazım.
        Uygun x,y kooridantlarını WALL_COUNT tükenene kadar arayıp oraya duvar ekliyoruz.
    '''
    for _ in range(WALL_COUNT):
        x, y = findFreeLoc(board, [])
        board[(x, y)] = WALL
    '''
        Sırada avcıların(ölü hayaletler) yerleştirilmesi var. Hayaletler onlara çarpınca da ölüyorlardı.
    '''
    for _ in range(DEAD_GHOSTS):
        x, y = findFreeLoc(board, [])
        board[(x, y)] = GHOST_HUNTER

    return board


'''
    Oyun sahasında boş x,y koordinatı bulan fonksiyon.
    Sonsuz bir döngüsü var. 
    Rastgele x,y değerleri üretilip board parametresi ile gelen güncel oyun sahasında var mı yok mu kontrol ediliyor.
    Buna göre uygun lokasyon bulunursak break ile döngüden çıkıp sonuçlar tuple türünden geriye döndürülüyor.
'''


def findFreeLoc(board, ghosts):
    while True:
        x = random.randint(1, BOARD_WITH - 2)
        y = random.randint(1, BOARD_HEIGHT - 2)
        if board[(x, y)] == EMPTY_SPACE and (x, y) not in ghosts:
            break
    return (x, y)


if __name__ == '__main__':
    main()