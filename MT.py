# coding: utf-8
import sys

'''
Modo de uso: 

O programa deve rodar via linha de comandos (shell) como: python MT.py transicoes.txt "cadeia"

A tabela da MT no arquivo deve conter uma transicao por linha na forma:
qx s px t m 
significando δ(q,s)=(p,t,m)
A primeira linha tem o estado inicial. 
A segunda linha tem o(os) estado(os) final(is)
A demais linhas contem as transicoes.

Para representar um movimento para direita é necessário utilizar a letra D maiúscula
Para representar um movimento para esquerda é necessário utilizar a letra E maiúscula
Para representar um símbolo branco é necessário utilizar a letra B maiúscula
''' 

tabelaCMD = 'transicoes.txt'

cadeiaCMD = '00111'
entrada = []
for posicaoEntrada in range(len(cadeiaCMD)):
    entrada += cadeiaCMD[posicaoEntrada]

estadosTransicoes = open(tabelaCMD, 'r')
estadoInicial = estadosTransicoes.readline().rstrip('\n')
estadoFinal = estadosTransicoes.readline().rstrip('\n')
transicoes = []
estadosComTransicoes = []

for linha in estadosTransicoes:
    conteudoLinha = linha.rstrip('\n')
    transicoes.append(conteudoLinha)
    estadoX = linha[:2]
    if estadoX not in estadosComTransicoes:
        estadosComTransicoes.append(estadoX)

estadoAtual = estadoInicial
posicaoCabecote = 0

def conferirTransicao(estado, simbolo, transicoes):
    novoEstado = ''
    for x in range(len(transicoes)):
        estadoLetraAtuais = estado + ' ' + simbolo
        if estadoLetraAtuais in transicoes[x][:4]:
            novoEstado = transicoes[x][5:7]
            novoSimbolo = transicoes[x][8]
            movimento = transicoes[x][-1]
            break
    if novoEstado == '':
        return 'break','break', 'break'
    return novoEstado, novoSimbolo, movimento

while True:
    simboloFita = entrada[posicaoCabecote]
    estadoAtual, simboloFita, movimento = conferirTransicao(estadoAtual, simboloFita, transicoes)
    if estadoAtual == 'break':
        estadoAtual = 'break'
        break
    else:
        entrada[posicaoCabecote] = simboloFita
        if movimento == 'D':
            posicaoCabecote += 1
            if posicaoCabecote >= len(entrada):
                entrada.append('B')
        elif movimento == 'E':
            posicaoCabecote -= 1
        if estadoAtual not in estadosComTransicoes:
            break
        
if estadoAtual == estadoFinal:
    print("%s - Cadeia aceita" % cadeiaCMD)
else:
    print("%s - Cadeia não aceita" % cadeiaCMD)
