from te import Te


print(" 1. Seleccona el sabor de Te (1 = Te negro / 2 = Te Verde / 3 agua de hierbas): ")

sabor = int(input("Elegir sabor del Te : "))

print(" Elige el formato ( 300  o 500 ) : ")

formato = int(input("Elige formato : "))

nombre, tiempo , recomendacion = Te.receta(sabor)
precio = Te.obtener_precio(formato)
duracion = Te.duracion


print(f"""Por tanto, debe mostrar en pantalla los valores de:
a. Sabor del tipo de té (como texto) {nombre}
b. Formato (como número) {formato}
c. Precio (como número) {precio}
d. Tiempo (como número) {tiempo}
e. Recomendación (como texto) {recomendacion}
f. Duracion {duracion}
""")
