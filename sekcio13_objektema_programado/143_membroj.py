# miks-uskleco (camelCase)
# sed Pitono uzas majuskligitan CamelCase, kaj nomas ĝin "CapWords"

# ĉiu klas-metodo de Pitono *nepre* devas havi
# la argumenton "self" (tamen povas esti iu ajna vorto, sed self estas la interkonsentita vorto"
# metodo __str__ konvertas ajnan tipon al string
class Dato:
    def __str__(self):
        return f"{self.jaro}-{self.monato}-{self.tago}"


d1 = Dato()  # instance, genero

# ĉar Pitono estas dinamika, eblas aldoni atributojn al objekto
# eĉ se la klaso ne informas ilin!
d1.jaro = 2020
d1.monato = 12
d1.tago = 17
# print(f"{d1.jaro}-{d1.monato}-{d1.tago}")
print(d1)

d2 = Dato()
d2.jaro = 2019
d2.monato = 11
d2.tago = 16
print(d2)

d3 = Dato()
d3.jaro = 2021
d3.monato = 10
d3.tago = 15
print(d3)
