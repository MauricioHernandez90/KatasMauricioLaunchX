# Almacenar las entradas del usuario
#Pista: variable = input("¿Cuál es tu nombre?")
print("\nEl siguiente programa calcula la distancia entre dos planetas tomando como referencia la distancia del sol")

planet_one = float(input("\n\nPor favor ingresa la distancia del primer planeta:\t"))
planet_two = float(input("Por favor ingresa la distancia del segundo planeta:\t"))

print(f"\n\nLa distancia del primer planeta es\t {planet_one} km")
print(f"La distancia del segundo planeta es\t {planet_two} km")

distance = planet_one - planet_two

print(f"\nLa distancia entre el planeta 1 y el planeta 2 es: {abs(distance)}")

