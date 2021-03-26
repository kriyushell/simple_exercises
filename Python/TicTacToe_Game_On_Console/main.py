"""
Kodda herhangi bir hata veya
daha iyi bir çözümü oldugunu dusunuyorsanı
bana discord adresimden ulaşabilirsiniz.
DiscordAdresim: R4mp4g3#4290
"""




tahta = [
    ["___", "___", "___"],
    ["___", "___", "___"],
    ["___", "___", "___"]
]
def tahtayiGoster():
    print("\n" * 3)
    for satir in tahta:
        print("\n\t".expandtabs(20), *satir, sep=" " * 2)
    print("\n" * 3)



titleText = "################## XOX Oyununa Hosgeldiniz. ##################"
print(titleText)
tahtayiGoster()

kazanmaKosullari = (
    ((0,0), (0,1), (0,2)),
    ((1,0), (1,1), (1,2)),
    ((2,0), (2,1), (2,2)),
    ((0,0), (1,0), (2,0)),
    ((0,1), (1,1), (2,1)),
    ((0,2), (1,2), (2,2)),
    ((0,0), (1,1), (2,2)),
    ((0,2), (1,1), (2,0)),
)

x_durum, o_durum = [], []
sira = 0


while True:
    oyuncu = "X" if sira % 2 == 0 else "O"


    print("Ornek input: 1,2")
    print(f"Sira: {oyuncu}")
    kordinatlar = input("Lutven oyniyacagınız yerin kordinatlarini giriniz.(cikis icin 'exit' yaziniz.)\nx,y: ")
    if kordinatlar.lower() == "exit":
        print("Cikiliyor...")
        quit()


    hata_mesaji = """\
HATA ! 
    Lutven verilen formata uygun kordinat giriniz."
    Format: x,y
    (1 <= x <= 3) and (1 <= y <= 3)
    Ornek: 3,2
    """
    try:
        x, y = map(int, kordinatlar.split(","))
        x, y = x - 1, y -1


        if tahta[y][x] != "___":
            print("\n" * 3)
            print("Girdiginiz kordinat dolu! lutven baska kordinat giriniz")
            tahtayiGoster()
            continue
        else:
            tahta[y][x] = oyuncu.center(3)
            tahtayiGoster()

            oyuncu_durumu = {"X": x_durum, "O": o_durum}[oyuncu] # type(oyuncu_durumu): list
            oyuncu_durumu += [(y, x)]

    except (ValueError, IndexError):
        print(hata_mesaji)
        continue
    else:
        sira += 1


    for kosul in kazanmaKosullari:
        oyuncuHamleleri = tuple(i for i in oyuncu_durumu if i in kosul)
        if len(oyuncuHamleleri) < 3: continue


        kazanma_durumu = True
        for i in oyuncuHamleleri:
            if i not in kosul:
                kazanma_durumu = False

        if kazanma_durumu:
            print(f"{oyuncu} KAZANDI !")
            input()
            quit()
