# -*- coding: utf-8 -*-
import sys

path = r"C:\Users\emres\OneDrive\Belgeler\UiPath\extract-trackid-automation\Main.xaml"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Eski regex: [\r\n]+ zorunlu satır sonu var — Trendyol'da satır sonu yok, bu yüzden boş geliyor
old = r'Takip\s*Et\s*[\r\n]+(.+?)(?:[\r\n]|Aşağıda|Takip Numaras[ıi])'
# Yeni regex: satır sonu zorunluluğunu kaldır
new = r'Takip\s*Et\s*(.+?)(?:Aşağıda|Takip Numaras[ıi]|[\r\n])'

if old in content:
    content = content.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("BASARILI: strKargoDurumu regex guncellendi.")
    print("Eski: " + old)
    print("Yeni: " + new)
else:
    print("UYARI: Eski ifade bulunamadi!")
    # Debug: mevcut Takip Et satırını bul
    idx = content.find("Takip\\s*Et")
    if idx >= 0:
        snippet = content[idx:idx+150]
        print("Mevcut: " + snippet)
    else:
        print("'Takip\\s*Et' ifadesi de bulunamadi.")
