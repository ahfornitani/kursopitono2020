# Pitono ne havas const, sed oni indikas volon havi const
# per majusklaj vortoj
MALPERMESATAJ_VORTOJ = ("piedpilkon", "religion", "politikon")
tekstoj = ["Johano ŝatas politikon kaj piedpilkon", "Vojaĝi estas amuze"]

for teksto in tekstoj:
    for vorto in teksto.lower().split():
        if vorto in MALPERMESATAJ_VORTOJ:
            print(f"Teksto havas almenaŭ unu malpermesata vorto: {vorto}")
            break
    else:
        print(f"Permesata teksto: {teksto}")
