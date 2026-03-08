# sample2.py
# Simulate a simple login check with username/password

def check_login(user, pwd):
    if user == "admin" and pwd == "secret":
        return "Access granted"
    elif user == "guest":
        return "Guest access"
    else:
        return "Access denied"

if __name__ == '__main__':
    u = input("Username: ")
    p = input("Password: ")
    print(check_login(u, p))

