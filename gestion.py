# Lista para almacenar productos como diccionarios
productos = []
def cargar_datos():
    
    try:
        with open('data.txt', 'r') as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }
                productos.append(producto)
    except FileNotFoundError:
        pass  # Si el archivo no existe, no hacemos nada

def guardar_datos():
    
    with open('data.txt', 'w') as file: 
        for p in productos: #navega en productos(cuenta)
            file.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

def añadir_producto():
   
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad disponible: "))
    
    #guardar los datos en un diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():

    if not productos:
        print("No hay productos disponibles.")
        return
    
    print("Productos disponibles:")
    for p in productos:
        print(f"Nombre: {p['nombre']}, Precio: {p['precio']}, Cantidad: {p['cantidad']}")

def actualizar_producto():
  
    nombre = input("Introduce el nombre del producto que deseas actualizar: ")
    for p in productos:
        if p['nombre'] == nombre:
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            if nuevo_nombre:
                p['nombre'] = nuevo_nombre # sutituye el nombre
            nuevo_precio = input("Introduce el nuevo precio: ")
            if nuevo_precio:
                p['precio'] = float(nuevo_precio) #sutituye el precio
            nueva_cantidad = input("Introduce la nueva cantidad: ")
            if nueva_cantidad:
                p['cantidad'] = int(nueva_cantidad) # sutituye la cantidad
            print(f"Producto '{nombre}' actualizado.")
            return
    
    print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto():
    
    nombre = input("Introduce el nombre del producto que deseas eliminar: ")
    global productos
    productos = [p for p in productos if p['nombre'] != nombre]
    
    print(f"Producto '{nombre}' eliminado." if len(productos) < len(productos) else f"Producto '{nombre}' eliminado.")

def menu():
  
    cargar_datos()  # Carga los datos al iniciar
    while True:
        print("                    ")
        print("Bienvenidos al supermecado")
        print("-------------------------")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos Guardados ")
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()