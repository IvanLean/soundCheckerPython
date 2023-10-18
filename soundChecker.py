import librosa
import numpy as np

def checkFirstSound(audio_file):

    y, sr = librosa.load(audio_file) # загрузка аудиофайла

    hop_length = int(sr / 1000)  # Определяем размер шага для 1 миллисекунды
    spectrogram = np.abs(librosa.stft(y, hop_length=hop_length))    # Преобразование аудиосигнала в спектрограмму


    # Вычисление средних частот для каждой миллисекунды
    average_frequencies = np.mean(spectrogram, axis=0)

    return average_frequencies

def checkSecondSound(audio_file):

    y, sr = librosa.load(audio_file) # загрузка аудиофайла

    
    hop_length = int(sr / 1000)  # Определяем размер шага для 1 миллисекунды
    spectrogram = np.abs(librosa.stft(y, hop_length=hop_length)) # Преобразование аудиосигнала в спектрограмму

    # Вычисление средних частот для каждого отрезка времени 
    average_frequencies = np.mean(spectrogram, axis=0)

    return average_frequencies





def checkSounds():
    result = []#
    resCount = 0
    firstParam = checkFirstSound("people.wav")
    secondParam = checkSecondSound("gudok2.wav")

    #вычисляем какой массив меньше и считаем относительно него цикл и получаем колличество подходящих данных

    if firstParam.size > secondParam.size: 
        print("1 option")
        for i in range(secondParam.size):
            if abs(firstParam[i]-secondParam[i])<0.1:
                resCount += 1

    elif firstParam.size < secondParam.size:
        print("2 option")
        for i in range(firstParam.size):
            if abs(firstParam[i]-secondParam[i])<0.1:
                resCount += 1


    minSize = min(firstParam.size, secondParam.size)
    print("FIRST:",firstParam)
    print("SECOND:",secondParam)
    print(result)
    print(minSize)
    print(resCount)
    print(minSize/resCount)

    if minSize/resCount < 10 and minSize/resCount != 0:
        print("Тип звуковых дорожек сходится")
    else:
        print("Тип звуковых дорожек НЕ сходится")



checkSounds()


