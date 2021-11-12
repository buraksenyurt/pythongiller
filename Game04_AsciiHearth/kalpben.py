from termcolor import colored
import random, sys

# Oyunda amaç oyuncunun girdiği kısa kelimeyi aşağıdaki kalp resminde görünen * sembolleri yerine yerleştirmek.
# Bunu yaparken işi eğlenceli kılmak için oyuncudan birde renk seçmesini isteyeceğiz.

bitmap = """
........................................
               * 
             *   *
           *      *
          *        *
         *         *    *  *
        *           *  *      *
        *            *         *
         *           *         *
          *                   *
           *                 *
            *               *
             *             *
               *          *
               *         *
                *       *
                 *     *
                  *   *
                    *
                   *
                  *
                 *
                  *
                   *
                  *
                 *
                *
                 *
                  *
........................................
"""

print(
    colored(
        """
    Merhabalar :) Ne güzel bir gün değil mi? Senin için bir resim çizmek isterim.
    
    Bana sevdiğin bir rengi söyler misin? (red, yellow, magenta, green, white, blue, cyan, gray)
""", "magenta"))

colors = ["RED", "YELLOW", "MAGENTA", "GREEN", "WHITE", "BLUE", "CYAN", "GRAY"]

# Doğru rengi yazana kadar onu gıcık ediyoruz :)
# Bunun için yine sonsuz bir döngümüz var girilen bilginin colors isimli string dizide olup olmadığına bakarak akışı yönlendiriyoruz.
while True:
    # Oyuncudan bir renk seçmesini istiyoruz
    user_color = input('..: ').upper()

    if user_color not in colors:
        print(
            colored(
                'Lütfen şunlardan birini yaz. red, yellow, magenta, green, white, blue, cyan, gray...',
                "red"))
    else:
        break

print(
    colored(
        "Şimdi tam beş harften oluşan bir mesaj yazar mısın? Eğer çıkmak istersen bir şey yazmadan enter'a basman yeterli.",
        "yellow"))

# Şimdi de oyuncuyu tam 5 karakterlik bir şeyler girmeye zorluyoruz
while True:
    user_message = input('..: ')
    # Kullanıcı hiçbir şey girmeden enter'a basarsa programdan çıkıp sisteme dönüyoruz.
    if user_message == '':
        sys.exit()

    if len(user_message) != 5:
        print(colored('Lütfen tam 5 karakterden oluşan bir şeyler yaz', 'red'))
    else:
        break

# Döngümüz bitmap içeriğini satır bazında parçalayarak başlıyor
for line in bitmap.splitlines():
    # her satır için enumerate fonksiyonunu kullanarak satırdaki tüm karakterleri dolaşabiliriz.
    # i ile satırdaki sütun numarasını, c ile de oradaki karakteri yakalıyoruz.
    for i, c in enumerate(line):
        # karakter boşluğa denk gelmişse yine boşluk atıyoruz
        if c == ' ':
            print(' ', end='')
        else:
            # ama * veya . sembolüne denk gelmişsek oyuncunun girdiği kelimeden modül alma operatörünü de kullanarak bir harf yakalayıp yerleştiriyoruz.
            print(colored(user_message[i % len(user_message)],
                          user_color.lower()),
                  end='')
    print() # iç döngü bitince bir alt satıra geçerek devam ediyoruz