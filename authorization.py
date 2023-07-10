import difflib

import speech_recognition as sr



def compare_voices(file1_path, file2_path):
    r = sr.Recognizer()

    # Распознавание речи из первого аудиофайла
    with sr.AudioFile(file1_path) as source:
        audio1 = r.record(source)

    # Распознавание речи из второго аудиофайла
    with sr.AudioFile(file2_path) as source:
        audio2 = r.record(source)

    # Сравнение распознанных текстов
    try:
        text1 = r.recognize_google(audio1)
        text2 = r.recognize_google(audio2)

        similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
        return similarity

    except sr.UnknownValueError:
        print("Ошибка распознавания речи")
        return None
    except sr.RequestError:
        print("Ошибка при обращении к сервису распознавания речи")
        return None