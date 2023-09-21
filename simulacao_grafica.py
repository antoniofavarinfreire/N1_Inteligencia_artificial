import pygame
import sys

# Inicialização do pygame
pygame.init()

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Tamanho da janela
WIDTH, HEIGHT = 800, 600

# Inicialização da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação de Leilão de Entregas")

# Fonte para exibir texto
font = pygame.font.Font(None, 36)

# Lista de eventos de entrega no formato (tempo, destino, valor)
eventos_entrega = [
    (0, "Destino A", 50),
    (5, "Destino B", 40),
    (10, "Destino C", 30),
    # Adicione mais eventos de entrega conforme necessário
]

# Variáveis para rastrear o tempo e as entregas programadas
tempo_atual = 0
entregas_programadas = []
lucro_total = 0  # Variável para rastrear o lucro total
running = True  # Variável para controlar a execução do programa

# Função para agendar entregas no momento atual
def agendar_entregas():
    for evento in eventos_entrega:
        if evento[0] == tempo_atual:
            entregas_programadas.append(evento)
    eventos_entrega[:] = [evento for evento in eventos_entrega if evento[0] > tempo_atual]
    
# Função para calcular o lucro total das entregas programadas
def calcular_lucro(evento):
    
    if event[0] == tempo_atual:
        lucro = sum(evento[2] for evento in entregas_programadas)
    return lucro

# Função para encerrar o programa de forma controlada
def encerrar_programa():
    global running
    running = False

# Loop principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpar a tela
    screen.fill(WHITE)

    # Agendar entregas no tempo atual
    agendar_entregas()

    # Desenhar entregas programadas
    for i, entrega in enumerate(entregas_programadas):
        text = font.render(f"Entrega para {entrega[1]}: R${entrega[2]}", True, BLACK)
        screen.blit(text, (50, 100 + i * 40))
        print(len(entrega))
        # print(len(eventos_entrega))
        calcular_lucro(entrega)
        # if len(eventos_entrega) > 0:
        #     if entrega[0] == tempo_atual:
        #         lucro_total += entrega[2]  
        

    # Exibir tempo atual
    tempo_text = font.render(f"Tempo Atual: {tempo_atual}", True, BLACK)
    screen.blit(tempo_text, (50, 50))
    
    lucro_text = font.render(f"Lucro Atual: R${lucro_total}", True, BLACK)
    screen.blit(lucro_text, (350, 50))

    # Adicionar botão para encerrar o programa
    pygame.draw.rect(screen, BLUE, (50, 350, 150, 50))
    encerrar_text = font.render("Encerrar", True, WHITE)
    screen.blit(encerrar_text, (60, 360))

    # Verificar se o botão de encerrar foi clicado
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if 50 <= mouse_x <= 200 and 350 <= mouse_y <= 400:
        pygame.draw.rect(screen, BLACK, (50, 350, 150, 50), 2)  # Destacar o botão se o mouse estiver sobre ele
        if pygame.mouse.get_pressed()[0]:  # Verificar se o botão do mouse foi clicado
            encerrar_programa()

    # Atualizar a tela
    pygame.display.flip()

    # Avançar o tempo
    if eventos_entrega:
        tempo_atual += 1

    # Controlar a taxa de atualização da tela
    pygame.time.delay(350)

# Exibir o lucro total quando a simulação terminar
print("Lucro Total:", lucro_total)

# Encerrar o pygame
pygame.quit()
sys.exit()





 