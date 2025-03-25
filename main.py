import pygame
import math
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube

def draw_text(x, y, text, font):
    """
    Renderiza um texto na posição (x,y) da janela utilizando OpenGL,
    com fundo transparente (usando alpha).
    """
    # Ativa blending para respeitar o canal alpha do texto
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Renderiza o texto (antialias=True) com cor branca e converte para surface com alpha
    text_surface = font.render(text, True, (255, 255, 255))
    text_surface = text_surface.convert_alpha()

    # Converte o surface em dados de pixel para OpenGL
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

    glDisable(GL_BLEND)

def generate_stars(num_stars, range_x, range_y, range_z):
    """
    Gera uma lista de posições para as estrelas.
    """
    stars = []
    for _ in range(num_stars):
        x = random.uniform(-range_x, range_x)
        y = random.uniform(-range_y, range_y)
        z = random.uniform(-range_z, -5)  # Posiciona as estrelas mais distantes que a nave
        stars.append((x, y, z))
    return stars

def draw_stars(stars):
    """
    Desenha as estrelas como pontos brancos.
    """
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    for star in stars:
        glVertex3fv(star)
    glEnd()

def main():
    # Inicializa o Pygame e configura a janela
    pygame.init()
    screen_width = 1000
    screen_height = 800
    pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Nave Espacial Interativa")

    # Configurações do OpenGL
    glClearColor(0.0, 0.0, 0.0, 1)
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
    glViewport(0, 0, screen_width, screen_height)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -30)

    # Instância da nave espacial (baseada no cubo)
    spaceship = Cube()
    # Gera estrelas
    stars = generate_stars(300, 50, 50, 50)

    # Parâmetros de transformação
    rotation_angle = 0.0
    translation_offset = 0.0
    scaling_factor = 1.0
    manual_tx, manual_ty = 0.0, 0.0

    # Flags para controlar os efeitos
    rotation_on = True
    translation_on = True
    scaling_on = True
    mirroring_on = False

    # Velocidades e amplitudes
    rotation_speed = 90       # graus por segundo
    translation_amplitude = 3.0
    # Aumente aqui para deixar a nave (cubo) maior
    scaling_base = 2.0
    scaling_variation = 0.5
    movement_speed = 5.0  # velocidade de movimento manual (unidades por segundo)

    # Configuração da fonte para overlay
    font = pygame.font.SysFont("Arial", 18)

    clock = pygame.time.Clock()
    running = True
    time_elapsed = 0.0

    while running:
        dt = clock.tick(60) / 1000.0  # delta time em segundos
        time_elapsed += dt

        # Processa eventos discretos
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    running = False
                elif event.key == K_r:
                    rotation_on = not rotation_on
                elif event.key == K_t:
                    translation_on = not translation_on
                elif event.key == K_s:
                    scaling_on = not scaling_on
                elif event.key == K_e:
                    mirroring_on = not mirroring_on

        # Movimento contínuo com setas
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            manual_tx -= movement_speed * dt
        if keys[K_RIGHT]:
            manual_tx += movement_speed * dt
        if keys[K_UP]:
            manual_ty += movement_speed * dt
        if keys[K_DOWN]:
            manual_ty -= movement_speed * dt

        # Atualiza as transformações oscilatórias
        if rotation_on:
            rotation_angle += rotation_speed * dt
        if translation_on:
            translation_offset = math.sin(time_elapsed) * translation_amplitude
        if scaling_on:
            scaling_factor = scaling_base + math.sin(time_elapsed) * scaling_variation

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Desenha o fundo estrelado
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(0, 0, -30)
        draw_stars(stars)
        glPopMatrix()

        # Aplica as transformações e desenha a nave
        glPushMatrix()
        glTranslatef(manual_tx + translation_offset, manual_ty, 0)
        glRotatef(rotation_angle, 0, 1, 0)
        glScalef(scaling_factor, scaling_factor, scaling_factor)
        if mirroring_on:
            glScalef(-1.0, 1.0, 1.0)
        spaceship.draw_spaceship()
        glPopMatrix()

        # Overlay com informações e controles
        glDisable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, screen_width, 0, screen_height)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        overlay_lines = [
            "Controles:",
            "R - Rotacao (ON/OFF): {}".format("ON" if rotation_on else "OFF"),
            "T - Translacao Oscilatoria (ON/OFF): {}".format("ON" if translation_on else "OFF"),
            "S - Escala Oscilatoria (ON/OFF): {}".format("ON" if scaling_on else "OFF"),
            "Setas - Mover a nave",
            "Q - Sair",
            "",
            "Parametros:",
            f"Rotacao: {rotation_angle:.2f}",
            f"Translacao: {translation_offset:.2f}",
            f"Escala: {scaling_factor:.2f}",
            f"Manual Tx: {manual_tx:.2f}",
            f"Manual Ty: {manual_ty:.2f}"
        ]
        y_offset = screen_height - 20
        for line in overlay_lines:
            draw_text(10, y_offset, line, font)
            y_offset -= 20

        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
