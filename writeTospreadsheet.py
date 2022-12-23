import pandas as pd
from datetime import datetime

now = datetime.now()

def putDataToSpreadsheet(audioRecording):
    d = {'col1': [str(audioRecording)], 'col2': [now.strftime("%d/%m/%Y %H:%M:%S")],'col3': [str('firstword')]}
    df = pd.DataFrame(data=d)
    print(df)
    df.to_excel('RecordedNotes.xlsx')
putDataToSpreadsheet(audioRecording='test')


