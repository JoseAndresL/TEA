# Tendencias e Innovacion en Tecnologia Agricola (TEA)
#
from unicodedata import numeric

horas = input("horas trabajadas?")
print(horas)
print(type(horas))
valorPorHora = input("valor por hora?")
print(valorPorHora)
print(type(valorPorHora))
numeric =[int(horas) * int(valorPorHora)]
print(numeric)


# se uutiliza la conversion de tipo a int
# si no se hace la conversion existira error porque trata de multiplicar strings
# total = int(horas)- (valorPorHora)

#print(total)

# solo falta imprimir el tipo
