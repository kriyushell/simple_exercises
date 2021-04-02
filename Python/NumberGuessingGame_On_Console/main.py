"""
Kodda herhangi bir hata veya
daha iyi bir cozumu oldugunu dusunuyorsaniz
bana discord adresimden ulasabilirsiniz.
DiscordAdresim: R4mp4g3#4290
"""


from random import randint

def Game(START=1, STOP=100, kalanHak=10):
    rasgeleSayi = randint(START, STOP)

    print("######### Sayi Tahmin oyununa Hosgeldiniz #########")
    print(f"{START} ile {STOP} arasında bir Sayi tuttum.", end=" ")
    while (kalanHak):
        try:
            tahmin = int(input("Haydi tahmin et: "))
        except (ValueError):
            print(f"Lutven sadece {START} ile {STOP} arasinda bir tam sayi gir!")
            continue

        if tahmin == rasgeleSayi:
            print("Tebrikler Kazandiniz !")
            print(f"{10 - kalanHak + 1} tahminde dogru cevabi buldunuz. ")
            if input("Tekrar oynamak istermisiniz? (e/h): ").lower() == "e":
                return True
            else:
                return False
        elif tahmin > rasgeleSayi:
            print("Yanlis tahmin. biraz daha kucuk bir sayi denemelisin.")
        else:
            print("Yanlis tahmin. biraz daha buyuk bir sayi denemelisin.")

        kalanHak -= 1
        print(f"Kalan hak: {kalanHak}\n\n")

    else:
        print("Maglesef hic hakkin kalmadi :(")
        if input("Tekrar oynamak istermisin? (e/h)").lower() == "e":
            return True
        else:
            return False

if __name__ == '__main__':
    tekrarOynanicakMi = Game()
    while tekrarOynanicakMi:
        print("\n"*20)
        tekrarOynanicakMi = Game()
