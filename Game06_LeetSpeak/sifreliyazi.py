import random, sys
from termcolor import colored
'''
Bir python modülünü projeye yüklerken sorun oluşma ihtimaline karşı try bloğu kullanabiliriz.
pyperclip paketini clipboard'a içerik kopyalamak için kullanacağız.
Sistemde paket yüklü değilse pass ile program akışına devam edecek.
'''

try:
    import pyperclip
except ImportError:
    pass

# Harflerin karşılıkları olan leet sembollerini bir dictionary'de aşağıdaki gibi tutabiliriz.
# Bazı harf karşılıkları görüldüğü üzere bir array ile ifade edilmektedir.
leet_map = {
    'a': ['4', '@', '/-\\'],
    'c': ['('],
    'd': ['|)'],
    'e': ['3'],
    'f': ['ph'],
    'h': [']-[', '|-|'],
    'i': ['1', '!', '|'],
    'k': [']<'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['7', '+'],
    'u': ['|_|'],
    'v': ['\\/']
}

# bonus olarak birde mors koduna dönüştürmekte kullanılacak koleksiyonu ekleyelim.
morse_map = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '_..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}

print(
    colored(
        '''
    Seninle istediğin kadar buradayım. Bana bir cümle yaz ve sana LeetSpeakçesini söyleyeyim.
    
    Ne yazık ki şimdilik cümlelerini İngilizce yazmalısın.
    
    Programdan çıkmak istersen E yazıp ışınla.''', "yellow"))

# Sonsuz döngümüz burada başlatılıyor.
while True:
    message = input(colored("Your Message..: ",
                            "cyan"))  # Kullanıcının girdiği mesajı alıyoruz.

    if message.lower() == 'e':
        print(colored('Görüşmek üzereeee. Yine gel.\a', 'blue'))
        sys.exit()

    # pyperclip yüklü ise copy ile mesaj içeriğini Clipboard'a alıyoruz
    try:
        pyperclip.copy(message)
        print("Mesajını zihnime kopyaladım.")
    except NameError:  # yüklü değilse bir NameError istisnası oluşacaktır
        pass  # görmezden gelip kod akışının devam etmesini sağlıyoruz

    # çıktıları toplayacağımız değişkenler
    leet_result = ''
    morse_result = ''

    # girilen mesaj içerisindeki herbir karakteri dolaşıyoruz
    for char in message:
        # eğer sıradaki harf mors karakter setinde varsa onun karşılığını ekliyoruz. Yoksa yerine boşluk koyuyoruz.
        if char.lower() in morse_map:
            morse_result = morse_result + morse_map[char.lower()]
        else:
            morse_result = morse_result + ' '

        # Buradaki kıyaslamamız ise biraz daha farklı.
        # sıradaki harf leet karakter setinde %70 olasılıkla varsa değiştiriyoruz
        if char.lower() in leet_map and random.random() <= 0.70:
            # bazı harfler için birden fazla leet seçeneği söz konusu            
            candidates = leet_map[char.lower()]
            # onlardan rastgele birisini alıyoruz. Zaten bir tane ise kendisi gelecektir.
            leet_char = random.choice(candidates)
            # string katarının arkasına ekliyoruz
            leet_result = leet_result + leet_char
        else:
            # eğer ilgili harf leet karakter setinde yoksa olduğu gibi ekliyoruz.
            leet_result = leet_result + char

    print(colored('''{}\n\n{}'''.format(leet_result, morse_result), "magenta"))
