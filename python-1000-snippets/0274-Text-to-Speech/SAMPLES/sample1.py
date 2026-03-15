# sample1.py
# Generate an MP3 file from text using gTTS (Google Text-to-Speech).

from gtts import gTTS


def main():
    text = "Hello world, this is a generated audio file from gTTS."
    out_path = "hello_tts.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(out_path)
    print(f"Saved TTS audio to {out_path}")


if __name__ == '__main__':
    main()
