# #............0...1.....2.........3....4
# #...........-5..-4....-3........-2...-1

# list_test = [12, True, 'Felipe', 1.2, []]

# list_test[-3] = 'Maria'

# print(list_test)
# print(list_test[2], type(list_test[2]))

lista = [10, 20, 30, 40]
lista[2] = 300
numero = lista[2]
print(lista)
del lista[2]
print(numero)
print(lista)
lista.append(50)
lista.pop()
lista.append(60)
ultimo_valor = lista.pop()
print(lista, 'Removido,', ultimo_valor)
lista.insert(2, 25)
print(lista)