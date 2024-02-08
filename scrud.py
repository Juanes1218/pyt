import json
from operator import itemgetter

def cargar_json(Archivo_json):
  with open(Archivo_json, 'r') as Archivo:
    data = json.load(Archivo)
  return data 
Archivo_json=("Archivo.json")

print("## EJERCICIO 1 ## ")


def fechas_recientes(Archivo_json):
  data = cargar_json(Archivo_json)
  pedidos = data['ventas']['pedidos']
  pedidos_ordenados = sorted(pedidos, key=lambda x: x["fecha"], reverse=True)
  for i in pedidos_ordenados:
     print(i)

print(fechas_recientes(Archivo_json))



print("## EJERCICIO 2 ## ")



def Mayor_Valor(Archivo_json):
  data = cargar_json(Archivo_json)
  pedidos = data['ventas']['pedidos']
  pedidos_ordenados_por_valor = sorted(pedidos, key=lambda x: x['total'], reverse=True)
  dos_pedidos_mas_valorados = pedidos_ordenados_por_valor[:2]
  for i in dos_pedidos_mas_valorados:
    print(i)

print(Mayor_Valor(Archivo_json))


print("## EJERCICIO 3 ## ")


def indentificadores_clientes(Archivo_json):
  data = cargar_json(Archivo_json)
  pedidos = data['ventas']['pedidos']
  clientes_pedidos = set()
  for pedido in pedidos:
    clientes_pedidos.add(pedido['id_cliente'])
  return list(clientes_pedidos)


print(indentificadores_clientes(Archivo_json))


print("## EJERCICIO 4 ## ")


def pedidos_2017_mayor_500(Archivo_json):
  data = cargar_json(Archivo_json)
  pedidos = data['ventas']['pedidos']
  pedidos_2017_mayor_500 = [pedido for pedido in pedidos if pedido['fecha'].startswith('2017') and pedido['total'] > 500]
  for i in pedidos_2017_mayor_500:
    print(i)
    

print(pedidos_2017_mayor_500(Archivo_json))


print("## EJERCICIO 5 ## ")


def comerciales_comision(Archivo_json):
  data = cargar_json(Archivo_json)
  comerciales = data['ventas']['comerciales']
  comision_005_011 = [comercial for comercial in comerciales if 0.05 <= comercial['comision'] <= 0.11]
  for i in comision_005_011:
    print(i)


comerciales_comision(Archivo_json)


print("## EJERCICIO 6 ## ")


def comision_MayorValor(Archivo_json):
  data = cargar_json(Archivo_json)
  comerciales = data['ventas']['comerciales']
  comision = [comercial['comision'] for comercial in comerciales ]
  comision_alta = max(comision)
  return comision_alta

print(comision_MayorValor(Archivo_json))


print("## EJERCICIO 7 ## ")



def clientes_sevilla(Archivo_json):
  data = cargar_json(Archivo_json)
  clientes = data['ventas']['clientes']
  ciudad_sevilla = [cliente for cliente in clientes if cliente['ciudad'] == 'Sevilla']
  ciudad_sevilla_ordenada = sorted(ciudad_sevilla, key = itemgetter('nombre','apellido1'))
  for i in ciudad_sevilla_ordenada:
    print(i)


print(clientes_sevilla(Archivo_json))

print("## EJERCICIO 8 ## ")


def clientes_An(Archivo_json):
  data = cargar_json(Archivo_json)
  clientes = data['ventas']['clientes']
  clientes_filtrados = [cliente['nombre'] for cliente in clientes if cliente['nombre'].startswith('A') and cliente['nombre'].endswith('n')]
  clientes_filtrados += [cliente['nombre'] for cliente in clientes if cliente['nombre'].startswith('P')]
  clientes_filtrados_ordenados = sorted(clientes_filtrados)
  return clientes_filtrados_ordenados

print(clientes_An(Archivo_json))


print("## EJERCICIO 9 ## ")


def clientes_A(Archivo_json):
  data = cargar_json(Archivo_json)
  clientes = data['ventas']['clientes']
  clientes_A = [cliente['nombre'] for cliente in clientes if cliente['nombre'].startswith('A')]
  clientes_A_ordenados = sorted(clientes_A)
  return clientes_A_ordenados


print(clientes_A(Archivo_json))

print("## EJERCICIO 10 ## ")

def comerciales_Ruiz(Archivo_json):
  data = cargar_json(Archivo_json)
  comerciales = data['ventas']['comerciales']
  comerciales_ruiz = set()
  for comercial in comerciales:
    if 'Ruiz' in comercial.values():
      comerciales_ruiz.add(comercial['nombre'])
  return list(comerciales_ruiz)
  
print(comerciales_Ruiz(Archivo_json))



