import random

def mostrar_menu(personajes):
    # Menú
    print("\n📜 Selección de Personajes:")
    for clave, datos in personajes.items():
        print(f"opción {clave}. {datos['nombre']}, ataque: {datos['atk']}, hp: {datos['hp']}")
    return safe_input("Elige un personaje por número: ")

def safe_input(ingreso):
    try:
        opción = int(input(ingreso))
        
        # Control del valor de la opción entre 1 y 4
        if opción < 1 or opción > 4:
            print("⚠️ Entrada inválida. Intenta con otro número.")
            return safe_input(ingreso)
        
        return opción
    except ValueError:
        print("⚠️ Entrada inválida. Intenta con un número.")
        return safe_input(ingreso)

def calcular_daño(atacante, defensor):
    daño = random.randint(1, atacante['atk'])
    defensor['hp'] -= daño
    return daño

# diccionario de personajes
personajes = {
    1: {
        "nombre": "Guerrero",
        "hp": 100,
        "atk": 20
    },
    2: {"nombre": "Mago", "hp": 80, "atk": 25},
    3: {"nombre": "Arquero", "hp": 90, "atk": 18},
    4: {"nombre": "Pícaro", "hp": 50, "atk": 27}
}
turno = 1
registro_turnos = [] # 📝 Lista que guarda el historial de cada turno

try:
    print("⚔️ Bienvenido al simulador de Batallas RPG ⚔️")

    # ingreso de opciones
    jugador_opcion = mostrar_menu(personajes)
    enemigo_opcion = mostrar_menu(personajes)

    # copiando el "objetos"
    jugador = personajes[jugador_opcion].copy()
    enemigo = personajes[enemigo_opcion].copy()

    # Batalla
    while jugador['hp'] > 0 and enemigo['hp'] > 0:
        print(f"\n🎯 Turno {turno}")
        print(f"{jugador['nombre']} (HP: {jugador['hp']}) vs {enemigo['nombre']} (HP: {enemigo['hp']})")

        # Ataque del jugador
        daño = calcular_daño(jugador, enemigo)
        
        registro_turnos.append(f"Turno {turno}: {jugador['nombre']} causa {daño} a {enemigo['nombre']}")

        if enemigo['hp'] <= 0:
            print(f"\n🏆 ¡{jugador['nombre']} ha ganado la batalla!")
            break

        # Ataque del enemigo
        daño = calcular_daño(enemigo, jugador)

        registro_turnos.append(f"Turno {turno}: {enemigo['nombre']} causa {daño} a {jugador['nombre']}")

        if jugador['hp'] <= 0:
            print(f"\n💀 ¡{enemigo['nombre']} ha ganado la batalla!")
            break

        # avanzar el turno
        turno += 1

    # Historial de la batalla
    for evento in registro_turnos:
        print(evento)

except Exception as e:
    print(f"❌ Error inesperado: {e}")



