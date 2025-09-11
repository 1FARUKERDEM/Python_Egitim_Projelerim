import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



target_url = "test url"
foundLinks = []

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

from urllib.parse import urljoin

def crawl(url):
    soup = make_request(url)
    for a in soup.find_all('a'):
        href = a.get('href')
        if not href:
            continue

        if "#" in href:
            href = href.split("#")[0]

        absolute = urljoin(url, href)  # relative -> absolute

        if absolute.startswith(target_url) and absolute not in foundLinks:
            foundLinks.append(absolute)
            print(absolute)
            crawl(absolute)


crawl(target_url)


# ========================== HATIRLATMA BLOĞU ==========================
# Bu kod ne yapıyor?
# -> Basit bir web crawler. Başlangıç URL’sinden girer, bütün <a href="...">
#    linklerini toplar, aynı domain’de olanları takip eder ve tekrar tarar.

# Adımlar:
# 1. requests.get(url) → HTML sayfayı indirir.
# 2. BeautifulSoup(response.text, "html.parser") → HTML’i parse eder.
# 3. soup.find_all('a') → sayfadaki bütün <a> etiketlerini bulur.
# 4. link.get('href') → her linkin adresini alır.
# 5. "#" varsa → split("#")[0] ile temizler (aynı sayfa içi linkleri ayıkla).
# 6. urljoin(url, href) → relative linkleri absolute linke çevir.
# 7. absolute.startswith(target_url) → sadece aynı siteye ait linkleri al.
# 8. Daha önce eklenmemişse foundLinks listesine ekler ve ekrana basar.
# 9. crawl(absolute) → fonksiyon kendini çağırır (recursive) → yeni sayfaya da girer.

# Neden böyle?
# - Recursive yapı → siteyi “ağaç gibi” dallanarak taramak için.
# - foundLinks listesi → aynı linki tekrar tarayıp sonsuz döngüye girmemek için.
# - urljoin → site içindeki "catalogue/..." gibi relative linkleri tam URL yapar.
# - "#" temizliği → aynı sayfanın farklı anchor’larını tekrar saymamak için.

# Olası geliştirmeler:
# - foundLinks'i list değil set yapmak → hızlı üyelik kontrolü.
# - Derinlik limiti eklemek → çok büyük sitelerde çökmesin.
# - Hata yakalama (try/except) → bağlantı koparsa program patlamasın.
# - robots.txt kontrolü → etik tarama kurallarına uyum.
# ======================================================================
