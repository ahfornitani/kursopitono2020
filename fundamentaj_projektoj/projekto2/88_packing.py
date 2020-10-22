# 0, 1, 2, 3, 5, 8, 13, 21…


def fibonacci(limo):
    antaŭlasta = 0
    lasta = 1
    print(f"{antaŭlasta}, {lasta}", end=",")
    while lasta < limo:
        antaŭlasta, lasta = lasta, antaŭlasta + lasta
        print(f"{lasta}", end=",")


if __name__ == "__main__":
    fibonacci(100000)
