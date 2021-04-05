from random import randint
"""
Kodda herhangi bir hata veya
daha iyi bir cozumu oldugunu dusunuyorsaniz
bana discord adresimden ulasabilirsiniz.
DiscordAdresim: R4mp4g3#4290
"""


benimSkor = oyuncuSkor = 0
def kazanma_kontrolu(hamle_1, hamle_2):
    global benimSkor, oyuncuSkor
    kazanma_kosullari = {  # 0: tas, 1:kagit, 2:makas
        (0, 2): "Tas Makasi kirar.",
        (1, 0): "Kagit Tasi sarar.",
        (2, 1): "Makas Kağıtı keser.",
    }

    if hamle_1 == hamle_2:
        return "Berabere"

    oyunDurumu = kazanma_kosullari.get((hamle_1, hamle_2), False)
    if oyunDurumu:
        benimSkor += 1
        return oyunDurumu + " Ben Kazandim."
    else:
        oyuncuSkor += 1
        return kazanma_kosullari.get((hamle_2, hamle_1)) + " Tebrikler Sen kazandin!."




def oyun():
    global benimSkor, oyuncuSkor
    print("############### Tas Kagit Makas Oyununa Geldiniz. ###############\n")
    elemanlar = ("Tas", "Kagit", "Makas")

    rasgeleIndex = randint(0, 2)
    while True:
        print("\t".expandtabs(20), f"Senin Skorun: {oyuncuSkor}")
        print("\t".expandtabs(20), f"Benim Skorum: {benimSkor}")
        print('\n' * 2)

        secim = input("Tas(1)\nKagit(2)\nMakas(3)\nCikis(0)\nsecim: ")
        if secim == '0':
            print("Cikiliyor", end="")
            for i in range(5):
                __import__('time').sleep(.5)
                print('.', end='', flush=True)
            break
        elif secim in ('1', '2', '3'):
            secimIndex = int(secim) - 1
            print("\nSenin Hamlen: {}\nBenim Hamlem: {}".format(
                elemanlar[secimIndex],
                elemanlar[rasgeleIndex]
            ))
            oyun_durumu = kazanma_kontrolu(rasgeleIndex, secimIndex)
            print(f"Oyun durumu: {oyun_durumu}", end="\n"*2)
        else:
            print("Hatali giris!")
            continue
        rasgeleIndex = randint(0, 2)



if __name__ == '__main__':
    oyun()
