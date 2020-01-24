# Leciono 22 - Unua programaro
from decimal import Decimal, getcontext
print('unua programaro')

# Leciono 23 - Bazaj tipoj
print('Vi estas ' + 10 * 'tre ' + 'bela!')
print([1, 2, 3])
print({'nomo': 'Augusto', 'aĝo': '29'})

# Leciono 24 - Variabloj
# Pitono estas dinamik-tipa lingvaĵo
# ne necesas "int", "double" ktp por deklari variablon
a = 10
b = 5.2
print(a + b)
a = 'Nun mi estas ĉeno!'
print(a)
# samtempe, ĝi estas forte tipigita:
# ekz-e print(a + b) nun kaŭzos eraro, ĉar la interpretilo ne provos "diveni" kion fari

# Leciono 25: Komentoj
# Miaj variabloj
salajro = 3450.45
elspezoj = 2456.2

# Mult-linia komento sube per 3 duoblaj aŭ simplaj citiloj
"""
La ideo estas kalkuli
kiom da mono restos
post monat-fino
"""
print('Fino')  # komento ankaŭ ĉi tie validas

# Leciono 26: Aritmetikaj operaciiloj
# Aritmetikaj operaciiloj estas duumaj (ĉiam du "operaciatoj")
# intermeta operaciskribo (infix)
print(2 + 3)
print(4 - 7)
print(2 * 5.3)
print(9.4 / 3)  # 3.1333333333333333
print(9.4 // 3)  # 3.0
print(2**8)  # 256
print(10 % 3)  # 1
a = 12
b = a
print(a + b)

# unuuma operaciilo
# intermeta / infix
# ++a
# postmeta / postfix
# b++ (ne ekzistas "++a" nek "a++" en Pitono)

# Leciono 27/28 : Defio pri aritmetikaj operaciiloj
# kiom da procentoj la elspezoj estas de la salajro
salajro = 3450.45
elspezoj = 2456.2
kpd = (elspezoj / salajro) * 100
print(f'{round(kpd, 2)} %')

# Leciono 29: Rilataj operaciiloj
print(3 > 4)  # False
print(4 >= 3)  # True
print(1 < 2)  # True
print(3 <= 1)  # False
print(3 != 2)  # True
print(3 == 3)  # True
print(2 == '2')  # False

# Leciono 30: Atribuiloj
var_a = 3
var_a = var_a + 7
print(var_a)

var_a += 5
print(var_a)

var_a -= 3
print(var_a)

var_a *= 2
print(var_a)

var_a /= 4
print(var_a)

var_a %= 10
print(var_a)

var_a **= 8
print(var_a)

var_a //= 256
print(var_a)

# Leciono 31: Logikaj operaciiloj
print(True or False)  # False
print(7 != 3 and 2 > 3)  # False

# ver(ec)o-tabelo

# and (kaj)
# T and T > True ; T and F > False
# F and T > False ; F and F > False

# or (aŭ)
# T or T > True ; T or F > True
# F or T > True ; F or F > False

# XOR (MAŬ)
# T != T (False)
# T != F (True)
# F != T (True)
# F != F (False)

# Negacia operaciilo (unuuma)
# not True > False
# not False > True

# not 0 > True
# not 1, not 2, not -1 (ajna numero malsama al 0 estas True) > False
# not not True > True ; not not False > False

# laŭbita opraciiloj > Atentu!
# True & True > True
# True & False > False
# False | True > True
# True ^ False > True (^ estas xor)

# laŭbite
# 3 -> 11
# 2 -> 10
# _ => 10 (1 kaj 1 = 1; 1 kaj 0 = 0)
# 3 & 2 => 2 (10 duume --> 2)
# 3 | 2 => 3 (1 aŭ 1 = 1; 1 aŭ 0 = 1)
# 3 ^ 2 => 1 (1 ^ 1 = 0; 1 ^ 0 = 1)

saldo = 1000
salajro = 4000
elspezoj = 2967

favora_saldo = saldo > 0
kontrolitaj_spezoj = salajro - elspezoj >= 0.2 * salajro

celo = favora_saldo and kontrolitaj_spezoj
print(celo)  # True

# Leciono 32 kaj 33: Defio pri logikaj operaciiloj
print('\nLeciono 33: \n')
mardo = True
ĵaŭdo = False
tv32 = False
tv50 = False

if mardo == False and ĵaŭdo == False:
    print('Resti hejme, sen eĉ glaciaĵon')
elif (mardo == False and ĵaŭdo == True) or (mardo == True and ĵaŭdo == False):
    print('Iri al butikumejo, aĉeti TV-n 32 kaj manĝi glaciaĵon')
else:
    print('Iri al butikumejo, aĉeti TV-n 32 kaj manĝi glaciaĵon')

# aŭ
laboro_mardo = True
laboro_ĵaŭdo = False
tv_50 = laboro_mardo and laboro_ĵaŭdo
glaciaĵo = laboro_mardo or laboro_ĵaŭdo
tv_32 = laboro_mardo != laboro_ĵaŭdo
pli_da_sano = not glaciaĵo

print(
    f'Tv50 = {tv_50} ; Tv32 = {tv_32}; Glaciaĵo = {glaciaĵo}; Sana = {pli_da_sano}')

# Leciono 34: Unuumaj operaciiloj
print('\nLeciono 34: ')
a = 3
# a++
a += 1
# a--
# ++a
-a  # negativigas a-n
+a  # pozitivigas a-n
a = -a

not 0
not 1  # ajna numero, escepte 0, estas True
not False
not not True

# Leciono 35: Triumaj operaciiloj
print('\nLeciono 35: \n')
pluvas = True
pripluvo = 'Hodiaŭ miaj vestaĵoj estas ' + ('sekaj.', 'malsekaj.')[pluvas]
print(pripluvo)
pripluvoif = 'Hodiaŭ miaj vestaĵoj estas ' + \
    ('malsekaj.' if pluvas else 'sekaj.')
print(pripluvoif)

# Leciono 36: Kromaj operaciiloj
# membra operaciilo
print('\nLeciono 36: \n')
listo = [1, 2, 3, 'Anna', 'Karlo']
print(2 in listo)  # True
print('Anna' not in listo)  # False

# identeca operaciilo
x = 3
y = x
z = 3
print(x is y)  # True
print(y is z)  # True
print(x is not z)  # False

listo_a = [1, 2, 3]
listo_b = listo_a
listo_c = [1, 2, 3]

# A kaj B direktiĝas al sama memor-adreso.
# Eĉ se C havas egalan enhavon al A (kaj B), ĝia
# memoradreso estas tute alia
print(listo_a is listo_b)  # True
print(listo_b is listo_c)  # False
print(listo_a is not listo_c)  # True

# Leciono 37: Integritaj moduloj kaj ĉiea amplekso (global scope)
print('\nLeciono 37: \n')
print(type(1))  # <class 'int'>
print(__builtins__.type('Hej, uloj!'))  # <class 'str'>
__builtins__.print(10 / 3)  # 3.3333333333333335
# print(help(dir)) # longa teksto
nomo = "Johano Zamenhof"
print(type(nomo))  # <class 'str'>
print(__builtins__.len(nomo))

# Leciono 38: Konverto de tipoj
print('\nLeciono 38: \n')
print(2 + 3)  # 5
print('2' + '3')  # 23
# print(2 + '3') # eraro
a = 2
b = '3'
print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(a + int(b))  # 5
print(str(a) + b)  # 23
print(type(str(a)))  # <class 'str'>, kompreneble
# print(a + intr('3.4')) # eraro
print(a + float(3.4))  # 5.4

# Leciono 39: Aŭtomata altipigo (coercion)
# okazas kiam ne ekzistas ambigueco, do implica altipogo ne necesas
print('\nLeciono 39: \n')
print(10 / 2)  # rezulto de divido ĉiam estas float
print(type(10/2))  # <class 'float'>
print(10 // 3)
print(type(10 // 3))  # <class 'int'>
# ĉar float konservas pli da datumoj, ĝi bezontas por la suba operacio
print(type(10 // 3.3))  # <class 'float'>
print(type(10 / 2.5))  # float, ĉar necese, eĉ se la rezulto estas 4 (4.0)
print(2 + True)  # True estas "1", do rezulto estas "3"
print(2 + 0)  # same, False estas 0, do rezulto estas "2"

# Leciono 40: Numeroj 1
print('\nLeciono 40: \n')
print(dir(int))
print('\n')
print(dir(float))
a = 5
b = 2.5
print(a / b)  # float
print(a + b)  # float ktp

print('\n')

print(b.is_integer())  # False
print(5.0.is_integer())  # True . Ĝi ne estas <int>, sed entjera valoro
print(5.1.is_integer())  # False . Samkiale as antaŭa linio

print(int.__add__(2, 3))  # 5 (per integrita modulo de <int>)
print(2 + 3)  # same, sed per modulo add de __builtins__

print((-2).__abs__())  # 2 per abs metodo de <int>
print(abs(-2))  # 2 , per builtins

# Leciono 41: Numeroj 2 > Dekumaj numeroj
print('\nLeciono 41: \n')

print(1.1 + 2.2)  # 3.3000000000000003

# 3.300000000000000266453525910037569701671600341796875
print(Decimal(1.1 + 2.2))
print(Decimal(1.1) + Decimal(2.2))  # 3.300000000000000266453525910
print(Decimal(1) / Decimal(7))  # 0.1428571428571428571428571429

# modifi precizecon
getcontext().prec = 10
print(Decimal(1.1) + Decimal(2.2))  # 3.300000000

getcontext().prec = 4
print(Decimal(1) / Decimal(7))  # 0.1429

# Leciono 42: Ĉenoj 1
print('\nLeciono 42: \n')

# ĉenoj estas neŝanĝeblaj
nomo = 'Kolomano Kaloĉajo'
print(nomo[0])  # 'K'
# nomo[0] = 'S' # eraro pro neŝanĝebleco: TypeError: 'str' object does not support item assignment
# kio JA eblas modifi: la enhavon de la variablo, per re-atribuigo
nomo = 'Kálmán Kalocsay'
print(nomo)  # Kálmán Kalocsay (jen nova ĉeno kreita memore, kaj kio anstataŭigas la antaŭan, SEN modifi ĝin)

# Leciono 43: Ĉenoj 2
print('\nLeciono 43: \n')

nomo = 'Katalin Kovats'
print(nomo[0])  # K
print(nomo[6])  # n
print(nomo[-2])  # t
# ekde pozicio 7, kiu estas la spaco -> "Kovats", inkluvizas la pozicion elektatan
print(nomo[8:])
# same, sed kalkulante ekde la fino renversen -> "Kovats", inkluzivas la pozicion elektatan
print(nomo[-6:])
print(nomo[:4])  # "Kata", ne inkluzivas la pozicion elektatan ([4] estas "l")
print(nomo[2:5])  # montros de 2 ĝis 4, do "tal"

numeroj = '1234567890'
print(numeroj[::])  # montros ĉiujn. Sennecese...
print(numeroj[::2])  # montros po du "13579"
print(numeroj[1::2])  # po du, ekde 1: "24680"

# facile por renvsersi ĉenon
print(numeroj[::-1])  # 0987654321
print(numeroj[::-2])  # 08462
print(nomo[::-1])  # stavoK nilataK

# Leciono 44: Ĉenoj 3
print('\nLeciono 44: \n')

frazo = 'Pitono estas bonega programlingvo!'
print("pi" in frazo)  # False , ĉar Pitino distingas usklecon pi != Pi
print("estas" in frazo)  # True
print("estas" not in frazo)  # False
print(len(frazo))  # 34
print(frazo.upper())  # PITONO ESTAS BONEGA PROGRAMLINGVO!
print(frazo)  # same as antaŭe, ĉar ĉeno estas neŝanĝebla
# split() montros liston. Implica apartig-valoro (split) estas spaco # ['Pitono', 'estas', 'bonega', 'programlingvo!']
print(frazo.split())
# nun per specifa signo, litero P
print(frazo.split('a'))  # ['Pitono est', 's boneg', ' progr', 'mlingvo!']

# print(help(str.center))

# Leciono 45: Ĉenoj 4 - magiaj metodoj
print('\nLeciono 45: \n')
a = '123'
b = ' von Rübeck 4'

# a.__add__(a, b)
# str.__add__(a, b)
print(a + b)
# a.__len__()
print(len(a))
# a.__contains__('1')
print('1' in a)