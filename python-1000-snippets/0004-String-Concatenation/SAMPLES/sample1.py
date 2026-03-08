# sample1.py
# construct a full name and greeting message

def main():
    first_name = "Jane"
    last_name = "Doe"
    greeting = "Hello, " + first_name + " " + last_name + "!"
    f_greeting = f"Hello, {first_name} {last_name}!"
    print(greeting)
    print(f_greeting)

if __name__ == '__main__':
    main()

