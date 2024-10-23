#Sistema de Compras de Ropas con POO
class Producto:
    def __init__(self, nombre, precio, talla):
        self._nombre = nombre
        self._precio = precio
        self._talla = talla

    def obtener_precio(self):
        return self._precio

    def mostrar_informacion(self):
        return f"Producto: {self._nombre} - Precio: ${self._precio} - Talla: {self._talla}"


class Camisa(Producto):
    def __init__(self, nombre, precio, talla, tipo_manga):
        super().__init__(nombre, precio, talla)
        self._tipo_manga = tipo_manga

    def mostrar_informacion(self):
        manga = "Larga" if self._tipo_manga else "Corta"
        return f"{super().mostrar_informacion()} - Manga: {manga}"


class Pantalon(Producto):
    def __init__(self, nombre, precio, talla, tipo_corte):
        super().__init__(nombre, precio, talla)
        self._tipo_corte = tipo_corte

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Corte: {self._tipo_corte}"


class Zapato(Producto):
    def __init__(self, nombre, precio, talla, tipo_material):
        super().__init__(nombre, precio, talla)
        self._tipo_material = tipo_material

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Material: {self._tipo_material}"


class Tienda:
    def __init__(self):
        self.productos = []

    def agg_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("\nProductos:")
        for i, producto in enumerate(self.productos):
            print(f"{i + 1}. {producto.mostrar_informacion()}")

    def procesar_compra(self, indices_seleccionados):
        total = 0
        print("\nProductos seleccionados:")
        for indice in indices_seleccionados:
            producto = self.productos[indice - 1]
            print(producto.mostrar_informacion())
            total += producto.obtener_precio()
        print(f"\nTotal a pagar: ${total:.2f}")


camisa = Camisa("Camisa Blanca", 20.0, "M", tipo_manga=True)
pantalon = Pantalon("Pantalon Negro", 30.0, "L", tipo_corte="Slim")
zapato = Zapato("Zapato Elegante", 50.0, 42, tipo_material="Cuero")

tienda = Tienda()
tienda.agg_producto(camisa)
tienda.agg_producto(pantalon)
tienda.agg_producto(zapato)


print("Bienvenido a la tienda de ropa!")
comprando = True
indices_seleccionados = []

while comprando:
    tienda.mostrar_productos()
    seleccion = input("Selecciona el número del producto que quieres ('0' para finalizar la compra): ")
    if seleccion == '0':
        comprando = False
    elif seleccion.isdigit() and 1 <= int(seleccion) <= len(tienda.productos):
        indices_seleccionados.append(int(seleccion))
        print("Producto añadido.")
    else:
        print("Error, intenta de nuevo.")

if indices_seleccionados:
    tienda.procesar_compra(indices_seleccionados)
else:
    print("Gracias por visitar la tienda!")
