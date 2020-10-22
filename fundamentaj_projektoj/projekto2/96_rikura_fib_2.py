def fibonnaci(kvanto, sekvenco=(0, 1)):
    # haltkondiĉo
    return sekvenco if len(sekvenco) == kvanto else \
        fibonnaci(kvanto, sekvenco + (sum(sekvenco[-2:]),))


if __name__ == "__main__":
    # Listigi la unuajn 20 numerojn de la sekvenco
    for fib in fibonnaci(20):
        print(fib)
