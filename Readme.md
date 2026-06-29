# Mini KGYS Simülasyonu

## Proje Hakkında

Bu proje, gerçek KGYS (Kent Güvenlik Yönetim Sistemi) altyapılarının küçük ölçekli bir simülasyonunu geliştirmek amacıyla hazırlanmıştır.

Sistem; ağ altyapısı, IP kamera sistemleri, Linux sunucu yönetimi, monitoring, alarm üretimi ve NVR kayıt mantığını bir araya getirmektedir.

## Amaç

Gerçek dünyadaki KGYS sistemlerinin temel çalışma mantığını öğrenmek ve uygulamak.

Bu proje kapsamında aşağıdaki alanlarda deneyim kazanılması hedeflenmektedir:

* Ağ yönetimi
* Switch altyapıları
* IP kamera sistemleri
* Linux sunucu yönetimi
* Monitoring sistemleri
* NVR mantığı
* Log yönetimi
* Alarm mekanizmaları
* IoT cihaz entegrasyonu

## Sistem Mimarisi

ESP32-CAM cihazları saha kameraları olarak görev yapacaktır.

Kameralar switch üzerinden Ubuntu Server çalıştıran merkezi sunucuya bağlanacaktır.

Sunucu üzerinde:

* Monitoring servisi
* Alarm yöneticisi
* NVR kayıt sistemi
* SQLite veritabanı
* Flask dashboard

çalışacaktır.

## Kullanılan Teknolojiler

* ESP32-CAM
* Ubuntu Server
* Python
* Flask
* SQLite
* OpenCV
* FFmpeg
* Git
* GitHub

## Proje Yapısı

* docs → Dokümantasyon
* dashboard → Web arayüzü
* monitoring → Cihaz izleme servisleri
* nvr → Kayıt sistemi
* database → Veritabanı işlemleri
* config → Yapılandırma dosyaları
* recordings → Kamera kayıtları
* tests → Test senaryoları

## Yol Haritası

* [x] Git ve GitHub kurulumu
* [x] Proje klasör yapısı
* [x] İlk dokümantasyon
* [ ] Ubuntu Server kurulumu
* [ ] Flask Dashboard
* [ ] Monitoring sistemi
* [ ] Alarm sistemi
* [ ] NVR sistemi
* [ ] Sistem entegrasyonu

