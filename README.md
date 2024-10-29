# Implementação
## O programa foi implementado em Python, utilizando as bibliotecas NumPy e OpenCV (cv2). As principais funções são:

rotacionaImagem: Aplica uma rotação na imagem em torno de um ponto de rotação especificado.
zoom_manual: Aplica um zoom na imagem, alterando suas dimensões.
criar_indices: Cria uma matriz de índices para manipulação de pixels.
run: Função principal que controla a captura de vídeo, a aplicação de rotação e zoom, e a interação com o usuário por meio do teclado.
# Como Executar
## Para executar o programa, siga os passos abaixo:

- Certifique-se de ter o Python instalado no seu sistema.
- Instale as bibliotecas necessárias executando o comando pip install numpy opencv-python.
- Baixe o código-fonte deste projeto.
- Execute o arquivo Python main.py.
- Pressione as teclas A e D para controlar a velocidade de rotação.
- Pressione as teclas W e S para controlar o zoom.
- Pressione a tecla Q para sair do programa.

# Explicação do Modelo Matemático
## Rotação da Imagem
Para aplicar a rotação na imagem, utilizamos o conceito de transformação geométrica utilizando matrizes de transformação. O modelo matemático consiste em três etapas:

- Translação Negativa para o Pivô: Primeiramente, movemos o ponto de rotação para a origem, realizando uma translação negativa. Isso é feito para que a rotação ocorra em torno do ponto desejado.

- Rotação: Em seguida, aplicamos a matriz de rotação, que é uma matriz de transformação linear que rotaciona um ponto em torno da origem. Essa matriz é calculada a partir do ângulo de rotação especificado pelo usuário.

- Translação Positiva de Volta ao Ponto Original: Por fim, movemos o ponto de rotação de volta para a sua posição original, realizando uma translação positiva.

Zoom na Imagem
Para aplicar o zoom na imagem, também utilizamos matrizes de transformação. O modelo matemático é composto por duas etapas:

- Translação Negativa para o Pivô: Movemos o ponto de referência (centro da imagem) para a origem, realizando uma translação negativa.

- Aplicação da Matriz de Zoom: Aplicamos uma matriz de zoom, que amplia ou reduz as coordenadas dos pixels da imagem, dependendo do valor de zoom especificado pelo usuário.

- Translação Positiva de Volta ao Ponto Original: Movemos o ponto de referência de volta para a sua posição original, realizando uma translação positiva.

# Detalhes das Matrizes de Transformação
## Matriz de Rotação (R)
A matriz de rotação (R) é uma matriz 3x3 que representa uma rotação bidimensional em torno da origem (0,0). Ela é calculada utilizando as funções trigonométricas cosseno e seno do ângulo de rotação (θ). A matriz é dada por:<br>

R = | cos(θ)  -sin(θ)  0 |<br>
    | sin(θ)   cos(θ)  0 |<br>
    |   0        0     1 |<br>
# Matriz de Zoom (Z)
## A matriz de zoom (Z) é uma matriz diagonal 3x3 que amplia ou reduz as coordenadas dos pixels da imagem. Ela é dada por:

Z = | Sx   0   0 |<br>
    |  0  Sy   0 |<br>
    |  0   0   1 |<br>
Onde Sx e Sy são os fatores de escala horizontal e vertical, respectivamente.

Matrizes de Translação (T1 e T2)
As matrizes de translação (T1 e T2) são matrizes 3x3 que realizam translações de coordenadas. T1 é utilizada para mover o ponto de referência para a origem (translação negativa), enquanto T2 é utilizada para movê-lo de volta para a sua posição original (translação positiva). Essas matrizes são dadas por:

T1 = | 1  0  -Tx |<br>
     | 0  1  -Ty |<br>
     | 0  0   1  |<br>

T2 = | 1  0   Tx |<br>
     | 0  1   Ty |<br>
     | 0  0   1  |<br>
Onde Tx e Ty são as quantidades de translação ao longo dos eixos x e y, respectivamente.
