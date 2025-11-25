
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sumar_lista(lista):
    if lista == []:
        return 0
    return lista[0] + sumar_lista(lista[1:])



class Medicamento:
    nombre = "Ibuprofeno"
    categoria = "Analgésico"
    stock = 8
    precio = 2000
    codigo_barras = "12345"

    def vender(cantidad):
        if cantidad > Medicamento.stock:
            print("No hay stock.")
        else:
            Medicamento.stock -= cantidad

    def reponer_stock(cantidad):
        Medicamento.stock += cantidad

    def esta_en_stock_critico():
        return Medicamento.stock < 10



m = Medicamento


print(factorial(5))
print(sumar_lista([1,2,3,4]))

m.vender(3)
print(m.stock)
print(m.esta_en_stock_critico())