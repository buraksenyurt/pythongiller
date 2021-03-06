# rastlantısallık oyunların olmazsa olmaz parçalarından
import random
# ortamı renklendirmek için başvuracağımız harici python paketi
from termcolor import colored

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
player_names = first_player[:5] + '|.........X.........|' + second_player[:5]
print(player_names)

left_box_closed = colored(
    '''
 _________ 
/        /| 
+-------+ |
|   {}   | |
|       | /
+-------+/
''', 'magenta')

right_box_closed = colored(
    '''
                 _________ 
                /        /|
                +-------+ |
                |   {}   | |
                |       | /
                +-------+/
''', 'cyan')

left_box_full = colored(
    '''
  __VV___ 
 |  VV   |
 |__||___| 
/   ||   /| 
+-------+ |
|   {}   | |
|       | /
+-------+/
    ''', 'magenta')

left_box_empty = colored(
    '''
  _______ 
 |       |
 |_______| 
/        /| 
+-------+ |
|  {}    | |
|       | /
+-------+/
    ''', 'magenta')

right_box_full = colored(
    '''
                  __VV___ 
                 |  VV   |
                 |__||___| 
                /   ||   /| 
                +-------+ |
                |  {}    | |
                |       | /
                +-------+/
    ''', 'cyan')

right_box_empty = colored(
    '''
                  _______ 
                 |       |
                 |_______| 
                /        /| 
                +-------+ |
                |  {}    | |
                |       | /
                +-------+/
    ''', 'cyan')

print(left_box_closed.format('A') + right_box_closed.format('B'))

# format fonksiyonunda aynı değişkenin birden fazla yerde kullanabiliriz. (p2)
print('''

    Oyuncu {p1}. Soldaki A kutusu senin.
        
    Oyuncu {p2}. Tahmin edeceğin üzere sağdaki B kutusu da senin.    
    ve şimdi gözlerini kapamalısın.
    Sakın açma haaa!!!

    Oyuncu {p1}. Arkadaşının bakmadığından emin olduktan sonra bir tuşa bas.
    
'''.format(p1=first_player.upper(), p2=second_player.upper()))
input()

# Şimdi soldaki kutu içine havuç koyup koymama kararını vereceğiz.
# 1 veya 2 gelmesi durumuna göre buna karar vereceğiz.
state = random.randint(1, 2)

# state değerini 1 olması hali orada havuç olduğu anlamına gelecek
carrot_in_left_box = state == 1

# örneğin 1 gelirse sol kutuda havuç olsun. 2 gelirse de olmasın
if state == 1:
    print(left_box_full.format('A'), right_box_closed.format('B'))
else:
    print(left_box_empty.format('A'), right_box_closed.format('B'))

input(
    colored('Devam etmek için lütfen bir tuşa bas {}'.format(first_player),
            'magenta'))

# Şimdi ikinci oyuncunun da aynı ekrana bastığını düşünecek olursak kutuların şu anki halini görmemeli.
# Bu nedenle aşağıdaki kullanımla ekranı şöyle epeyce aşağıya kaydırıyoruz ve diğer kullanıcının yukarıya çıkmamasını umuyoruz :D
# 200 kere enter yaptırdık
print('\n' * 200)

print(
    colored(
        '''

    Oyuncu {p1}. Artık gizemli arkadaşın {p2} gözlerini açabilir.
    Oyuncu {p2}, sence arkadaşının kutusunda havuç var mı? Bunu iyice bir düşün.

    Yeterince düşündün mü {p2}?
    Peki ya kutunu {p1} ile değiştirmek ister misin ;)

    Olur diyorsan E olmaz diyorsan H tuşla ve enter'a bas.

'''.format(p1=first_player.upper(), p2=second_player.upper()), 'green'))

# ikinci oyuncunun cevabını ısrarla almak istediğimizde sonsuz bir while döngüsü var
# girdinin E veya H olup olmadığına göre döngü kırılıyor
while True:
    p2_response = input('..:').upper()
    if not (p2_response == 'E' or p2_response == 'H'):
        print(second_player + ' Lütfen Evet için E, hayır için H yaz')
    else:
        break

print(
    colored(
        '''
    
    Leydiiisss ennn centılmııınnnn!!!
    İşte sonuçlar :)

    Sonuçlar için lütfen bir tuşa basın.

    \a
''', 'blue'))
input()

# Eğer ikinci oyuncu kutuların yerleri değişsin istediyse
# kutuların yerini değiştirip havucun hangi kutuda olduğuna bakarak sonuçları ekrana basıyoruz.
if p2_response == 'E':
    left_box_full, right_box_empty = right_box_full, left_box_empty  # eşitliğin her iki tarafında eşit sayıda değişken kullanılarak çoklu atama yapabiliriz

if carrot_in_left_box:
    print(left_box_full.format('A'), right_box_empty.format('B'))
else:
    print(right_box_full.format('B'), left_box_empty.format('A'))

print('Oynadığınız için teşekkürler :) Görüşmek üzere')