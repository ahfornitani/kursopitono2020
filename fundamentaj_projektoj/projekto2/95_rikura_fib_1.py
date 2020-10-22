def fibonnaci(kvanto, sekvenco=(0, 1)):
    # haltkondiĉo
    if len(sekvenco) == kvanto:
        return sekvenco
    return fibonnaci(kvanto, sekvenco + (sum(sekvenco[-2:]),))


if __name__ == "__main__":
    # Listigi la unuajn 20 numerojn de la sekvenco
    for fib in fibonnaci(20):
        print(fib)
