import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from writeTospreadsheet import putDataToSpreadsheet
def translateAudioFile():
    model = whisper.load_model("tiny")
    result = model.transcribe("./recording0.wav")
  #  result = model.transcribe("./signal-2022-12-23-003115.aac")
    allWords = result["text"].split()
    firstWord = allWords[0]

    print(result["text"])
    return result["text"], firstWord

def recordAudioToFile():
    # import required libraries

    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 5

    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("recording0.wav", freq, recording)

    result, firstWord = translateAudioFile()
    putDataToSpreadsheet(audioRecording=str(result),firstWord=str(firstWord))

