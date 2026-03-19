# sample2.py
# List available voices in pyttsx3 and demonstrate selecting one.

import pyttsx3


def list_voices() -> None:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    print(f"Found {len(voices)} voices")
    for idx, v in enumerate(voices[:5], 1):
        print(f"{idx}. id={v.id} name={v.name} lang={getattr(v, 'languages', None)}")


def main() -> None:
    list_voices()


if __name__ == "__main__":
    main()
