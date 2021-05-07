"""
Created on Fri May  7 15:48:48 2021

@author: Everton Andrade
"""

#Média de notas:
    
    
nome = input('Insira seu nome: ')

nota1 = float(input('Sua primeira nota foi: '))
nota2 = float(input('Sua segunda nota foi: '))

print('Olá', nome, 'suas notas foram:')
print(nota1, 'e', nota2)

soma = nota1 + nota2
media = soma/2

print('Sua média é', media)
