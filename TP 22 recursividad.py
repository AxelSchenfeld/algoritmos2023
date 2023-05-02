def use_force(backpack, element):
    if not backpack:
        return None
    elif backpack[0] == element:
        return 1
    else:
        objects = use_force(backpack[1:], element)
        if not objects:
            return None
        else:
            return objects + 1


backpack = ["sable laser", "comida", "capa", "brujula", "llaves", "sable de luz"]
element = input('Ingrese el elemento: ')


objects = use_force(backpack, element)

if objects == None:
    print(f"No se encontró {element} en la mochila")
else:
    print(f"Se encontró {element} después de sacar {objects} objetos")