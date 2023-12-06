import mutagen
from mutagen.wave import WAVE


audio =WAVE("final-project-team-hagil/assets/musics/careless.wav")
length=audio.info.length
print(length)

