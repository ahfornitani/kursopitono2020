def registri(funkcio):
    def ornamilo(*args, **kwargs):
        # funkcio kiel objekto
        print(f"Ekas alvoko de funkcio: {funkcio.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        rezulto = funkcio(*args, **kwargs)
        print(f"Rezulto de alvoko: {rezulto}")
        return rezulto

    return ornamilo


@registri
def sumi(x, y):
    return x + y


@registri
def subtrahi(x, y):
    return x - y


if __name__ == "__main__":
    print(sumi(5, 7))
    print(subtrahi(5, y=7))
