#.py uzantılı bir dosya oluştur
# Kurulum:  pip install PyPDF2
# ÖNEMLİ NOT : Gerekli kütüphanenin yüklü olması gerek ve pdf dosyalarının kodun çalıştığı klasörle aynı
# klasörde olması gerekli ayrıca pdf ler sıralanırken 01,02 ...10,11... şeklinde devam etmeli buna dikkat edilmezse
# pdfleri karışık şekilde topluyor.
import glob
from PyPDF2 import PdfMerger



# Aynı klasördeki tüm .pdf dosyalarını al
pdf_list = glob.glob("*.pdf")

# İsimleri sıralayalım (01.pdf, 02.pdf, 03.pdf gibi)
pdf_list.sort()

print("Bulunan PDF dosyaları:")
for i, f in enumerate(pdf_list, 1):
    print(f"{i}. {f}")

merger = PdfMerger(strict=False)

for f in pdf_list:
    merger.append(f)

merger.write("birlesik.pdf")
merger.close()

print("\n✓ İşlem tamam! -> birlesik.pdf")
