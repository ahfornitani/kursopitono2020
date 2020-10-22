produkto = {"nomo": "Ŝika skribilo", "prezo": 14.99, "importita": True, "registro": 793}

for ŝlosilo in produkto.keys():  # aŭ nur "produto", ĉar 'keys' estas implice
    print(ŝlosilo)

for valoro in produkto.values():
    print(valoro)


for ŝlosilo, valoro in produkto.items():
    print(f"{ŝlosilo}: {valoro}")

# valoroj restas post for! Samkiel uzo de "var" ĉe JavaScript
# valoroj ne restringiĝas por interno de iteracio
print(ŝlosilo, valoro)
