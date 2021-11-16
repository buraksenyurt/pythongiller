import copy, random, sys, time  # Kullanacağımız python paketleri
from termcolor import colored

# Yaşam alanımızın sınırlarını belirliyoruz
# 49 X 20 bir ortam olduğunu düşünebiliriz.
SCREEN_WIDTH = 49
SCREEN_HEIGHT = 20
ALIVE = colored(
    '■', 'yellow')  # Canlı olma halini bu ASCII karakteri ile simüle edelim
DEAD = ' '  # Ölü olma hali tam bir boşluk


def main():

    # oyun alanının durumunu tutacağımız dictionary koleksiyonunu setup ile dolduruyoruz
    next_cells = setup()

    # oyunun ana döngüsü (tabii ki biz aksini diyinceye kadar sonsuz bir döngü)
    while True:
        print(
            '\n' * 80
        )  # oyun zeminini her setup ya da simülasyonun sonraki aşamasında şöyle bir temizliyoruz.

        # ilk olarak nextCells'in simülasyonun güncel durumunu deep copy ile kopyalıyoruz
        cells = copy.deepcopy(next_cells)
        print_cells(cells)
        next_cells = calculate_next_generation(cells)

        # oyuncan çıkmak için kullanıcının bir tuşa basmasını bekliyoruz.
        # bunu yaparken bir try bloğu kullandık ve içinde sahneyi 3 saniyeliğine dondurmaktayız (Thread sleep).
        try:
            time.sleep(1)
        except KeyboardInterrupt:  # Klavyeden bir kesme sinyali gelirse exit ile sisteme döneceğiz
            sys.exit()


"""
setup()

Oyun alanını iki boyutlu bir dizi şeklinde düşünürsek,
tuple olarak tutulan x,y koordinatlarında ölü bir hücre mi yoksa canlı bir hücre mi olacağını sağladığımız kısım.
randint ile üretilen değerin 0 olma haline göre (x,y) şeklinde ifade edilen tuple'ın ALIVE veya DEAD karakterlerinden birisini alması söz konusu.
Burada aralığı ne kadar geniş verirsek 0 bulma ihtimalimiz o kadar azalacağından yaşam alanındaki hücrelerin sayısını da (canlı popülasyonunu) doğrudan etkilemiş oluyoruz.
"""


def setup():
    cells = {}
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            if random.randint(0, 5) == 0:
                cells[(x, y)] = ALIVE
            else:
                cells[(x, y)] = DEAD
    return cells


"""
print_cells

parametre olarak gelen dictionary'deki bilgilere göre ekrana hücreleri çizen fonksiyon
"""


def print_cells(cells):
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            print(cells[(x, y)], end='')
        print()


"""
calculate_next_generation

parametre olarak gelen dictionary'deki hücrelerin komşularını bulur. 
Komşuların sayısına göre Conway kuralları işletilir ve yeni hesaplamara göre oluşan dictionary 
fonksiyondan geriye döndürülür.
"""


def calculate_next_generation(cells):
    next_cells = {}
    # dictionary'deki x ve y değerlerini dolaşıyoruz.
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            (l, r, a, b) = get_neighbors_coor(x, y)
            neighbors_count = 0  # canlı komşuları bulacağız. Bakmamız gereken 8 yer var.
            if cells[(l, a)] == ALIVE:  # Üst sol komşu canlı ise
                neighbors_count += 1
            if cells[(x, a)] == ALIVE:  # Üst komşu canlı ise
                neighbors_count += 1
            if cells[(r, a)] == ALIVE:  # sağ üst komşu canlı ise
                neighbors_count += 1
            if cells[(l, y)] == ALIVE:  # sol komşu canlı ise
                neighbors_count += 1
            if cells[(r, y)] == ALIVE:  # sağ komşu canlı ise
                neighbors_count += 1
            if cells[(l, b)] == ALIVE:  # sol alt komşu canlı ise
                neighbors_count += 1
            if cells[(x, b)] == ALIVE:  # alt komşu canlı ise
                neighbors_count += 1
            if cells[(r, b)] == ALIVE:  # Sağ alt komşu canlı ise
                neighbors_count += 1

            # Buradan itibaren Conway kuralları geçerli olacaktır.
            # Üst if bloklarında (x,y)'nin komşularının sayısını bulmuş olduk
            # eğer x,y konumundaki hücre canlı ise ve 2 veya 3 komşusu varsa yaşamaya devam edecek
            if cells[(x, y)] == ALIVE and (neighbors_count == 2
                                           or neighbors_count == 3):
                next_cells[(x, y)] = ALIVE
            elif cells[(
                    x, y
            )] == DEAD and neighbors_count == 3:  # eğer kendisi ölü ve tam 3 canlı komşusu varsa o hücre canlanacak
                next_cells[(x, y)] = ALIVE
            else:  # aksi durumların hepsinde x,y konumundaki hücre ölü kabul edilecek
                next_cells[(x, y)] = DEAD

    return next_cells


"""
    get_neighbors_coor

    paramtre olarak gelen x,y'ye bağlı olarak komşu konumları buluyor
"""


def get_neighbors_coor(x, y):
    # önce o anki hücrenin sağ, sol, üst ve alt komşularına ait koordinatları buluyoruz.
    l = (x - 1) % SCREEN_WIDTH
    r = (x + 1) % SCREEN_WIDTH
    a = (y - 1) % SCREEN_HEIGHT
    b = (y + 1) % SCREEN_HEIGHT
    return (l, r, a, b)


if __name__ == '__main__':
    main()