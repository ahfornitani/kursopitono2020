# 0, 1, 2, 3, 5, 8, 13, 21…


def fibonacci(kvanto):
    rezulto = [0, 1]
    while True:
        rezulto.append(sum(rezulto[-2:]))
        if len(rezulto) == kvanto:
            break
    return rezulto


if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib)
