# sample3.py
# Use named placeholders with .format()

def main():
    template = "Name: {name}, Score: {score}%"
    print(template.format(name="Alice", score=92))
    print(template.format(name="Bob", score=85))

if __name__ == '__main__':
    main()

