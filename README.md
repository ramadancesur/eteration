# Eteration Academy Test Projects

Bu repository, Eteration Academy için test projelerini içerir.

## 1. Selenium Test Otomasyonu

### Test Senaryoları

1. **Eğitmen Listesi Testi**: 
   - Eğitmenler sayfasına gider
   - Eğitmen listesinin boş olmadığını kontrol eder
   - Bulunan eğitmen sayısını raporlar

2. **Newsletter Abonelik Testi**:
   - Ana sayfaya gider
   - Newsletter bölümünü bulur
   - Test email adresi girer
   - Formu gönderir

### Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

2. Chrome WebDriver'ın yüklü olduğundan emin olun (webdriver-manager otomatik olarak yükleyecektir)

### Testleri Çalıştırma

Tüm testleri çalıştırmak için:
```bash
python test_eteration_academy.py
```

### Gereksinimler

- Python 3.x
- Selenium WebDriver
- Chrome Tarayıcı

## 2. Manuel Test Senaryoları

Detaylı manuel test senaryoları için `Google_Test_Cases.xlsx` dosyasına bakınız.
