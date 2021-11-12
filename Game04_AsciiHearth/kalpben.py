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
""", "blue"))
# Oyuncudan bir renk seçmesini istiyoruz
user_color = input('..: ').upper()

colors = ["RED", "YELLOW", "MAGENTA", "GREEN", "WHITE", "BLUE", "CYAN", "GRAY"]

# Doğru rengi yazana kadar onu gıcık ediyoruz :)
# Bunun için yine sonsuz bir döngümüz var girilen bilginin colors isimli string dizide olup olmadığına bakarak akışı yönlendiriyoruz.
while True:
    if user_color not in colors:
        print(
            colored(
                'Lütfen şunlardan birini yaz. red, yellow, magenta, green, white, blue, cyan, gray...'
            ), "blue")
    else:
        break

print(
    colored(
        "Şimdi beş harfi geçmeyecek bir mesaj yazar mısın? Eğer çıkmak istersen bir şey yazmadan enter'a basman yeterli.",
        "yellow"))

user_message = input('..: ')
# Kullanıcı hiçbir şey girmeden enter'a basarsa programdan çıkıp sisteme dönüyoruz.
if user_message == '':
    sys.exit()

# Şimdi de oyuncuyu tam 5 karakterlik bir şeyler girmeye zorluyoruz
while True:
    if user_message.len() != 5:
        print(colored('Lütfen tam 5 karakterden oluşan bir şeyler yaz', 'red'))
    else:
        break
