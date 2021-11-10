import random  # rastlantısallık oyunların olmazsa olmaz parçalarından
from termcolor import colored  # ortamı renklendirmek için başvuracağımız harici python paketi

# ''' notasyonunu kullandığımızda buraya nasıl yazdıysak terminale de o şekilde basılacaktır.
print(
    colored('''
    Oyunculaarrrr!!! 
    
    Havuç hangi kutuda oyununa hoşgeldiniz.                
                
    Oyun başladığında her ikinizin birer kutusu olacak.
    İçinizden seçeceğim birisine diğerinin gözleri kapalı iken kutusunun içini göstereceğim.

    Sonra diğer oyuncu tahminde bulunacak. 
    Havuç o kutunun içinde mi yoksa arkadaşı kutuların yerini değiştirmiş olabilir mi?
    
    ''',
            'yellow',
            attrs=['bold'])
)  # attrs termcolor paketinin bir özelliği. sarı renkli fontu aynı zamanda kalın formatta basmayı sağlıyor.

# Oyuna başlayabilmek için terminalden girdi bekliyoruz
input('Başlamak için bir tuşa basınız')

# oyuncuların adlarını terminalden alalım ve iki değişkende tutalım
first_player = input(
    colored('İlk oyuncu. Bana adını söyler misin? ', 'magenta'))
second_player = input(
    colored('Şimdi de gizemli arkadaşın bana adını behşeder mi lütfen? ',
            'cyan'))

# :5 operatörü ile bir string içinde ilk 5 karakteri dilimleyebiliriz
player_names = first_player[:5] + '.........' + second_player[:5]
print(player_names)

left_box_closed = colored(
    '''
 _________ 
/        /| 
+-------+ |
|   A   | |
|       | /
+-------+/
''', 'magenta')

right_box_closed = colored(
    '''
                 _________ 
                /        /|
                +-------+ |
                |   B   | |
                |       | /
                +-------+/
''', 'cyan')

left_box_opened = colored(
    '''
  __VV___ 
 |  VV   |
 |__||___| 
/   ||   /| 
+-------+ |
|   A   | |
|       | /
+-------+/
    '''
,'magenta')

left_box_empty = colored(
    '''
  _______ 
 |       |
 |_______| 
/        /| 
+-------+ |
|   A   | |
|       | /
+-------+/
    '''
,'magenta')

right_box_opened = colored(
    '''
                  __VV___ 
                 |  VV   |
                 |__||___| 
                /   ||   /| 
                +-------+ |
                |   B   | |
                |       | /
                +-------+/
    '''
,'cyan')

right_box_empty = colored(
    '''
                  _______ 
                 |       |
                 |_______| 
                /        /| 
                +-------+ |
                |   B   | |
                |       | /
                +-------+/
    '''
,'cyan')

print(left_box_closed + right_box_closed)
