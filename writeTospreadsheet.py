import pandas as pd
from datetime import datetime
import sounddevice as sd
from scipy.io.wavfile import write
now = datetime.now()

def recordAudioToFile():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file 




def putDataToSpreadsheet(audioRecording):
    d = {'col1': [str(audioRecording)], 'col2': [now.strftime("%d/%m/%Y %H:%M:%S")],'col3': [str('firstword')]}
    df = pd.DataFrame(data=d)
    print(df)
    df.to_excel('RecordedNotes.xlsx')
putDataToSpreadsheet(audioRecording='test')


