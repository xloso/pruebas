
def fight(f1, f2):
    print("los nombres de los luchadores son {} y {}".format(f1, f2))
    if f1 == 'pepe':
        return f1
    else:
        return f2

#funcion con parametros variables
def luchadores(*fighters):
    for fighter in fighters:
        print("este luchador se llama {}".format(fighter))
        if fighter == 'Bruce Lee':
            return fighter
    return None

def karate(f1, f2):
    if f1 > f2:
        return f1
    else:
        return f2

#funciones como parámetros - programación funcional
def clubLucha(fighters, engine):
    for fighters[0] in fighters:
        for fighters[1] in fighters:

            winner = engine(fighters[0], fighters[1])
    print("\n el ganador de la funcional es {}".format(winner))
    return winner

name = input("introduce nombre: ")
if name == 'luke':
    print("soy un Jedi")
elif name == "chewbacca:":
    print('aaaahahahahah')
else:
    print('no soy luke')

darthVader = True
count = 0
while darthVader:
    print("soy tu padre")
    count += 1
    if count == 4:
        darthVader = False

fruits = ["apple", "peach", "watermelon"]
for i in fruits:
    print("Me gusta comer:", i)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
from_2_to_6 = numbers[2:7]
print(from_2_to_6)
greater_than_4 = numbers[5:]
print(greater_than_4)
print("los pares son ", numbers[::2])
print("los impares son ", numbers[1::2])

#diccionarios
fighterD = {"name": "chuck", "last_name": "norris", "tecnique":"Karate"}
#para acceder usar siempre "get" ya que si da error con "get" no PETA
print(fighterD["name"]) #esta no usar<
print(fighterD.get("name"))


ganador = fight("paco", "pepe")
print(" el luchador que ha ganado es: {}\n".format(fight("paco", "pepe")))
#otra formas
print(" el luchador que ha ganado es: {}\n".format(ganador))
print(" ahora ejecutamos funcion luchadores\n")

print("\n el luchador que ha ganado se llama: {}".format(luchadores('alfonso', 'chuck', 'otro luchador', 'Bruce Lee')))
print('\n el ganador de la funcion funcional es: {}'.format(clubLucha(['Bruce', 'Chuck'], 'karate')))
print ("\n fin programa")