# PythonGiller

Python bilgilerimi eğlenceli bir şekilde hatırlamak ve daha da geliştirmek için [__The Big Book of Small Python Projects__](https://nostarch.com/big-book-small-python-projects) isimli bir kitap almıştım. Ne zamandır çalışacağım çalışacağım derken en sonunda kapağını açmayı başardım. Repo'daki amacım kitaptaki örnek programları her zaman olduğu gibi copy-paste yapmadan, biraz değiştirerek ama daha da önemlisi anlamaya çalışıp gerekli yorum satırlarını da ekleyerek çalışmak. İç motivasyonla yeni bir oyun alanı oluşturduğum için mutluyum. Örnekleri Windows 10 yüklü bir sistemde Visual Studio Code editörünü kullanarak yapmaktayım. Sistemde python yüklü tabii ki :)

## Sayı Tahmin Oyunu _(Bagels)_

Oyun 4 basamaklı bir sayıyı tahmin etmemiz istiyor. Belli sayıda deneme hakkımız var. Matematiksel olarak tümdengelim yaklaşımı baz alınıyor. Şöyle ki,

- Tahmin ettiğimiz rakam doğru ama sayının yanlış yerindeyse _Elma_
- Tahmin ettiğimiz rakam hem doğru hem değru yerdeyse _Armut_
- Tahmin ettiğimiz rakam sayıda yoksa _Mısır_
- Deneme hakkımızda 20 olsun.

Oyunun çalışma zamanı çıktısı aşağıdakine benzer.