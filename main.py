def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numberAssString = givenString.split(",")
    for x in numberAssString:
        l.append(int(x))
    return l
def printMeniu():
    print("1.Citirea lista:")
    print("3.Suma celui mai mic si celui mai mare numar din lista: ")
    print("4.Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr n citit de la tastatura")
    print("5.Afișarea listei obținute din lista inițială în care numerele pătrat perfect sunt înlocuite cu radicalul acestora. În cazul numerelor care nu sunt pătrat perfect, acestea sunt înlocuite cu o listăcu numerele pătrat perfect mai mici decât numărul inițial. Modificările se aplică doar pe numerele pozitive")
    print("x.Iesire")
def concatenarea(l):
    '''
    Concateneaza numerele pozitive din lista
    :param l: o lista de numere intregi
    :return: numarul rezultat din concatenare
    '''
    rezultat = " "
    for x in l:
        if x > 0:
            rezultat.__add__(str(x))
    return rezultat
def sumaMinMax(l):
    '''
    Determina suma dintre cel mai mic si cel mai mare numar din lista
    :param l: o lista de numere intregi
    :return: Suma minimului si maximului din lista
    '''
    min=0
    max=0
    for x in l:
        if x > max:
            max = x
        elif x < min:
            min = x
    return min+max
def test_sumaMinMax():
    assert sumaMinMax([-1,0,2,3]) == 2
    assert sumaMinMax([]) == 0
    assert sumaMinMax([-10,8,9,10]) == 0
def verificareSumaCifMaiMareSauegaln(l,n):
    '''
    Determina si afiseaza toate numerele din lista care au suma cifrelor egala sau mai mare decat un numar n citit de la tastatura
    :param l: o lista de numere intregi
    :param n: numarul citit de la tastatura cu care este comparata suma cifrelor
    :return: o lista de numere intregi care au suma cifrelor egala cu nuamrul citit de la tastatura
    '''
    rezultat = []
    n = int(input("Suma cifrelor dorita: "))
    for x in l:
        cx = x
        if x < 0:
            cx = (-1) * x
        cifs = 0
        while cx != 0:
            cif = cx % 10
            cifs = cifs + cif
            cx = cx // 10
        if cifs >= n:
            rezultat.append(x)
    return rezultat
def test_verificareSumaCifMaiMareSauegaln():
    assert verificareSumaCifMaiMareSauegaln([12,10,11,13],3) == [12,13]
    assert verificareSumaCifMaiMareSauegaln([21,22,25],7) == [25]
def listaPatratePerfecte(l):
    '''
    Afiseaza lista cu patrate perfecte sau daca nu sunt patrate perfecte se afiseaza cel mai mare pp mai mic decat numarul
    :param l: o lista de numere intregi
    :return: lista de patarte perfecte
    '''

    assert listaPatratePerfecte([25,64]) == [25,64]
    assert listaPatratePerfecte([20,25]) == [16,25]

def main():
    test_sumaMinMax()
    l=[]
    while True:
        printMeniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l=citireLista()
        elif optiune == "2":
            print(concatenarea(l))
        elif optiune == "3":
            print(sumaMinMax(l))
        elif optiune == "4":
            print(verificareSumaCifMaiMareSauegaln(l))
        elif optiune == "5":
            break
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, te rog reincearca !")
main()
