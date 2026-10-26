from difflib import SequenceMatcher

def yaqin(a, b):
    return SequenceMatcher(None, a, b).ratio() >= 0.7
sozlar = {}
with open("sozlar.txt", encoding="utf-8") as f:
    for qator in f:
        qator = qator.strip()
        if qator:
            yapon, tarjima = qator.split(",", 1)
            sozlar[yapon] = tarjima

import random

ball = 0
xatolar = []

yuqoridagi = list(sozlar.items())
random.shuffle(yuqoridagi)

for yapon, tarjima in yuqoridagi:
    javob = input(f"{yapon} nima degani? ")
    if yaqin(javob.lower().strip(), tarjima):
        print("To'g'ri!")
        ball += 1
    else:
        print(f"Xato. To'g'ri javob: {tarjima}")
        xatolar.append((yapon, tarjima))

print(f"\nTest tugadi! Natija: {ball}/{len(sozlar)}")

if xatolar:
    print("\nXato qilgan so'zlaringni qayta takrorlaymiz:")
    for yapon, tarjima in xatolar:
        javob = input(f"{yapon} nima degani? ")
        if yaqin(javob.lower().strip(), tarjima):
            print("To'g'ri!")
        else:
            print(f"Yana xato. To'g'ri javob: {tarjima}")