import time
import matplotlib.pyplot as plt
def leilao_entregas_versao1(destinos_conexoes, entregas):
    lucro_total = 0
    tempo_atual = 0

    for horario, destino, bonus in entregas:
        for origem, proximo_destino, tempo in destinos_conexoes:
            if origem == destino:
                tempo_atual += tempo
                break

        lucro_total += bonus
    return lucro_total, tempo

 

# Exemplo de uso:
destinos_conexoes = [("A", "B", 5), ("B", "C", 3), ("A", "D", 2), ("C", "D", 8)]
entregas = [(0, "B", 1), (5, "C", 10), (10, "D", 8)]

 

lucro_versao1, tempo = leilao_entregas_versao1(destinos_conexoes, entregas)
print("Lucro total (Versão 1):", lucro_versao1)
print("Tempo (Versão 1): ", tempo)
print("")
 

 

def leilao_entregas_versao2(destinos_conexoes, entregas):
    lucro_maximo = 0
    tempo_atual = 0

    # Ordenar as entregas pelo horário
    entregas.sort(key=lambda x: x[0])

    for horario, destino, bonus in entregas:
        melhor_lucro_entrega = bonus
        melhor_tempo_entrega = 0

        for origem, proximo_destino, tempo in destinos_conexoes:
            if origem == destino:
                tempo_atual += tempo
                break

            if tempo_atual + tempo <= horario:
                if bonus > melhor_lucro_entrega:
                    melhor_lucro_entrega = bonus
                    melhor_tempo_entrega = tempo

        lucro_maximo += melhor_lucro_entrega
        tempo_atual += melhor_tempo_entrega
    return lucro_maximo, tempo_atual

 

# Exemplo de uso:
lucro_versao2, tempo = leilao_entregas_versao2(destinos_conexoes, entregas)
print("Lucro máximo (Versão 2):", lucro_versao2)
print("Tempo (Versão 2):", tempo)
print("")

def leilao_entregas_versao3(destinos_conexoes, entregas):
    entregas = sorted(entregas, key=lambda x: x[0])  # Ordena as entregas por horário
    lucro_maximo = 0
    caminho_otimo = []

 

    for i in range(len(entregas)):
        horario, destino, bonus = entregas[i]
        tempo_atual = horario
        caminho = [(horario, destino, bonus)]
        lucro = bonus

 

        for j in range(i, len(entregas)):
            for origem, proximo_destino, tempo in destinos_conexoes:
                if origem == destino:
                    tempo_destino = tempo
                    break

 

            if tempo_atual + tempo_destino <= entregas[j][0]:
                destino = entregas[j][1]
                horario = entregas[j][0]
                bonus = entregas[j][2]
                tempo_atual += tempo_destino
                caminho.append((horario, destino, bonus))
                lucro += bonus

        if lucro > lucro_maximo:
            lucro_maximo = lucro
            caminho_otimo = caminho

 
    
    return lucro_maximo, caminho_otimo, tempo_atual

 

# Exemplo de uso com os dados fornecidos:
destinos_conexoes = [("A", "B", 5), ("B", "C", 3), ("A", "D", 2), ("C", "D", 8)]
entregas = [(0, "B", 1), (5, "C", 10), (10, "D", 8)]

 

lucro, caminho, tempo = leilao_entregas_versao3(destinos_conexoes, entregas)
print("Lucro máximo:", lucro)
print("Caminho ótimo:", caminho)
print("Tempo ótimo:", tempo)

# Medir o tempo de execução e o lucro para cada versão
tempo_inicio = time.time()
lucro_versao_a = leilao_entregas_versao1(destinos_conexoes, entregas)
tempo_versao_a = time.time() - tempo_inicio

tempo_inicio = time.time()
lucro_versao_b = leilao_entregas_versao2(destinos_conexoes, entregas)
tempo_versao_b = time.time() - tempo_inicio

tempo_inicio = time.time()
lucro_versao_c = leilao_entregas_versao3(destinos_conexoes, entregas)
tempo_versao_c = time.time() - tempo_inicio

# Imprimir os resultados
print("Versão A:")
print("Tempo de Execução:", tempo_versao_a)
print("Lucro Obtido:", lucro_versao_a)

print("Versão B:")
print("Tempo de Execução:", tempo_versao_b)
print("Lucro Obtido:", lucro_versao_b)

print("Versão C:")
print("Tempo de Execução:", tempo_versao_c)
print("Lucro Obtido:", lucro_versao_c)



# Dados para o gráfico
versoes = ["Versão A", "Versão B", "Versão C"]
tempos = [tempo_versao_a, tempo_versao_b, tempo_versao_c]

# Criar o gráfico de barras
plt.bar(versoes, tempos)
plt.xlabel("Versões")
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Comparação de Tempo de Execução")
plt.show()
