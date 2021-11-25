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
BOARD = """
ABCDEFG
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+"""

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

    Kimin başlayacak? Yazı/Tura. Seçiminizi yapın.

    """, "yellow"))

    # Yazı Tura oynatıp kimin başlayacağına karar verdiriyoruz.
    # Basit bir if else bloğu da olabilirdi. Biraz renklendirelim dedim.
    # 0 veya 1 gelmesine göre dizinden o indise ait eleman seçilir.
    input('Para atışı yapıldı. Devam etmek için bir tuşa basın..:')

    choises = ["Yazı", "Tura"]
    print(
        colored("{} diyen başlar!".format(choises[random.randint(0, 1)]),
                "magenta"))


if __name__ == '__main__':
    main()
