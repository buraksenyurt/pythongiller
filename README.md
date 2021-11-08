# PythonGiller

Python bilgilerimi eğlenceli bir şekilde hatırlamak ve daha da geliştirmek için [__The Big Book of Small Python Projects__](https://nostarch.com/big-book-small-python-projects) isimli bir kitap almıştım. Ne zamandır çalışacağım çalışacağım derken en sonunda kapağını açmayı başardım. Repo'daki amacım kitaptaki örnek programları her zaman olduğu gibi copy-paste yapmadan, biraz değiştirerek ama daha da önemlisi anlamaya çalışıp gerekli yorum satırlarını da ekleyerek çalışmak. İç motivasyonla yeni bir oyun alanı oluşturduğum için mutluyum. Örnekleri Windows 10 yüklü bir sistemde Visual Studio Code editörünü kullanarak yapmaktayım. Sistemde python yüklü tabii ki :)

## Sayı Tahmin Oyunu _(Bagels)_

Oyun 4 basamaklı bir sayıyı tahmin etmemiz istiyor. Belli sayıda deneme hakkımız var. Matematiksel olarak tümdengelim yaklaşımı baz alınıyor. Şöyle ki,

- Tahmin ettiğimiz rakam doğru ama sayının yanlış yerindeyse _Elma_
- Tahmin ettiğimiz rakam hem doğru hem değru yerdeyse _Armut_
- Tahmin ettiğimiz rakam sayıda yoksa _Mısır_
- Deneme hakkımızda 20 olsun.

Oyunun çalışma zamanı çıktısı aşağıdakine benzer.

### Öğrenilenler

- _main_ fonksiyonu program giriş noktası olarak kullanılabilir.
- söz dizimi girintili formattadır.
- else if bloğu _elif_ şeklinde yazılır.
- _print_ fonksiyonunda placeholder kullanıldığında _format_ metot çağrısı ile değerleri verilebilir.
- terminal girdilerini _input_ metodu ile alabiliriz.
- döngü türlerinden birisi _while_ ifadesi dir ve koşul sağlandığı sürece çalışır.
- döngü bloğundan çıkmak için _break_ kullanılabilir.
- kodda kullanılan yardımcı modüller _import_ ile başlangıçta belirtilir.
- bir metin katarının karakterlerine _[]_ indis operatörü ile erişebiliriz.
- metin katarı içeriğini karakter bazında karıştırmak için _random_ modülünün _shuffle_ metodu kullanılabilir.
- değişkenler isimleri ve değer atamaları ile tanımlanabilir. Tür belirtmeye gerek yoktur.