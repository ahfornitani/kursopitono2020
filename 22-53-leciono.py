# Leciono 22 - Unua programaro
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
print('Fino') # komento ankaŭ ĉi tie validas

# Leciono 26: Aritmetikaj operaciiloj
# Aritmetikaj operaciiloj estas duumaj (ĉiam du "operaciatoj")
# intermeta operaciskribo (infix)
print(2 + 3)
print(4 - 7)
print(2 * 5.3)
print(9.4 / 3) # 3.1333333333333333
print(9.4 // 3) # 3.0
print(2**8) # 256
print(10 % 3) # 1
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
print(3 > 4) # False
print(4 >= 3) # True
print(1 < 2) # True
print(3 <= 1) # False
print(3 != 2) # True
print( 3 == 3) # True
print(2 == '2') # False

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
print(True or False) # False
print(7 != 3 and 2 > 3) # False

###  ver(ec)o-tabelo

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

## laŭbite
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
print(celo) # True

