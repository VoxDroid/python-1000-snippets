# Text to Speech

## Description
This snippet demonstrates text-to-speech conversion using `pyttsx3`.

## Code
```python
# Note: Requires `pyttsx3`. Install with `pip install pyttsx3`
try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("Hello, world")
    engine.runAndWait()
    print("Speech generated")
except ImportError:
    print("Mock Output: Speech generated")
```

## Output
```
Mock Output: Speech generated
```
*(Real output with `pyttsx3`: `Speech generated`, plays audio)*

## Explanation
- **Text to Speech**: Converts text to spoken audio using `pyttsx3`.
- **Logic**: Initializes engine and speaks a phrase.
- **Complexity**: O(n) for n characters in text.
- **Use Case**: Used for accessibility or voice interfaces.
- **Best Practice**: Adjust voice settings; handle engine errors; test audio output.