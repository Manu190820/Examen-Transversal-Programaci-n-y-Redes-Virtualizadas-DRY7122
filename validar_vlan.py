# validar_vlan.py

def validar_vlan(numero_vlan):
    if 1 <= numero_vlan <= 1000:
        print(f"La VLAN {numero_vlan} pertenece al rango normal.")
    elif 1002 <= numero_vlan <= 4094:
        print(f"La VLAN {numero_vlan} pertenece al rango extendido.")
    else:
        print(f"La VLAN {numero_vlan} no es valida.")

if __name__ == "__main__":
    vlan = int(input("Ingrese el numero de VLAN a validar: "))
    validar_vlan(vlan)
