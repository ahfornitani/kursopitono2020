import csv

with open("97_homoj.csv") as enigo:
    for homo in csv.reader(enigo):
        print("Nomo: {}, Aĝo: {}".format(*homo))
