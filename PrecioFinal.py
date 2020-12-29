# alpha by dev-lang

from decimal import Decimal

# FUNCION PARA DEFINIR VALOR

Flag_Dolar = 1	# para funcion futura entre pesos y dolares # no implementada

# INGRESO DE DOLARES
dolar = input("Inserte valor en dolares: ")

precio_pesos = input("Ingrese valor en pesos: ")

# VARIABLES

ivav = 0.21
paisv = 0.08
gananciasv = 0.35
dolarv = 88.5


def Armar_Variables_Dolar(dolar):
	global ingreso
	global iva
	global pais
	global ganancias
	global total
	precio_prueba = float(dolar) * dolarv
	ingreso = precio_prueba
	iva = precio_prueba * ivav
	iva = str(int(iva)) + str(Decimal(str(iva)) % 1)[1:4]
	iva = float(iva)
	pais = precio_prueba * paisv
	pais = str(int(pais)) + str(Decimal(str(pais)) % 1)[1:4]
	pais = float(pais)
	ganancias = precio_prueba * gananciasv
	ganancias = str(int(ganancias)) + str(Decimal(str(ganancias)) % 1)[1:4]
	ganancias = float(ganancias)
	total = precio_prueba + iva + pais + ganancias
	total = str(int(total)) + str(Decimal(str(total)) % 1)[1:4]

def Armar_Variables_Pesos(precio_pesos):
	global ingreso
	global iva
	global pais
	global ganancias
	global total
	global precio_pesos_dolar
	ingreso = float(precio_pesos)
	iva = ingreso * ivav
	iva = str(int(iva)) + str(Decimal(str(iva)) % 1)[1:4]
	iva = float(iva)
	pais = ingreso * paisv
	pais = str(int(pais)) + str(Decimal(str(pais)) % 1)[1:4]
	pais = float(pais)
	ganancias = ingreso * gananciasv
	ganancias = str(int(ganancias)) + str(Decimal(str(ganancias)) % 1)[1:4]
	ganancias = float(ganancias)
	total = ingreso + iva + pais + ganancias
	precio_pesos_dolar = ingreso / dolarv
	precio_pesos_dolar = str(int(precio_pesos_dolar)) + str(Decimal(str(precio_pesos_dolar)) % 1)[1:4]


def Mostrar_Calculo(dolar):
	print("Ingreso de: ", "USD", dolar, "AR", ingreso)
	print("\nIVA: ", iva, 
		"Impuesto PAIS: ", pais, 
		"RG 4815/2016 (ganancias)", ganancias)
	print("\nConsumo total: ", total)




Armar_Variables_Dolar(dolar)
Mostrar_Calculo(dolar)
print("=========================================")
Armar_Variables_Pesos(precio_pesos)
Mostrar_Calculo(precio_pesos_dolar)
print("=========================================")
