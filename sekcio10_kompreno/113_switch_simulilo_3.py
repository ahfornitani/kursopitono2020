def get_tagspeco(tago):
    tagoj = {
        (1, 7): "Semajnfino",
        tuple(range(2, 7)): "Semajntago",
    }

    elektita_tago = (speco for numeroj, speco in tagoj.items() if tago in numeroj)
    return next(elektita_tago, "** nevalida tago **")


if __name__ == "__main__":
    for tago in range(0, 9):
        print(f"{tago}: {get_tagspeco(tago)}")
