'''Faça um programa que tenha um função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é maior'''
def maior(*nums):
    print('-='*30)
    print('Analisando os valores passados...')
    if len(nums) == 0:
        print(f'Não foram informados valores.')
    else:
        mai = 0
        for c in nums:
            print(c, end=' ')
            if c > mai:
                mai = c
        print(f'Foram informados {len(nums)} valores ao todo.')
        print(f'O maior valor informado foi {mai}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()