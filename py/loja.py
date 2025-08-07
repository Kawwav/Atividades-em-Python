# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura de tinta é de 1 litro para cada 3 metros quadrados.
# E que a tinta é vendida em latas de 18 litro, que custam R$ 80,00.
# Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.

CUSTO_LATA = 80

metro_quadrados = int(input("Quantidade de metros quadrado:"))

litros, resto = divmod(metro_quadrados, 3)

if resto > 0:
    litros += 1

latas, adicional = divmod(litros,18)

if adicional > 0:
    latas += 1

custo = latas * CUSTO_LATA
 
print("Quantida de latas de tintas:", latas)
print(f"Custo total: R${custo}")