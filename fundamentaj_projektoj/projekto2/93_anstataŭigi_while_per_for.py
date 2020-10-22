# 0, 1, 2, 3, 5, 8, 13, 21…


def fibonacci(kvanto):
    rezulto = [0, 1]
    for _ in range(2, kvanto):
        rezulto.append(sum(rezulto[-2:]))
    return rezulto


if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib)
