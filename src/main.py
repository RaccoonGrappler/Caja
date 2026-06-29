#!/usr/bin/env python3

def main():
    print("Bienvenido cazador! Es bueno verte por aca!")
    print("Que cazaremos el dia de hoy?")

    monsters = ["Rathalos", "Kirin", "Mizutsune", "Rajang", "Zoh Shia", "Nu Udra", "Chameleos", "Valstrax", "Khezu", "Arkveld", "Lala Barina"]

    print(f"The options are: {', '.join(monsters)}")

    monsterToHunt = input("Cual monstruo cazaremos?: ")
    while monsterToHunt not in monsters:
        monsterToHunt = input("Cual monstruo cazaremos?: ")

        if monsterToHunt not in monsters:
            print("Lo lamentamos cazador! Ese monstruo no esta disponible en este momento. Porfavor elige uno de la lista.")

    print(f"Vas a cazar un {monsterToHunt} miauster? You need to eat good firrrrst!")

    platillosDisponibles = {
        "Ataque": "Carne de Wyvern", 
        "Resistencia": "Patas de pescado", 
        "Defensa": "Hongo gigante de wyveria", 
        "Balanceado": "Puggie a la braza muajaja!",
        "Collab": "Fideos sabrosos de algun restaurante de Japon",
        "Ataque+": "Carne de Rathalos"
    }

    print("Hola miauestro! Mira lo que tenemos en el menu miau!: ")
    for platillo in platillosDisponibles.keys():
        print(f"{platillo}: {platillosDisponibles[platillo]}")

    opcionPlatillo = input("Que estadistica quieres mejorar?: ")
    while opcionPlatillo not in platillosDisponibles:
        opcionPlatillo = input("Que estadistica quieres mejorar?: ")

    print("Cocina dandolo todo fuertemente!....")
    print("Cazador lleno y palico relleno, estamos listos para la caza!!!")
    print("*Sonido de iniciacion de la caza*!!!! Paraaaaaaa!!!")

if __name__ == "__main__":
    main()
