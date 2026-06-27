#!/usr/bin/env python3

def main():
    print("Bienvenido cazador! Es bueno verte por aca!")
    print("Que cazaremos el dia de hoy?")

    monsters = ["Zinogre", "Rathalos", "Brachydios", "Kirin", "Mizutsune", "Rajang", "Deviljho"]

    print(f"The options are: {', '.join(monsters)}")

    monsterToHunt = None
    while monsterToHunt not in monsters:
        monsterToHunt = input("Enter your choice: ")

        if monsterToHunt not in monsters:
            print("Lo lamentamos cazador! Ese monstruo no esta disponible en este momento. Porfavor elige uno de la lista.")

    print(f"Vas a cazar un {monsterToHunt} miauster? You need to eat good firrrrst!")
    print("Cocina dandolo todo fuertemente!....")
    print("Cazador lleno y palico relleno, estamos listos para la caza!!!")
    print("*Sonido de iniciacion de la caza*!!!! Paraaaaaaa!!!")

if __name__ == "__main__":
    main()
