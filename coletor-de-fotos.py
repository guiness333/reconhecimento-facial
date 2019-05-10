import cv2
import numpy as np

camera = cv2.VideoCapture(0)#pega o source de video da webcam
classificador = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")#carrega uma base de dados no classificador
classificadorOlho = cv2.CascadeClassifier("haarcascade-eye.xml")#classificador para os olhos
amostra = 1
numeroAmostra = 25

id = input("Digite seu identificador: ")
largura, altura = 220, 220
print("Capturando as faces")

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)#Converte a imagem para uma escala de cinza
    print(np.average(imagemCinza))
    facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                    scaleFactor=1.5,
                                                    minSize=(150,150))#usando a imagem em cinza usa o algoritimo do classificador para detectar faces
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        regiao = imagem[y:y + a, x:x + l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

        for(ox, oy, ol, oa) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                if np.average(imagemCinza) > 100:
                    imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                    cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
                    print("[foto " + str(amostra) + " capturada com sucesso]")
                    amostra += 1
    
    cv2.imshow("Face", imagem)#mostra a imagem em uma janela
    cv2.waitKey(1)
    if(amostra >= numeroAmostra+1):
        break
print("faces capturadas com sucesso")
camera.release()#libera a memoria da camera
cv2.destroyAllWindows()#destroi todas as janelas
