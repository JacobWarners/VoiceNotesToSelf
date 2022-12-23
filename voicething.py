import whisper

model = whisper.load_model("tiny")
result = model.transcribe("./signal-2022-12-23-003115.aac")
print(result["text"])