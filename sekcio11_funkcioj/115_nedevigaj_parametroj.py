# HTML-generilo v1
def etikedo_bloko(teksto, klaso="sukceso"):
    return f'<div class="{klaso}">{teksto}</div>'


if __name__ == "__main__":
    # Testoj (assertions)
    assert (
        etikedo_bloko("Enigita sukcese!")
        == '<div class="sukceso">Enigita sukcese!</div>'
    )
    assert (
        etikedo_bloko("Ne eblas forigi!", "eraro")
        == '<div class="eraro">Ne eblas forigi!</div>'
    )
    print(etikedo_bloko("bloko"))
