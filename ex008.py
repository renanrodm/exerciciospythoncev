#Escreva um programa que leia um valor em metros e a exiba convertido em centímetros e milimetros.
m = float(input('Digite um valor em metros: '))
print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(m, (m/1000), (m/100), (m/10), (m*10), (m*100), (m*1000)))