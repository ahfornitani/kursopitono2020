def etikedo(etikedo, *args, **kwargs):
    if "html_class" in kwargs:
        kwargs["class"] = kwargs.pop("html_class")
    atributoj = " ".join(f'{ŝ}="{v}"' for ŝ, v in kwargs.items())
    ena = "".join(args)
    return f"<{etikedo} {atributoj}>{ena}</{etikedo}>"


if __name__ == "__main__":
    print(
        etikedo(
            "p",
            etikedo("span", "Kurso pri Pitono 3 far "),
            etikedo("strong", "Juracy Filho", id="jf"),
            etikedo("span", " kaj "),
            etikedo("strong", "Leonardo Leitão", id="ll"),
            etikedo("span", "."),
            html_class="alert",
        )
    )
