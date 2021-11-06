import random # rastgele sayı üretmek için ihtiyacımız olan python modülü

NUM_DIGITS = 4 # hane sayısı için bir değişken
GUESSES_LIMIT=20 # ne kadar tahmin hakkı vereceğimiz

def main():
    print('''Bil Bakalım Aklımdaki Sayı Ne? oyununa hoşgeldin.
    
    Aklımdan {} basamaklı bir sayı tutacağım. 4987 gibi. Ama sana söylemeyeceğim.
    
    Sen bir tahmin yapacaksın.
    
    Eğer Elma dersem, rakamlardan biri doğru ama yanlış pozisyonda.
    Armut dersem rakamlardan biri doğru ve doğru pozisyonda.
    Mısır dersem ise karavana :-)
    '''.format(NUM_DIGITS)) # {} ile işaret edilen yere NUM_DIGITS değeri gelecektir.
    print()

"""
Aşağıdaki fonksiyon oyunun ihtiyacı olan rastgele sayıyı üretir.
"""
def get_game_number():
    numbers=list('0123456789') # Önce rakamları taşıyan bir liste
    random.shuffle(numbers) # sayıları güzelce bir karşıtırır
    secret_number=''
    for i in range(NUM_DIGITS): # 4 atımlık bir döngü
        secret_number+=str(numbers[i]) # sırayla sayılar secret_number değişkeninde ardışıl toplanır
    return secret_number # dört haneli sayı geriye döner

if __name__ == '__main__':
    main()