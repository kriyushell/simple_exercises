# questions https://github.com/R4mp4g3-0/simple_exercises/blob/main/README.md at this address
"""
sorular için daha iyi bir çözüm bulursaniz discord'dan bana ulasabilirsiniz,
sizin çözümünüzüde eklerim.
discrod hesabim: Kriyushell#4290

not: bu dosya daha sonra guncellenebilir.
"""

# cozum fonksiyonlari
def solution_for_question1() -> None:

    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    num3 = float(input("Third Number: "))

    ########## python gömülü fonksiyonu kullanalarak ##########
    # print("Largest Number: {}".format(max(num1, num2, num3)))
    ###########################################################

    # benim mantığıma göre;
    if (num1 == num2 == num3):
        print("Largest Number: {}".format(num1))
        return


    if (num1 > num2) and (num1 > num3):
        print("Largest Number: {}".format(num1))
        return
    elif (num2 > num1) and (num2 > num3):
        print("Largest Number: {}".format(num2))
        return
    elif (num3 > num1) and (num3 > num2):
        print("Largest Number: {}".format(num3))
        return


    if ( (num1 == num2) and (num1 > num3) ) or ( (num1 == num3) and (num1 > num2) ):
        print("Largest Number: {}".format(num1))
        return
    elif (num2 == num3) and (num2 >num1):
        print("Largest Number: {}".format(num2))
        return


"""Solution1 Fonc. End"""


def solution_for_question2() -> None:
    def myEbobFonc(A: int, B: int) -> int:
        """
        Ebob, en buyuk ortal bolen anlamina gelir
        """
        ebob = 1
        for i in range(1, max(A, B) + 1):
            if ((A % i) == 0) and ((B % i) == 0):
                ebob = i
        return ebob
    """MY EBOB FONK. END"""
    def myEkokFonc(A: int, B: int) -> int:
        """
        Ekok, en küçük ortak kat anlamina gelir
        """
        if A == B == 1: return 1
        for i in range(2, A * B):
            if ((i % A) == 0) and ((i % B) == 0):
                return i
    """MY EKOK FONK. END"""

    #  Another result with the oclid algorithm

    def obeb(a: int, b: int):
        """
        kaynak;
        https://tr.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
        """
        if b > a:
            return obeb(b, a)

        while b:
            a, b = b, a % b
        return a
    """FONC. END"""
    def okek(a: int, b: int):
        return a*b // obeb(a, b)
    """FONC. END"""

    # import the reduce fonk.
    from functools import reduce
    def oklidAlgObeb(*args):
        return reduce(obeb, args)

    def oklidAlgOkek(*args):
        return  reduce(okek, args)


    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))

    # my solution
    ebob = myEbobFonc(num1, num2)
    ekok = myEkokFonc(num1, num2)
    print(f"EBOB({num1}, {num2}) = {ebob}")
    print(f"EKOK({num1}, {num2}) = {ekok}")

    # Another result with the oclid algorithm
    print("Another result with the oclid algorithm;")
    secEbob = oklidAlgObeb(num1, num2)
    secEkok = oklidAlgOkek(num1, num2)
    print(f"EBOB({num1}, {num2}) = {secEbob}")
    print(f"EKOK({num1}, {num2}) = {secEkok}")

    # Another result with python built in func.
    print("Another result with python built in func;")
    from math import gcd
    thirdEbob = gcd(num1, num2)
    thirdEkok = abs(a*b) // gcd(a, b)
    print(f"EBOB({num1}, {num2}) = {thirdEbob}")
    print(f"EKOK({num1}, {num2}) = {thirdEkok}")



"""Solution2 Fonc. End"""

def solution_for_question3() -> None:
    num = int(input("Plase enter a number: "))
    sumNumber = 0

    for i in range(1, num):
        if (num % i) == 0:
            sumNumber += i

    if sumNumber == num: print("the number is perfect number.")
    else: print("the number isn't perfect number.")

    #
    # print("the number is perfect number." if sum((i for i in range(1, num) if num % i == 0))==num else "the number isn't perfect number.")
    #
"""Solution3 Fonc. End"""


def solution_for_question4() -> None:
    num = int(input("Plase enter a number: "))
    print("3 ve 5'e tam bolunuyor" if (num % 3*5 == 0) else "3 ve 5'e tam bolunmuyor")
"""Solution4 Fonc. End"""

def solution_for_question5() -> None:
    num = int(input("lütven 0 ile 99,999 arasında bir tam sayı giriniz: "))
    while not (num > 0 and num <= 99_999):
        print("lutven dogru aralikta sayi girdiginizden emin olun.")
        num = int(input("0 ile 99,999 arasinda bir tam sayi giriniz: "))

    basamaklar = ("onbinler", "binler", "yuzler", "onlar", "birler")
    strNum = str(num)
    for i in range(len(strNum)):
        print(f"{basamaklar[i]} basamaigi: {strNum[i]}")

"""Solution5 Fonc. End"""


def solution_for_question6() -> None:
    num = input("lütven 3 basamakli bir tam sayı giriniz: ")
    while len(num) != 3:
        num = int(input("3 basamakli bir tam sayi giriniz: "))
    num = int(num)

    basamaklar = ("birler", "onlar", "yuzler")
    for basamak in basamaklar:
        print(f"{basamak} basamagi: {num % 10}")
        num = num // 10
"""Solution6 Fonc. End"""

def solution_for_question7() -> None:
    num = input("Plase enter a integer number: ")
    exponential = len(num)

    total = 0
    for i in num: total += int(i) ** exponential
    print("The number entered is the Armstrong number." if total == int(num) else "The number entered is not a Armstrong number.")

"""Solution7 Fonc. End"""

def solution_for_question8() -> None:
    """
    v = x / t
    hiz = mesafe / zaman
    t = x / v
    """
    v = 60
    x = int(input("Mesafe girin: "))
    t = x / v
    print(f"{x} km yolu arac {t} saatte gider.")
"""Solution8 Fonc. End"""

def solution_for_question9() -> None:
    maas = int(input("Maasi giriniz: "))
    cSayisi = int(input("Cocuk Sayisini giriniz: "))
    while cSayisi < 0:
        cSayisi = int(input("Cocuk Sayisini giriniz: "))

    if cSayisi == 0: pass
    elif cSayisi == 1: maas = maas + maas * 0.05
    elif cSayisi == 2: maas = maas + maas * 0.1
    else: maas = maas + maas * 0.15

    print("iscinin toplam geliri = {0}".format(maas))

"""Solution9 Fonc. End"""

def solution_for_question10() -> None:
    r = int(input("Dairenin yari capini giriniz: "))
    pi = 3.14

    (cevre, alan) = (2*pi*r), (pi*r*r)
    print(f"dairenin alani = {alan}\ndairenin cevresi = {cevre}")

"""Solution10 Fonc. End"""

def solution_for_question11() -> None:
    num = int(input("Bir sayi giriniz: "))
    bolenler = []

    for i in range(1, num + 1):
        if (num % i) == 0:
            bolenler.append(i)

    print(f"{num} sayisinin tam bolenleri:", *bolenler)

"""Solution11 Fonc. End"""

def solution_for_question12() -> None:
    num = int(input("Bir sayi giriniz: "))

    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} asal sayi degildir.")
            break
    else:
        print(f"{num} asal bir sayidir.")

"""Solution12 Fonc. End"""

def solution_for_question13() -> None:
    n = int(input("Birden kaça kadar asal sayilari bilmek istiyorsun?: "))

    asallar = []
    for i in range(2, n):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            asallar.append(i)

    print(f"bir ile {n} arasindaki asal sayilar:", *asallar)

"""Solution13 Fonc. End"""

def solution_for_question14() -> None:
    num1 = int(input("Birinci tam sayi: "))
    num2 = int(input("ikinci tam sayi : "))

    if (num1 > 0 and  num2 > 0) and ((num1 - num2) in (2, -2)):

        for num in (num1, num2):
            for i in range(2, num):
                if (num % i) == 0:
                    print(f"{num1},{num2} ikiz asallar degildir.")
                    return
        else:
            print(f"{num1}, {num2} ikiz asallardir.")
    else:
        print(f"{num1}, {num2} ikiz asallar degildir.")


"""Solution14 Fonc. End"""

def solution_for_question15() -> None:
    # 1.yol
    def factorialFirstWay(num: int) -> int:
        carpim = 1
        for i in range(2, num + 1):
            carpim *= i
        return carpim

    # 2.yol
    def factorialSecondWay(num: int) -> int:
        if 0 <= num <= 1:
            return 1
        else:
            return num * factorialSecondWay(num - 1)


    number = int(input("Bir sayi giriniz: "))
    fac  = factorialFirstWay(number)
    fac2 = factorialSecondWay(number)

    if fac == fac2:
        print(f"{number}! = {fac}")

"""Solution15 Fonc. End"""

def solution_for_question16() -> None:
    """
    C = (F-32) / 1.8
    F = (1.8*C) + 32
    """
    choice = input("(1) Fahrenheit to Celsius\n(2) Celsius to Fahrenheit\nchoice: ")

    if choice == "1":
        F = int(input("Fahrenheit: "))
        C = (F-32) / 1.8
        print(f"{F} Fahrenheit is {C} Celsius")
    elif choice == "2":
        C = int(input("Celsius: "))
        F = (1.8*C) + 32
        print(f"{C} Celsius is {F} Fahrenheit")


"""Solution16 Fonc. End"""

def solution_for_question17() -> None:
    num = int(input("Bir sayi giriniz: "))
    print(f"{num} sayisi Hilbert sayidir." if (num -1) % 4 == 0 else f"{num} sayisi Hilbert sayi degildir.")

"""Solution17 Fonc. End"""

def solution_for_question18() -> None:
    n = int(input("Fib. dizi eleman sayisini giriniz: "))

    dizi = [0, 1]
    for i in  range(n):
        if len(dizi) == n:
            break
        eleman = dizi[i] + dizi[i+1]
        dizi.append(eleman)
    print("Fibonacci Diziniz: {", end="")
    print(*dizi[:n], sep=", ", end="}\n")


"""Solution18 Fonc. End"""

def solution_for_question19() -> None:
    fac = lambda a: 1 if 0<= a <= 1 else a * fac(a - 1)
    comb = lambda n, r:  fac(n) / (fac(n-r) * fac(r))

    n = int(input("Pascal ucgeni yukesekligini giriniz: "))
    # benim algoritmam
    def firstWay(n) -> None:
        ucgen = []
        for n in range(n):
            basamaklar = []
            for r in range(n + 1):
                eleman = str(int(comb(n, r))).center(3)
                basamaklar.append(eleman)

            basamaklar = "".join(basamaklar)
            ucgen.append(basamaklar)

        for i in range(n):
            print(' ' * (n - i - 1) + ucgen[i])

    # https://www.algoritmaornekleri.com/python/python-pascal-ucgeni-ornegi/
    def secondWay(yukseklik, satirlar=[]):
        satirlar.append([1])
        satir = [1]
        for i in range(yukseklik):
            sonraki = 0
            siradaki_satir = []
            for k in satir:
                siradaki_satir.append(sonraki + k)
                sonraki = k
            siradaki_satir.append(1)

            satir = siradaki_satir
            satirlar.append(satir)

        for x in satirlar:
            print(x)


    print("Benim fonksiyonum;")
    firstWay(n)

    print("internetten ornek;")
    secondWay(n)
"""Solution19 Fonc. End"""

def solution_for_question20() -> None:
    onlukSayi = int(input("Onluk tabanli bir sayi giriniz: "))

    # 1. yol
    def firstWay(n: int) -> str:
        result = ""
        kalan = n % 2
        bolum = n // 2
        while bolum != 1:
            result += str(kalan)
            kalan = bolum % 2
            bolum = bolum // 2
        result += str(kalan)
        result += str(bolum)

        return result[::-1]

    # internetten ornek
    def secondWay(n):
        output = ""
        while n > 0:
            output = "{}{}".format(n % 2, output)
            n = n // 2
        return output

    # python gomulu fonk. kullanarak
    def thirdWay(n):
        print("Gomulu fonksiyon(bin) kullanarak;")
        print(bin(n)[2:])

        print("string formatlama kullanarak;")
        print("{0:b}".format(n))


    print("Benim fonksiyonum;")
    print(firstWay(onlukSayi))

    print("internetten ornek;")
    print(secondWay(onlukSayi))
    # gomulu fonk. kullanarak
    thirdWay(onlukSayi)

"""Solution20 Fonc. End"""

if __name__ == '__main__':
    solutionFonks = (
        solution_for_question1,  solution_for_question2,  solution_for_question3,  solution_for_question4,
        solution_for_question5,  solution_for_question6,  solution_for_question7,  solution_for_question8,
        solution_for_question9,  solution_for_question10, solution_for_question11, solution_for_question12,
        solution_for_question13, solution_for_question14, solution_for_question15, solution_for_question16,
        solution_for_question17, solution_for_question18, solution_for_question19, solution_for_question20
    )

    questionNumber = int(input("Please enter a question number: "))
    fonk = solutionFonks[questionNumber - 1]
    fonk()
