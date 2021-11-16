import random

'''
Bir python modülünü projeye yüklerken sorun oluşma ihtimaline karşı try bloğu kullanabiliriz.
pyperclip paketini clipboard'a içerik kopyalamak için kullanacağız.
Sistemde paket yüklü değilse pass ile program akışına devam edecek.
'''

try:
    import pyperclip
except ImportError:
    pass