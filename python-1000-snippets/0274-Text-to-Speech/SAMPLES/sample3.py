# sample3.py
# Generate audio for multiple phrases using gTTS and save separate files.

from gtts import gTTS


def main():
    phrases = [
        "Python is a great programming language.",
        "This audio is generated automatically."  
    ]

    for i, text in enumerate(phrases, start=1):
        out = f"tts_phrase_{i}.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(out)
        print(f"Wrote {out}")


if __name__ == '__main__':
    main()
