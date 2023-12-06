import mutagen
from mutagen.wave import WAVE

def audio_duration(length):
    second=length
    return second
audio =WAVE("final-project-team-hagil/assets/musics/careless.wav")

audio_info=audio.info
length=audio_info.length
audio_length=audio_duration(length)
print(audio_length)