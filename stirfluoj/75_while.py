# while True:
#       print('Vai demorar muito')

from random import randint

informita_numero = 0
sekreta_numero = randint(0, 9)

while informita_numero != sekreta_numero:
    informita_numero = int(input("Enigu numeron: "))

print(f"Sekreta numero {sekreta_numero} estis trovita!")
