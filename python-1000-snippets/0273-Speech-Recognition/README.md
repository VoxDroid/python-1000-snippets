# Speech Recognition

## Description
This snippet demonstrates speech recognition using `speechrecognition`.

## Code
```python
# Note: Requires `speechrecognition` and `pyaudio`. Install with `pip install speechrecognition pyaudio`
try:
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source, timeout=1)
    text = recognizer.recognize_google(audio)
    print("Recognized:", text)
except:
    print("Mock Output: Recognized: hello world")
```

## Output
```
Mock Output: Recognized: hello world
```
*(Real output with `speechrecognition`: `Recognized: <spoken text>`)*

## Explanation
- **Speech Recognition**: Converts audio input to text using Google’s API.
- **Logic**: Listens via microphone and processes audio to text.
- **Complexity**: O(1) for API call (network latency varies).
- **Use Case**: Used for voice assistants or transcription.
- **Best Practice**: Handle noise; use offline models; secure API keys.