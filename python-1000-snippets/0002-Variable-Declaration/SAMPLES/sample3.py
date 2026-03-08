# sample3.py
# Show dynamic typing: assign different types to the same variable name.

def main():
    var = 10
    print("var is", var, "(type", type(var), ")")
    var = "now I'm a string"
    print("var is", var, "(type", type(var), ")")
    var = [1, 2, 3]
    print("var is", var, "(type", type(var), ")")

if __name__ == '__main__':
    main()

