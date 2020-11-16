# coding: utf-8
import sys

'''
Código que transforma as transições em um número decimal

O código deve ser rodado via prompt de comando, como o seguinte exemplo: 

python MTUdecimal.py tMTU.txt

Você pdoe utilizar o arquivo com o nome que desejar, vale lembrar que o arquivo deve estar no mesmo local que o MTUdecimal.py

Cada linha deverá ser escrita com o seguinte padrão:

q0 0 q1 0 R

Com as informações separadas por um espaço.

- A primeira informação (q0) é do estado atual, ele precisa ser escrito com a letra q seguida do número que representa o estado
- A segunda informação (0) é o estado lido
- A terceira informação (q1) é o próximo estado, ele precisa ser escrito com a letra q seguida do número que representa o estado
- A quarta informação é o símbolo que será escrito
- A quinta informação é o movimento da fita, ele precisa ser R, L ou STOP.
'''

arquivo = sys.argv[1]
entradaCMD = open(arquivo, 'r')

estadosTransicoes = entradaCMD.readlines()

entrada = []
for posicaoEstadoTransicao in range(len(estadosTransicoes)):
    limpaTransicao = estadosTransicoes[posicaoEstadoTransicao].rstrip("\n")
    estadoTransicao = limpaTransicao.split(" ")
    entrada.append(estadoTransicao)

transicao = ""
for posicaoEntrada in range(len(entrada)):
    transicaoConfere = ""
    estadoLido = entrada[posicaoEntrada][2][1:]
    transicaoConfere += bin(int(estadoLido))[2:]
    transicaoConfere += entrada[posicaoEntrada][3]
    transicaoConfere += entrada[posicaoEntrada][4]
    if transicaoConfere[0:2] == '01':
        transicaoConfere = '1' + entrada[posicaoEntrada][4]
    elif transicaoConfere == '00R':
        transicaoConfere = 'R'
    elif '00R' in transicaoConfere:
        posTroca = transicaoConfere.index('00R')
        if transicaoConfere[posTroca-1:posTroca+3] != 'R00R' or transicaoConfere[posTroca-1:posTroca+3] != 'L00R' or transicaoConfere[posTroca-1:posTroca+3] != 'P00R': 
            pass
        else:
            transicaoConfere = transicaoConfere.replace('00R', 'R')
    transicao += transicaoConfere

binarioUMT = ""
for posicaoTransicao in range(len(transicao)):
    if transicao[posicaoTransicao] == '0':
        binarioUMT += '0'
    elif transicao[posicaoTransicao] == '1':
        binarioUMT += '10'
    elif transicao[posicaoTransicao] == 'R':
        binarioUMT += '110'
    elif transicao[posicaoTransicao] == 'L':
        binarioUMT += '1110'
    elif transicao[posicaoTransicao:posicaoTransicao+4] == 'STOP':
        binarioUMT += '11110'
    
if binarioUMT == '110110' or binarioUMT == '110':
    print(0)
else:
    binarioUMT = binarioUMT[3:-3]
    decimal = int(binarioUMT,2)
    print(decimal)