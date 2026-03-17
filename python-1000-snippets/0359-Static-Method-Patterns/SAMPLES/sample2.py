# sample2.py
# Static method used as a helper within a class

class TextUtils:
    @staticmethod
    def sanitize(text):
        return text.strip().lower()

    def clean_and_prefix(self, text):
        return "Mr. " + TextUtils.sanitize(text)


def main():
    t = TextUtils()
    print(t.clean_and_prefix("  Alice  "))


if __name__ == "__main__":
    main()
