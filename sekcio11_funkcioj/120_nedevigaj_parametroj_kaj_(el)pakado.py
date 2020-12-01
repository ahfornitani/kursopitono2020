# HTML-generilo v4
def etikedo_bloko(enhavo, *args, klaso="sukceso", enteksta=False):
    etikedo = "span" if enteksta else "div"
    html = enhavo if not callable(enhavo) else enhavo(*args)
    return f'<{etikedo} class="{klaso}">{html}</{etikedo}>'


def etikedo_listo(*eroj):
    listo = "".join((f"<li>{ero}</li>" for ero in eroj))
    return f"<ul>{listo}</ul>"


if __name__ == "__main__":
    print(etikedo_bloko("bloko"))
    print(etikedo_bloko("enteksta kaj klaso", klaso="info", enteksta=True))
    print(etikedo_bloko("enteksta", enteksta=True))
    print(etikedo_bloko("malsukcesis", klaso="eraro"))
    print(etikedo_bloko(etikedo_listo("Ero 1", "Ero 2"), klaso="info"))
    print(
        etikedo_bloko(etikedo_listo, "Sabato", "Dimanĉo", klaso="info", enteksta=True)
    )
