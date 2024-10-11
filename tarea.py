class Producto:
    def __init__(self, codigo, nombre, precio, cantidad, bodega):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.bodega = bodega

    def __repr__(self):
        return (f"Código: {self.codigo}, Nombre: {self.nombre}, "
                f"Precio: {self.precio}, Cantidad: {self.cantidad}, "
                f"Bodega: {self.bodega}")


class SistemaInventario:
    def __init__(self):
        self.catalogo = {}

    def agregar_producto(self, codigo, nombre, precio, cantidad, bodega):
        if codigo in self.catalogo:
            print("El producto ya está registrado. Usa la opción de modificar.")
        else:
            nuevo_producto = Producto(codigo, nombre, precio, cantidad, bodega)
            self.catalogo[codigo] = nuevo_producto
            print("Producto agregado con éxito.")

    def actualizar_producto(self, codigo, **atributos):
        if codigo in self.catalogo:
            for key, valor in atributos.items():
                if hasattr(self.catalogo[codigo], key):
                    setattr(self.catalogo[codigo], key, valor)
            print("Producto actualizado con éxito.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.catalogo:
            del self.catalogo[codigo]
            print("Producto eliminado con éxito.")
        else:
            print("Producto no encontrado.")

    def mostrar_producto(self, codigo):
        if codigo in self.catalogo:
            print(self.catalogo[codigo])
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, busqueda):
        resultados = [producto for producto in self.catalogo.values()
                      if busqueda in (producto.codigo, producto.nombre)]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos.")


if __name__ == "__main__":
    inventario = SistemaInventario()

    inventario.agregar_producto("001", "Laptop", 1000, 10, "Bodega A")
    inventario.agregar_producto("002", "Teclado", 50, 25, "Bodega B")

    inventario.mostrar_producto("001")

    inventario.actualizar_producto("001", precio=900, cantidad=15)

    inventario.eliminar_producto("002")

    inventario.buscar_producto("Laptop")
    inventario.buscar_producto("002")  # No debería encontrar nada
