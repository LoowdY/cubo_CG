# Nave Espacial Interativa

Este projeto demonstra uma nave espacial interativa utilizando OpenGL com Python e Pygame. A nave (baseada em um cubo modificado com um "bico") realiza transformações de rotação, translação e escala. Você pode controlá-la com as setas do teclado (movimento contínuo ao segurar) e alternar cada efeito com teclas de atalho. O fundo estrelado adiciona dinamismo à cena.  
**Agora, o overlay de texto utiliza alpha blending para remover a mancha branca, e o tamanho da nave está maior por padrão.**

## Funcionalidades

- **Rotação Contínua:** A nave pode rotacionar automaticamente.
- **Translação Oscilatória:** A nave se move de forma oscilatória (senoidal).
- **Escala Oscilatória:** A nave varia seu tamanho dinamicamente.
- **Espelhamento:** Ativa/desativa a reflexão no eixo X.
- **Movimento Manual:** Utilize as setas do teclado para mover a nave continuamente.
- **Fundo Estrelado:** Adiciona um efeito visual ao cenário.
- **Overlay Transparente:** A interface de texto foi atualizada para usar alpha blending, evitando manchas brancas.

## Controles

- **R:** Ativa/Desativa a rotação.
- **T:** Ativa/Desativa a translação oscilatória.
- **S:** Ativa/Desativa a escala oscilatória.
- **E:** Ativa/Desativa o espelhamento (reflexão) no eixo X.
- **Setas:** Movimentam a nave (mantendo a tecla pressionada, o movimento é contínuo).
- **Q:** Sai do programa.

## Requisitos

- Python 3.x
- Pygame
- PyOpenGL

Para instalar as dependências, execute:
```bash
pip install pygame PyOpenGL
```

## Estrutura do Projeto

- **cube.py**  
  Define a classe `Cube`, contendo os vértices e arestas do cubo, além do método `draw_spaceship()` para desenhar a nave espacial (cubo com “bico”).
  
- **main.py**  
  Configura o ambiente OpenGL/Pygame, implementa as transformações e a interação, renderiza a cena, desenha as estrelas de fundo e exibe um overlay de texto transparente (com alpha blending).

- **README.md**  
  Instruções para instalação, execução e uso do projeto (este arquivo).

## Executando o Projeto

Para executar o projeto, basta rodar o arquivo `main.py`:

```bash
python main.py
```

Uma janela será aberta exibindo a nave espacial interativa em wireframe com um fundo estrelado e um overlay transparente com as informações de controle e parâmetros atuais.

## Personalização

- Para **aumentar/diminuir** ainda mais o tamanho da nave, ajuste a variável `scaling_base` em `main.py`.  
- Para alterar a **quantidade de estrelas**, modifique `generate_stars(300, 50, 50, 50)` para o valor desejado.  
- Outros parâmetros, como velocidade de rotação, translação e movimento manual, podem ser alterados diretamente em `main.py`.

Sinta-se à vontade para expandir o projeto com novas funcionalidades, efeitos ou interações!
