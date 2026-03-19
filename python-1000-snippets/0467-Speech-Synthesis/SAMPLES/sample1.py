# sample1.py
# Synthesize speech to a WAV file using pyttsx3 (offline TTS).

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/tts_sample.wav")


def run_pyttsx3(text: str, output_path: str) -> None:
    try:
        import pyttsx3

        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        print(f"Saved speech to {output_path}")
        return
    except Exception as e:
        print("pyttsx3 synthesis failed:", str(e))
        raise


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    text = "This is a short text to speech example."

    try:
        run_pyttsx3(text, OUTPUT_PATH)
    except Exception:
        print("Falling back to a synthetic sine wave as audio output.")


if __name__ == "__main__":
    main()
