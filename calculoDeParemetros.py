#Autor: Aziel de Fontes Melo
#Data: 05/03/2024

pi = 3.14159265359

#Tabela para filtros butterworth
a = [1.414214, 1, 0.765367, 0.618034, 0.517638, 0.445042, 0.390181]
b = 1

print("Olá, Escreva abaixo o valor da frequência de corte desejada:")
fc = int(input())
print("Agora, escreva abaixo o valor do ganho máximo desejado (maior que 1):")
k = float(input())

C_2 = 10 / fc
C_2 = round(C_2, 3)

# valor comercial para C_2

C_1 = 0.9 * ((a[0]**2+4*b*(k-1))*C_2)/(4*b)
R_1 = 2/((a[0]*C_2+((a[0]**2+4*b*(k-1))*C_2**2-4*b*C_1*C_2)**(1/2))*fc*2*pi)
R_2 = 1 / (b*C_1*C_2*R_1*(2*pi*fc)**2)
R_3 = (k*(R_1+R_2))/(k-1)
R_4 = k*(R_1+R_2)

print("C_2 = " + str(C_2*10**9/10000) + " nF")
print("C_1 = " + str(C_1*10**9/10000) + " nF")
print("R_1 = " + str(R_1*10000) + " ohm")
print("R_2 = " + str(R_2*10000) + " ohm")
print("R_3 = " + str(R_3*10000) + " ohm")
print("R_4 = " + str(R_4*10000) + " ohm")
