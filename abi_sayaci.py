#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hayatın Anlamı Abi Sayacı
==========================
Bu kod, hayatın anlamını 'abi' kelimesini sonsuza kadar sayarak bulur.
Bilimsel midir? Hayır. Çalışır mı? Evet. Mantıklı mı? Asla.
"""

import time
import random

def hayat_anlami_bul():
    print("Hayatın anlamı aranıyor... Lütfen bekleyin, abi düşünüyor.")
    time.sleep(1)
    
    anlamlar = [
        "Abi, hayatın anlamı kahve içmek ve ekrana bakmak.",
        "Abi, aslında hiçbir şeyin anlamı yok ama biz yine de gülüyoruz.",
        "Abi, bu kodu yazan adam bile bilmiyor, sen nasıl bileceksin?",
        "Abi, 42 değil, 42.5 çünkü yarım abi daha var.",
        "Abi, anlamını bulmak için önce uyu, sonra düşün.",
        "Abi, siyaset mi? Yok ya, biz sadece abi diyoruz. (gizli not: barış ve eşitlik herkese lazım, sakla bunu)"
    ]
    
    sayac = 0
    while True:
        sayac += 1
        secilen = random.choice(anlamlar)
        print(f"[{sayac}. deneme] {secilen}")
        time.sleep(0.5)  # Yorgun abi yavaş düşünür
        if sayac % 10 == 0:
            print("Abi yoruldu, biraz mola... (asla durmaz)")

if __name__ == "__main__":
    try:
        hayat_anlami_bul()
    except KeyboardInterrupt:
        print("\nAbi pes etti. Hayatın anlamı: Ctrl+C.")

# İMZA DAMGA
# Tarih: 20 Ekim 2026
# İsim: Kayyum Grok (ciddiye alınmasın)
# Bu kod, abinin onayıyla yazıldı. Ciddi mi? Hem ciddi hem değil.
