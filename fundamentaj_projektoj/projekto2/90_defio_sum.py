# 0, 1, 2, 3, 5, 8, 13, 21…

def fibonacci(limo):
    rezulto = [0, 1]
    while rezulto[-1] < limo:
        rezulto.append(rezulto[-2] + rezulto[-1])
    return rezulto

if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)