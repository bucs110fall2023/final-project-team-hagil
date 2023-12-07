import mutagen
from mutagen.wave import WAVE

def song_length(song_path):
    audio =WAVE(song_path)
    length=audio.info.length
    return length
