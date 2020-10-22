def get_tagspeco(tago):
    tagoj = {
        1: "Semajnfino",
        2: "Semajntago",
        3: "Semajntago",
        4: "Semajntago",
        5: "Semajntago",
        6: "Semajntago",
        7: "Semajnfino",
    }
    return tagoj.get(tago, "** nevalide **")


if __name__ == "__main__":
    for tago in range(8):
        print(f"{tago} : {get_tagspeco(tago)}")
