# HTML-generilo v3
def etikedo_bloko(teksto, klaso="sukceso", enteksta=False):
    etikedo = "span" if enteksta else "div"
    return f'<div class="{klaso}">{teksto}</div>'


def etikedo_listo(*eroj):
    listo = "".join((f"<li>{ero}</li>" for ero in eroj))
    return f"<ul>{listo}</ul>"


if __name__ == "__main__":
    print(etikedo_bloko("bloko"))
    print(etikedo_bloko("enteksta kaj klaso", "info", True))
    print(etikedo_bloko("enteksta", enteksta=True))
    print(etikedo_bloko("malsukcesis", klaso="eraro"))
    print(etikedo_bloko(etikedo_listo('Ero 1', 'Ero 2'), klaso='info'))
