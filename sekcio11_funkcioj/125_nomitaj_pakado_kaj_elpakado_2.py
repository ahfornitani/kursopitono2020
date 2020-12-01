# HTML-generilo v5
bloko_atributoj = ("bloko_accesskey", "bloko_id")
ul_atributoj = ("ul_id", "ul_style")


def filtri_atributojn(informitaj, subtenataj):
    return " ".join(
        f'{k.split("_")[-1]}="{v}"' for k, v in informitaj.items() if k in subtenataj
    )


def etikedo_bloko(enhavo, *args, klaso="sukceso", enteksta=False, **novaj_atributoj):
    etikedo = "span" if enteksta else "div"
    html = enhavo if not callable(enhavo) else enhavo(*args, **novaj_atributoj)
    atributoj = filtri_atributojn(novaj_atributoj, bloko_atributoj)
    return f'<{etikedo} {atributoj} class="{klaso}">{html}</{etikedo}>'


def etikedo_listo(*eroj, **novaj_atributoj):
    listo = "".join((f"<li>{ero}</li>" for ero in eroj))
    return f"<ul {filtri_atributojn(novaj_atributoj, ul_atributoj)}>{listo}</ul>"


if __name__ == "__main__":
    print(etikedo_bloko("bloko"))
    print(etikedo_bloko("enteksta kaj klaso", klaso="info", enteksta=True))
    print(etikedo_bloko("enteksta", enteksta=True))
    print(etikedo_bloko("malsukcesis", klaso="eraro"))
    print(etikedo_bloko(etikedo_listo("Ero 1", "Ero 2"), klaso="info"))
    print(
        etikedo_bloko(etikedo_listo, "Sabato", "Dimanĉo", klaso="info", enteksta=True)
    )
    print(
        etikedo_bloko(
            etikedo_listo,
            "Ero 1",
            "Ero 2",
            klaso="info",
            bloko_accesskey="m",
            bloko_id="enhavo",
            ul_id="listo",
            ul_style="color:red",
        )
    )
