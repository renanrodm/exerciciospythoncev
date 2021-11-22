'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colação. Depois mostre:
A) Apenas os 5 primeiros colocados;
B) Os últimos 4 colocados da tabela;
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.'''

tabela = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Corinthians', 'Internacional', 'Fluminense', 'Athletico-PR', 'Cuiabá', 'Ceará', 'Atlético-GO', 'São Paulo', 'Juventude', 'América-MG', 'Santos', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')

print(f'Os 5 primeiros são: {tabela[:5]}')
print(f'Os 4 últimos são: {tabela[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}º posição')