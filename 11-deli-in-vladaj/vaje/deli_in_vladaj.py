###############################################################################
# Želimo definirati pivotiranje na mestu za tabelo [a]. Ker bi želeli
# pivotirati zgolj dele tabele, se omejimo na del tabele, ki se nahaja med
# indeksoma [start] in [end].
#
# Primer: za [start = 0] in [end = 8] tabelo
#
# [10, 4, 5, 15, 11, 2, 17, 0, 18]
#
# preuredimo v
#
# [0, 2, 5, 4, 10, 11, 17, 15, 18]
#
# (Možnih je več različnih rešitev, pomembno je, da je element 10 pivot.)
#
# Sestavi funkcijo [pivot(a, start, end)], ki preuredi tabelo [a] tako, da bo
# element [ a[start] ] postal pivot za del tabele med indeksoma [start] in
# [end]. Funkcija naj vrne indeks, na katerem je po preurejanju pristal pivot.
# Funkcija naj deluje v času O(n), kjer je n dolžina tabele [a].
#
# Primer:
#
#     >>> a = [10, 4, 5, 15, 11, 2, 17, 0, 18]
#     >>> pivot(a, 1, 7)
#     3
#     >>> a
#     [10, 2, 0, 4, 11, 15, 17, 5, 18]
###############################################################################


## ni se dokončana moja funkcija za pivot sasmo narobe ker mam dve for zanki ni O(n) časovna zahtevnost

# def pivot (a, start, end):
#     pivotni = a[start]
#     index = a.index(a[start])
#     for i in range(start + 1, end):
#         if a[i]< pivotni:
#             elment = a[i]
#             for j in range (start+1,i-1)


#             index += 1

#         else a[i] > pivotni
#     return index


def pivot (a, start, end):
    # robni pogoj
    if start == end:
        return start
    p = a[start]
    prvi_vecji = start + 1
    #invarianta ki jo vzdržujem: med [prvi_vecji] in [i] so samo elemnti manjši od p
    for i in range(start + 1, end + 1):
        if a[i] < p:
            a[prvi_vecji],a[i] = a[i], a[prvi_vecji]
            prvi_vecji += 1
    # vstavimo pivot na pravo mesto
    a[start], a[prvi_vecji -1] = a[prvi_vecji-1], a[start]
    return prvi_vecji -1




###############################################################################
# V tabeli želimo poiskati vrednost k-tega elementa po velikosti.
#
# Primer: Če je
#
#     >>> a = [10, 4, 5, 15, 11, 3, 17, 2, 18]
#
# potem je tretji element po velikosti enak 5, ker so od njega manši elementi
#  2, 3 in 4. Pri tem štejemo indekse od 0 naprej, torej je "ničti" element 2.
#
# Sestavite funkcijo [kth_element(a, k)], ki v tabeli [a] poišče [k]-ti
# element po velikosti. Funkcija sme spremeniti tabelo [a]. Cilj naloge je, da
# jo rešite brez da v celoti uredite tabelo [a].
###############################################################################



###############################################################################
# Tabelo a želimo urediti z algoritmom hitrega urejanja (quicksort).
#
# Napišite funkcijo [quicksort(a)], ki uredi tabelo [a] s pomočjo pivotiranja.
# Poskrbi, da algoritem deluje 'na mestu', torej ne uporablja novih tabel.
#
# Namig: Definirajte pomožno funkcijo [quicksort_part(a, start, end)], ki
#        uredi zgolj del tabele [a].
#
#     >>> a = [10, 4, 5, 15, 11, 3, 17, 2, 18]
#     >>> quicksort(a)
#     [2, 3, 4, 5, 10, 11, 15, 17, 18]
###############################################################################



def quicksort(a):
    def quicksort_part(start,end):
        if end - start <= 0:
            return
        pivot_i = pivot(a,start, end)
        quicksort_part(start, pivot_i -1)
        quicksort_part(pivot_i + 1, end)
    quicksort_part(0, len(a) - 1)
    return

import random
def test_quicksort(n, max_l, max_k):
    for _ in range (n):
        l = random.randint(0, max_l)
        a = [random.randint( - max_k, max_k) for _ in range(l)]
        a1 = a[:]
        a2 = a[:]
        quicksort(a1)
        a2.sort()
        if a1 != a2:
            return a




###############################################################################
# Če imamo dve urejeni tabeli, potem urejeno združeno tabelo dobimo tako, da
# urejeni tabeli zlijemo. Pri zlivanju vsakič vzamemo manjšega od začetnih
# elementov obeh tabel. Zaradi učinkovitosti ne ustvarjamo nove tabele, ampak
# rezultat zapisujemo v že pripravljeno tabelo (ustrezne dolžine).
# 
# Funkcija naj deluje v času O(n), kjer je n dolžina tarčne tabele.
# 
# Sestavite funkcijo [zlij(target, start, end, list_1, list_2)], ki v del 
# tabele [target] med start in end zlije tabeli [list_1] in [list_2]. V primeru, 
# da sta elementa v obeh tabelah enaka, naj bo prvi element iz prve tabele.
# 
# Primer:
#  
#     >>> list_1 = [1,3,5,7,10]
#     >>> list_2 = [1,2,3,4,5,6,7]
#     >>> target = [-1 for _ in range(len(list_1) + len(list_2))]
#     >>> zlij(target, 0, len(target), list_1, list_2)
#     >>> target
#     [1,1,2,3,3,4,5,5,6,7,7,10]
#
###############################################################################
def zlij (target, begin, end, list1, list2):
    # target tabela ustrezne dolžine
    for i in range (0, len(list1) + len(list2)):
        if list1 == []:
            target[i] = list2[0]
            list2 = list2[1:end]
        elif list2 == []:
            target[i] = list1[0]
            list1 = list1[1:end]
        else:
            if list1[0]<=list2[0]:
                target[i] = list1[0]
                list1 = list1[1:end]
            else:
                target[i] = list2[0]
                list2 = list2[1:end]
    return


def merge(target, begin, end, list1, list2):
    i1, i2 = 0, 0
    for j in range(begin, end+1):
        i1_is_ok = i1 <len(list1)
        i2_is_ok = i2 < len(list2)
        if (not i2_is_ok  and i1_is_ok) or (i1_is_ok and list1[i1] < list2[i2]):
            #primer, ko lahko damo samo iz prvega seznama, ali pa lahko iz prvega seznama in je element v prvem seznamu manjši. je pravilno nastavljeno. 
            target[j] = list1[i1]
            i1 += 1
        elif i2_is_ok:
            target[j] = list2[i2]
            i2 +=1
        else:
            raise Exception("Dolžini seznamov nista zadovoljivi.")

###############################################################################
# Tabelo želimo urediti z zlivanjem (merge sort). 
# Tabelo razdelimo na polovici, ju rekurzivno uredimo in nato zlijemo z uporabo
# funkcije [zlij].
#
# Namig: prazna tabela in tabela z enim samim elementom sta vedno urejeni.
#
# Napišite funkcijo [mergesort(a)], ki uredi tabelo [a] s pomočjo zlivanja.
# Za razliko od hitrega urejanja tu tabele lahko kopirate, zlivanje pa je 
# potrebno narediti na mestu.
#
# >>> a = [10, 4, 5, 15, 11, 3, 17, 2, 18]
# >>> mergesort(a)
# [2, 3, 4, 5, 10, 11, 15, 17, 18]
###############################################################################


# ne dela ker ko locimo seznama nista urejena jaz sem ka porabil zlji ki pa dla le na ze urejenih seznamih
# def mergesort_moj(a):
#     n = len(a)
#     if n % 2 == 0:
#         sez1 = a[0: int(n/2 - 1)]
#         sez2 = a[int(n/2) :-1]
#     else:
#         sez1 = a[0:(n-1)//2]
#         sez2 = a[n-1: -1]
#     target = [-1 for _ in range(len(sez1) + len(sez2))]
#     zlij (target, 0, len(target), sez1, sez2)
#     return target

def mergesort_asistenotov(a):
    # a = a
    # b = a[:]
    # def mergesort_in_place(start, end, primary_list, secondary_list):
    if len(a) <= 1:
        return
    polovicka = len(a)//2
    a1, a2 = a[:polovicka], a[polovicka:]
    mergesort_asistenotov(a1)
    mergesort_asistenotov(a2)
    merge(a, 0, len(a)-1, a1, a2)

def test_mergesort(n, max_l, max_k):
    for _ in range(n):
        l = random.randint(0, max_l)
        a = [random.randint(-max_k,max_k) for _ in range(l)]
        a1, a2 = a[:], a[:]
        mergesort_asistenotov(a1)
        a2.sort()
        if a1 != a2:
            return a

