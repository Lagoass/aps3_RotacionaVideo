import numpy as np
import cv2 as cv
import itertools

def matrizR(angulo):
    theta = np.radians(angulo)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    R = np.array([[cos_theta, -sin_theta, 0],
                  [sin_theta, cos_theta, 0],
                  [0, 0, 1]])
    return R

def rotacionaImagem(image, angulo, pontoRotacao):
    T1 = np.array([[1, 0, -pontoRotacao[0]],
                   [0, 1, -pontoRotacao[1]],
                   [0, 0, 1]])
    R = matrizR(angulo)
    T2 = np.array([[1, 0, pontoRotacao[0]],
                   [0, 1, pontoRotacao[1]],
                   [0, 0, 1]])
    matrizTransformacao = np.dot(T2, np.dot(R, T1))
    imagemRotacionada = cv.warpPerspective(image, matrizTransformacao, (image.shape[1], image.shape[0]))
    return imagemRotacionada

def zoom_manual(image, valorZoom):
    height, width, _ = image.shape
    novoPontoRotacao = (width // 2, height // 2)
    
    # Matriz de zoom
    Z = np.array([[valorZoom, 0, 0],
                  [0, valorZoom, 0],
                  [0, 0, 1]])
    
    # Matriz de translação negativa para o pivô
    T1 = np.array([[1, 0, -novoPontoRotacao[0]],
                   [0, 1, -novoPontoRotacao[1]],
                   [0, 0, 1]])
    
    # Matriz de translação positiva para retornar ao ponto original após o zoom
    T2 = np.array([[1, 0, novoPontoRotacao[0]],
                   [0, 1, novoPontoRotacao[1]],
                   [0, 0, 1]])
    
    # Combinando as transformações
    matrizTransformacao = np.dot(T2, np.dot(Z, T1))
    
    # Aplicando a transformação na imagem
    image_zoomed = cv.warpPerspective(image, matrizTransformacao, (image.shape[1], image.shape[0]))
    
    return image_zoomed

def criar_indices(min_i, max_i, min_j, max_j):
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack( (idx_i, idx_j) )
    return idx

def run():
    cap = cv.VideoCapture(0)
    width = 600
    height = 300

    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    angulo = 0
    velocidadeRotacao = 0
    pontoRotacao = (width // 2, height // 2)
    valorZoom = 1.0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Não consegui capturar frame!")
            break

        image = np.array(frame).astype(np.uint8)

        if velocidadeRotacao != 0:
            angulo += velocidadeRotacao

        image_zoomed = zoom_manual(image, valorZoom)

        rotated_image = rotacionaImagem(image_zoomed, angulo, pontoRotacao)

        cv.imshow('Minha Imagem!', rotated_image)
        
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('d'):
            velocidadeRotacao += 1
        elif key == ord('a'):
            velocidadeRotacao -= 1
        elif key == ord('w'):
            valorZoom += 0.1
        elif key == ord('s'):
            valorZoom -= 0.1

    cap.release()
    cv.destroyAllWindows()

run()
