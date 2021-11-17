import random, sys, time
from termcolor import colored
'''
    Oyun sahasının uzunluğu, yüksekliği, hayalet sayısı, teleport sayısı, avcı hayalet sayısı,
    duvar sayısı, ve karakter sembolleri ile ilgili sabit tanımlamaları yapılıyor.
'''
BOARD_WITH = 70
BOARD_HEIGHT = 20
GHOST_COUNT = 20
TELEPORT_COUNT = random.randint(1, 4)
HUNTER_GHOSTS_COUNT = 2
WALL_COUNT = 100
GHOST = colored(chr(9587), 'cyan')  # Oyuncuyu kovalayan hayalet karakteri
PLAYER = colored(
    'P', 'magenta', attrs=['bold', 'blink', 'underline']
)  # Oyuncu için altı çizili magenta renginde ve yanıp sönen bir P karakteri kullandık
EMPTY_SPACE = ' '
GHOST_HUNTER = colored(
    chr(9587), 'red')  # Hayaletler çarptığında onları öldüren avcı karakteri
WALL = chr(9608)  # Duvar sembolü


def main():
    print(colored('Hayaletten kaç oyununa hoş geldin', 'cyan'))

    # oyun sahası oluşturulur
    board = createBoard()
    # hayaletler sahaya yerleştirilir
    ghosts = addGhosts(board)
    # oyuncu için müsait başlangıç pozisyonu bulunur
    player_location = findFreeLoc(board, ghosts)

    while True:
        # oyun sahası ekrana çizilir
        displayBoard(board, ghosts, player_location)

        if len(ghosts) == 0:
            print('''
                Ortada hiç hayalet kalmadı. 
                Kazandın dostum :)

                Yine gel!!!
                    ''')
            sys.exit()

        player_location = move(board, ghosts, player_location)

        displayBoard(board, ghosts, player_location)


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
    for _ in range(HUNTER_GHOSTS_COUNT):
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


'''
    Oyun tahtasını sahaya çizmek için kullanılan fonksiyondur.
'''


def displayBoard(board, ghost, player_position):
    # Tüm tahtayı dolaşan iki boyutlu döngü (x,y)'nin ne olduğun bakar ve print işlemi gerçekleştirir.
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WITH):
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == GHOST_HUNTER:
                print(GHOST_HUNTER, end='')
            elif (x, y) == player_position:
                print(PLAYER, end='')
            elif (x, y) in ghost:
                print(GHOST, end='')
            else:
                print(EMPTY_SPACE, end='')
        print(
        )  # Dış döngünün satırıdır. İlk satırdaki karakterlerin yerleşimi bitince alt satıra geçilir.
    print()


'''
    Hayaletleri parametre olarak gelen güncel oyun sahasına ekleyen fonksiyon
'''


def addGhosts(board):
    ghosts = []
    for _ in range(GHOST_COUNT):
        x, y = findFreeLoc(board, ghosts)
        ghosts.append((x, y))
    return ghosts


'''

    Oyuncuya bir sonraki hamlesinin ne olacağını soran ve uygun lokasyonu döndüren fonksiyondur.
    W yukarı, A sola, D sağa, X aşağıya, S ise olduğun yerde kal hamlelerini temsil eder.
'''


def move(board, ghosts, player_location):
    #İlk olarak parametre olarak gelen güncel oyuncu konumundan x,y değerleri alınır
    pX, pY = player_location

    # w değişkenin W olma şartı yukarı harekette bir engelle karşılaşılmama halidir. Aksi durumda w değişkenine boşluk atanır.
    # aynı koşul a,d,x ile yapılmak istenen hareketler için de kontrol edilir.
    w = 'W' if isEmpty(pX, pY - 1, board, ghosts) else ' '
    a = 'A' if isEmpty(pX - 1, pY, board, ghosts) else ' '
    d = 'D' if isEmpty(pX + 1, pY, board, ghosts) else ' '
    x = 'X' if isEmpty(pX, pY + 1, board, ghosts) else ' '
    # allMoves içinde ardışıl olarak sadece hareket edilebilecek yerlere ait bilgiler yer alacaktır.
    # allMoves değişkenini aşağıdaki döngüde geriye uygun hareket alanını dönerken kullanmaktayız.
    allMoves = (w + a + d + x + 'S')

    # Sonsuz döngüde oyuncunun hareket edebileceği alanlara göre kullanabileceği tuşları göstermekteyiz.
    # Kullanabileceği tuşlar yukarıda tespit edilmişti.
    # Ayrıca T harfine basarsa boş ve rastgele bir lokasyona ışınlanması da söz konusu.
    while True:
        print(
            colored(
                '''
        {} kez ışınlanabilirsin. Tahnin et hangi harfe basınca ışınlacaksın...'
        Hareket edebileceğin yerler şöyle.

                ({})
        ({}) -   (S) -  ({})
                ({})
        
        Hamleni görelim.
        Çıkmak için YETER yazman yeter :D
        
        '''.format(board["teleports"], w, a, d, x), "yellow"))

        # Oyuncudan hangi hamleyi yapacağını öğreniyoruz.
        player_move = input('..:').upper()
        # eğer yeter yazarsa oyundan çıkılır
        if player_move == "YETER":
            sys.exit()
        # eğer T harfine basmış ve board isimli dictionary koleksiyonunda(ki metoda parametre olarak gelir)
        # kullanılabilir sayıda teleport hakkı varsa boş bir lokasyon bulup üretilen x,y değerlerini döndürüyoruz
        elif player_move == 'T' and board["teleports"] > 0:
            board["teleports"] -= 1
            return findFreeLoc(board, ghosts)
        # Yukarıdaki koşullar haricinde bir durumda, geçerli bir hamle girilmiş ve bu hamle(basılan tuş)
        # oyuncunun hareket edebileceği yerleri işaret eden allMoves metninde varsa
        # { } arasındaki hareket noktalarından oyuncunun seçtiği yöne doğru olanın x,y bilgisini dönüyoruz.
        elif player_move != '' and player_move in allMoves:
            # return kısmında bir dictionary koleksiyonu oluşturulur
            # ve [] operatörü ile oyuncunun hamlesine denk düşen ikili (tuş ve x,y koordinatını taşıyan tuple) döndürülür
            return {
                'W': (pX, pY - 1),
                'A': (pX - 1, pY),
                'D': (pX + 1, pY),
                'X': (pX, pY + 1),
                'S': (pX, pY)
            }[player_move]
        else:
            # tedbir amaçlı yukarıdaki koşullara uymayan bir durum varsa duvara denk düştüğümüzü varsayıp
            # olduğu yerde hamle yapmasını sağlayabiliriz.
            return (pX, pY)


def isEmpty(x, y, board, ghosts):
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in ghosts


if __name__ == '__main__':
    main()