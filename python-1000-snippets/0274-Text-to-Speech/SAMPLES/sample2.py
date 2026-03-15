# sample2.py
# Use pyttsx3 to generate speech audio to a WAV file.

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None


def main():
    if pyttsx3 is None:
        print("pyttsx3 not installed; please install with `pip install pyttsx3`");
        return

    engine = pyttsx3.init()
    text = "This is a test of pyttsx3 text to speech."
    out_path = "pyttsx3_output.wav"
    engine.save_to_file(text, out_path)
    engine.runAndWait()
    print(f"Saved TTS audio to {out_path}")


if __name__ == '__main__':
    main()
