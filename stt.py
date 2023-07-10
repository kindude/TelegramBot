
import os
import shutil
import tempfile
import speech_recognition as sr
from pydub import AudioSegment
from pydub import AudioSegment
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\ffmpeg\\ffprobe.exe"


class Transcriber:
    def __init__(self, language="ru-RU"):
        self.language = language


    def transcribe(self, file_path):
        # конвертировать файл в WAV формат, используя pydub
        self.temp_dir = tempfile.mkdtemp()
        temp_file = self.create_wav(file_path, self.temp_dir)
        # распознать речь с помощью Google Speech API, используя SpeechRecognition
        r = sr.Recognizer()
        with sr.AudioFile(temp_file) as source:
            audio = r.record(source)

        shutil.rmtree(self.temp_dir)

        try:
            text = r.recognize_google(audio, language='ru-RU')
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            raise Exception('Не удалось получить ответ от сервера Google Speech Recognition')


    def create_wav(self, file_path, temp_dir):
        sound = AudioSegment.from_file(file_path, format="ogg")
        temp_file = os.path.join(temp_dir, "temp.wav")
        sound.export(temp_file, format="wav")
        return temp_file
