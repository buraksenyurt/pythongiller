import copy, random, sys, time  # Kullanacağımız python paketleri

SCREEN_WIDTH = 120
SCREEN_HEIGHT = 40
ALIVE = '■'  # Canlı olma halini bu ASCII karakteri ile simüle edelim
DEAD = ' '  # Ölü olma hali tam bir boşluk

# oyun alanının durumunu tutacağımız dictionary.
nextCells = {}


def main():

    init()

    # oyunun ana döngüsü (tabii ki biz aksini diyinceye kadar sonsuz bir döngü)
    while True:
        print(
            '\n' * 80
        )  # oyun zeminini her setup ya da simülasyonun sonraki aşamasında şöyle bir temizliyoruz.

        # ilk olarak nextCells'in simülasyonun güncel durumunu deep copy ile kopyalıyoruz
        cells = copy.deepcopy(nextCells)
        print_cells(cells)


# Oyun alanını iki boyutlu bir dizi şeklinde düşünürsek,
# tuple olarak tutulan x,y koordinatlarında ölü bir hücre mi yoksa canlı bir hücre mi olacağını sağladığımız kısım.
# randint ile üretilen değeri 0 veya 1 olma haline göre (x,y) şeklinde ifade edilen tuple'ın ALIVE veya DEAD karakterlerinden birisini alması söz konusu.
def init():
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            if random.randint(0, 1) == 0:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD


# parametre olarak gelen dictionary'deki bilgilere göre ekrana hücreleri çizen fonksiyon
def print_cells(cells):
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            print(cells[(x, y)], end='')
        print()


if __name__ == '__main__':
    main()