# miks-uskleco (camelCase)
# sed Pitono uzas majuskligitan CamelCase, kaj nomas ĝin "CapWords"

# ĉiu klas-metodo de Pitono *nepre* devas havi
# la argumenton "self" (tamen povas esti iu ajna vorto, sed self estas la interkonsentita vorto"
# metodo __str__ konvertas ajnan tipon al string
# konstruilo en Pitono, anstataŭ samnoma kiel klaso (ekz. C#), uzas la vorton "__init__"
# Pitono ankaŭ permesas UNUNURAN konstruilon. Ne pli ol unu!
class Dato:
    def __init__(self, jaro=1970, monato=1, tago=1):
        self.jaro = jaro
        self.monato = monato
        self.tago = tago

    def __str__(self):
        return f"{self.jaro}-{self.monato}-{self.tago}"


# instance, genero
d1 = Dato(2020, 12, 17)
print(d1)
d2 = Dato()  # uzos implican argumentojn
print(d2)
d3 = Dato(jaro=1980)
print(d3)
