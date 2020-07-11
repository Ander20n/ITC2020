'''1. Escreva um script Python para simular um AFD. 
Ler o AFD como tabela, ler uma palavra e da como saida reconhece ou nao.

para que o script funcione corretamente, e preciso que as informacoes sejam informadas respeitando os espacos do o exemplo abaixo

Estados: A B C 
Simbolos do alfabeto: 0 1
Transicao x: A 1 B
Estado(os) Final(ais): A B
'''



def saberEstado(letraAlfabeto, estado, listaTransicoes):
    for x in range(len(listaTransicoes)):
        estadoELetra = estado + ' ' + letraAlfabeto
        if estadoELetra in listaTransicoes[x]:
            novoEstado = listaTransicoes[x][4]
            break
    return novoEstado

estados = input("Estados: ")
simbolosAlfabeto = input("Simbolos do alfabeto: ")

quantidadeTransicoes = int (input("Quantidade de transicoes: "))

listaTransicoes = []
for xTransicoes in range(quantidadeTransicoes):
    condicao = True
    while condicao:
        transicoes = input ("Transicao %s: " % (xTransicoes+1))
        if transicoes[2] in simbolosAlfabeto and transicoes[0] in estados and transicoes[4] in estados:
            listaTransicoes.append(transicoes)
            condicao = False
        else:
            print("A transicao possui estados ou simbolos que nao estao nos esatdos e simbolos informados")

estadoInicial = input("Estado Inicial: ")
estadoFinal = input("Estado(os) Final(ais): ")

quantidadePalavras = int(input("Quantidade de palavras: "))

listaPalavras = []
for xPalavras in range(quantidadePalavras):
    condicaoPalavra = True
    while condicaoPalavra:
        palavras = input("Palavra %s: " % (xPalavras+1))
        validacao = ""
        for confereLetra in range(len(palavras)):
            if palavras[confereLetra] in simbolosAlfabeto:
                continue
            else:
                print("A palavra contem caracteres que nao fazem parte do alfabeto")
                validacao = "parada"
                break
        if validacao == '':
            condicaoPalavra = False
        else:
            condicaoPalavra = True
    listaPalavras.append(palavras)

resultado = []

for todasPalavras in range(len(listaPalavras)):
    palavra = listaPalavras[todasPalavras]
    estadoAtual = estadoInicial
    for letra in range(len(palavra)):
        ultimoEstado = saberEstado(palavra[letra], estadoAtual, listaTransicoes)
        estadoAtual = ultimoEstado
    if estadoAtual in estadoFinal:
        resultado.append(palavra + ' - reconhece')
    else:
        resultado.append(palavra + ' - nao reconhece')

print(resultado)