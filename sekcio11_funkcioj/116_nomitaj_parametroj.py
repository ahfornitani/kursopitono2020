# HTML-generilo v2
def etikedo_bloko(teksto, klaso="sukceso", enteksta=False):
    etikedo = "span" if enteksta else "div"
    return f'<div class="{klaso}">{teksto}</div>'


if __name__ == "__main__":
    print(etikedo_bloko("bloko"))
    print(etikedo_bloko("enteksta kaj klaso", "info", True))
    print(etikedo_bloko("enteksta", enteksta=True))
    print(etikedo_bloko("malsukcesis", klaso="eraro"))
