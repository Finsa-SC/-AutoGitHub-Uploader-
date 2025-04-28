from pydub.playback import play
from pydub import AudioSegment

def Notify():
    audio = AudioSegment.from_file("assets/Input.mpeg")
    play(audio)

def Uploaded():
    print("Upload Successfully!!")
    audio = AudioSegment.from_file("assets/Save.mpeg")
    play(audio)
