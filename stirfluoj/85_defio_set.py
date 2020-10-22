# Pitono ne havas const, sed oni indikas volon havi const
# per majusklaj vortoj
MALPERMESATAJ_VORTOJ = {"piedpilkon", "religion", "politikon"}
tekstoj = ["Johano ŝatas politikon kaj piedpilkon", "Vojaĝi estas amuze"]

for teksto in tekstoj:
    interkovro = MALPERMESATAJ_VORTOJ.intersection(set(teksto.lower().split()))
    if interkovro:
        print(f"teksto havas malpermesatajn vortojn: {interkovro}")
    else:
        print(f"Permesata teksto: {teksto}")
