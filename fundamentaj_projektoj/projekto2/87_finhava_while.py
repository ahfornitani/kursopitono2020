# 0, 1, 2, 3, 5, 8, 13, 21…


def fibonacci(limo):
    antaŭlasta = 0
    lasta = 1
    print(f"{antaŭlasta}, {lasta}", end=",")
    while lasta < limo:
        sekva = antaŭlasta + lasta
        print(sekva, end=",")
        antaŭlasta = lasta
        lasta = sekva


if __name__ == "__main__":
    fibonacci(100000)
