# Ejemplo de uso de listas
misvecinos=["Aripina", "Anastacia", "Maria"]
misnumeros=[888, 777, 444]
# Mostrando mis numeros
print(misvecinos)
# mostrando mis numeros raros
print (misnumeros)
print("------accediendo a los elementos de la lista------")
print(misvecinos[-2])
if "pedro" in misvecinos:
    print("si, 'Anastacia' está en la lista de mis vecinos")
else:
    print("Chale no eres mi vecino")
    print("Numero de vecinos")
    Vvecinos=len(misvecinos)
    print(f"Numero de vecinos= {Vvecinos}")
    print("ciclo for en listas")
    posicion=0
for mediovecino in misvecinos:
    print(posicion, " ",mediovecino)
    posicion=posicion+1