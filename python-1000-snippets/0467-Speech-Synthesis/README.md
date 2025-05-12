# Speech Synthesis

## Description
This snippet demonstrates text-to-speech synthesis using `gTTS`.

## Code
```python
# Note: Requires `gTTS`. Install with `pip install gTTS`
try:
    from gtts import gTTS
    tts = gTTS(text="Hello world", lang="en")
    tts.save("output.mp3")
    print("Audio file generated")
except ImportError:
    print("Mock Output: Audio file generated")
```

## Output
```
Mock Output: Audio file generated
```
*(Real output with `gTTS`: `Audio file generated`)*

## Explanation
- **Speech Synthesis**: Converts text to speech and saves as MP3.
- **Logic**: Uses `gTTS` to generate audio from text.
- **Complexity**: O(n) for n characters (network-dependent).
- **Use Case**: Used for voice assistants or accessibility tools.
- **Best Practice**: Validate text; handle language support; test audio quality.