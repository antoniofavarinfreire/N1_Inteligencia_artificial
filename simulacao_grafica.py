import pygame
import random

# Inicializa o pygame
pygame.init()

# Defina as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Lista para armazenar as entregas
entregas = []

# Lê o arquivo de entrada
with open('entregas.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.strip().split()
        if len(partes) == 3:
            entrega, valor, tempo_inicio = partes
            entregas.append((entrega, int(valor), int(tempo_inicio)))

# Inicializa a tela do pygame
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Leilão de Entregas")

# Parâmetros do leilão
lance_atual = 0
melhor_entrega = None
tempo_atual = 0
lucro_total = 0

# Função para realizar o leilão
def realizar_leilao():
    global lance_atual, melhor_entrega, lucro_total, tempo_atual
    lance_atual = random.randint(1, 30)  # Gere um lance aleatório
    melhor_entrega = None
    
    for entrega, valor, tempo_inicio in entregas:
        if tempo_inicio >= tempo_atual and valor >= lance_atual:
            if melhor_entrega is None or valor > melhor_entrega[1]:
                melhor_entrega = (entrega, valor, tempo_inicio)

    if melhor_entrega:
        tempo_atual += melhor_entrega[2]
        lucro_total += melhor_entrega[1]
        entregas.remove(melhor_entrega)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                realizar_leilao()

    screen.fill(WHITE)

    # Exibe informações na tela
    texto_tempo_atual = FONT.render("Tempo Atual: " + str(tempo_atual), True, BLACK)
    texto_lance_atual = FONT.render("Lance Atual: $" + str(lance_atual), True, BLACK)
    texto_melhor_entrega = FONT.render("Melhor Entrega: " + (melhor_entrega[0] if melhor_entrega else "Nenhuma"), True, BLACK)
    texto_lucro_total = FONT.render("Lucro Total: $" + str(lucro_total), True, BLACK)

    screen.blit(texto_tempo_atual, (50, 50))
    screen.blit(texto_lance_atual, (50, 100))
    screen.blit(texto_melhor_entrega, (50, 150))
    screen.blit(texto_lucro_total, (50, 200))

    pygame.display.flip()

# Encerra o pygame
pygame.quit()
