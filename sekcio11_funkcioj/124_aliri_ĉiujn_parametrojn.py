def ĉiuj_parametroj(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == "__main__":
    ĉiuj_parametroj('a', 'b', 'c')
    ĉiuj_parametroj(1, 2, 3, mojosa=True, valoro=12.99)
    ĉiuj_parametroj('Ana', False, [1, 2, 3], grandeco='M', fragila=False)
    ĉiuj_parametroj(unua='Maria', dua='Johano')
    ĉiuj_parametroj('Maria', unua='Johano')
