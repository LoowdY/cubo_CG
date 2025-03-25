from OpenGL.GL import *

class Cube:
    """
    Classe para representar e desenhar um cubo no modo wireframe.
    O cubo é centrado na origem e possui dimensões 1x1x1.
    Também implementa o método draw_spaceship() para desenhar uma nave espacial
    baseada no cubo, com um "bico" adicionado.
    """
    def __init__(self):
        # Vértices do cubo
        self.vertices = [
            (0.5,  0.5,  0.5),
            (0.5,  0.5, -0.5),
            (0.5, -0.5,  0.5),
            (0.5, -0.5, -0.5),
            (-0.5,  0.5,  0.5),
            (-0.5,  0.5, -0.5),
            (-0.5, -0.5,  0.5),
            (-0.5, -0.5, -0.5)
        ]
        # Arestas definidas como pares de índices dos vértices
        self.edges = (
            (0, 1), (1, 3), (3, 2), (2, 0),  # Face direita
            (4, 5), (5, 7), (7, 6), (6, 4),  # Face esquerda
            (0, 4), (1, 5), (2, 6), (3, 7)   # Conexões entre faces
        )
        
    def draw_wireframe(self):
        """
        Desenha o cubo no modo wireframe, exibindo apenas as arestas.
        """
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
        
    def draw_spaceship(self):
        """
        Desenha uma nave espacial baseada no cubo, com um "bico" adicionado.
        """
        # Desenha a base da nave (cubo)
        self.draw_wireframe()
        
        # Desenha o "bico" da nave – uma pirâmide simples no topo do cubo
        nose = (0, 0.8, 0)  # Posição do bico acima do cubo
        top_indices = [0, 1, 4, 5]  # Vértices da face superior do cubo
        glBegin(GL_LINES)
        for i in top_indices:
            glVertex3fv(self.vertices[i])
            glVertex3fv(nose)
        glEnd()
