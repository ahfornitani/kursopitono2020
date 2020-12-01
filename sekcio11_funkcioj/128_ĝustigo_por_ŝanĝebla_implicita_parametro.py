# Ne uzu mutables kiel default argument
def fibonacci(sekvenco=None):
    sekvenco = sekvenco or [0, 1]
    sekvenco.append(sekvenco[-1] + sekvenco[-2])
    return sekvenco


def fibonacci_sen_problemoj(sekvenco=(0, 1)):
    return sekvenco + (sekvenco[-1] + sekvenco[-2],)


if __name__ == "__main__":
    eko = fibonacci()
    print(eko, id(eko))
    print(fibonacci(eko))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
    print(fibonacci_sen_problemoj())
